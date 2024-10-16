import json
import socket
import threading
import time
import logging
from dtc_types import DTCMessageType, LogonRequest, Heartbeat, HistoricalOrderFillResponse, DTCVersion


class Client:
    def __init__(self):
        self.conn = None
        self.fill_request_handler = None
        self.is_running = False

    def connect(self):
        self.conn = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.conn.connect(('127.0.0.1', 11099))
        print("Connected to DTC server")

    def do_logon(self):
        request = LogonRequest(
            Type=DTCMessageType.LOGON_REQUEST,
            ProtocolVersion=DTCVersion.CURRENT_VERSION,
            Username="",
            Password="",
            GeneralTextData="",
            Integer_1=0,
            Integer_2=0,
            HeartbeatIntervalInSeconds=60,
            Unused1=0,
            TradeAccount="",
            HardwareIdentifier="",
            ClientName="pyDTC",
            MarketDataTransmissionInterval=0
        )

        self.send_request(request)
        response = self.read_response()
        if response.get('Type') != DTCMessageType.LOGON_RESPONSE:
            raise Exception("Unexpected response type")
        return response

    def do_heartbeat(self):
        self.is_running = True
        while self.is_running:
            try:
                time.sleep(5)
                hb = Heartbeat(
                    Type=DTCMessageType.HEARTBEAT,
                    NumDroppedMessages=0,
                    CurrentDateTime=int(time.time())
                )
                self.send_request(hb)
            except Exception as e:
                logging.error(f"Error in heartbeat: {str(e)}")
                break
        logging.info("Heartbeat thread exiting")

    def stop(self):
        self.is_running = False
        if self.conn:
            self.conn.close()

    def send_request(self, data):
        json_data = json.dumps(data.__dict__)
        self.conn.sendall(json_data.encode() + b'\0')

    def read_response(self):
        buffer = b''
        while True:
            chunk = self.conn.recv(4096)
            if not chunk:
                raise Exception("Connection closed")
            buffer += chunk
            if b'\0' in buffer:
                message, buffer = buffer.split(b'\0', 1)
                return json.loads(message.decode())

    def RequestHistoricalFills(self, trade_account, number_of_days):
        request = {
            'Type': DTCMessageType.HISTORICAL_ORDER_FILLS_REQUEST,
            'RequestID': 1,
            'ServerOrderID': 0,
            'TradeAccount': trade_account,
            'NumberOfDays': number_of_days,
            'StartDateTime': 0
        }

        self.send_request(request)

        responses = []
        while True:
            response = self.read_response()
            if response['Type'] != DTCMessageType.HISTORICAL_ORDER_FILL_RESPONSE:
                continue
            responses.append(HistoricalOrderFillResponse(**response))
            if response['MessageNumber'] == response['TotalNumberMessages']:
                return responses

        raise Exception("Incomplete read of HistoricalFill responses")


def NewClient():
    client = Client()
    heartbeat_thread = None
    try:
        client.connect()
        client.do_logon()
        logging.info("Successfully logged on to DTC server")

        # Start the heartbeat in a separate thread
        heartbeat_thread = threading.Thread(target=client.do_heartbeat, daemon=True)
        heartbeat_thread.start()

        return client, heartbeat_thread
    except Exception as e:
        logging.error(f"Failed to create client: {str(e)}")
        if client:
            client.stop()
        raise


# Usage example
if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    try:
        client, heartbeat_thread = NewClient()

        # Your main program logic here
        # ...

        # Wait for the heartbeat thread to exit
        heartbeat_thread.join()
        logging.info("Heartbeat thread has exited, shutting down")
    except Exception as e:
        logging.error(f"An error occurred: {str(e)}")
    finally:
        if 'client' in locals():
            client.stop()