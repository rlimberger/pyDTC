from enum import IntEnum

class DTCVersion(IntEnum):
    DTC_VERSION_UNSET = 0
    CURRENT_VERSION = 8

class DTCMessageType(IntEnum):
    MESSAGE_TYPE_UNSET = 0
    # Authentication and connection monitoring
    LOGON_REQUEST = 1
    LOGON_RESPONSE = 2
    HEARTBEAT = 3
    LOGOFF = 5
    ENCODING_REQUEST = 6
    ENCODING_RESPONSE = 7
    # Market data
    MARKET_DATA_REQUEST = 101
    MARKET_DATA_REJECT = 103
    MARKET_DATA_SNAPSHOT = 104
    MARKET_DATA_UPDATE_TRADE = 107
    MARKET_DATA_UPDATE_TRADE_COMPACT = 112
    MARKET_DATA_UPDATE_LAST_TRADE_SNAPSHOT = 134
    MARKET_DATA_UPDATE_TRADE_WITH_UNBUNDLED_INDICATOR = 137
    MARKET_DATA_UPDATE_TRADE_WITH_UNBUNDLED_INDICATOR_2 = 146
    MARKET_DATA_UPDATE_TRADE_NO_TIMESTAMP = 142
    MARKET_DATA_UPDATE_BID_ASK = 108
    MARKET_DATA_UPDATE_BID_ASK_COMPACT = 117
    MARKET_DATA_UPDATE_BID_ASK_NO_TIMESTAMP = 143
    MARKET_DATA_UPDATE_BID_ASK_FLOAT_WITH_MICROSECONDS = 144
    MARKET_DATA_UPDATE_SESSION_OPEN = 120
    MARKET_DATA_UPDATE_SESSION_HIGH = 114
    MARKET_DATA_UPDATE_SESSION_LOW = 115
    MARKET_DATA_UPDATE_SESSION_VOLUME = 113
    MARKET_DATA_UPDATE_OPEN_INTEREST = 124
    MARKET_DATA_UPDATE_SESSION_SETTLEMENT = 119
    MARKET_DATA_UPDATE_SESSION_NUM_TRADES = 135
    MARKET_DATA_UPDATE_TRADING_SESSION_DATE = 136
    MARKET_DEPTH_REQUEST = 102
    MARKET_DEPTH_REJECT = 121
    MARKET_DEPTH_SNAPSHOT_LEVEL = 122
    MARKET_DEPTH_SNAPSHOT_LEVEL_FLOAT = 145
    MARKET_DEPTH_UPDATE_LEVEL = 106
    MARKET_DEPTH_UPDATE_LEVEL_FLOAT_WITH_MILLISECONDS = 140
    MARKET_DEPTH_UPDATE_LEVEL_NO_TIMESTAMP = 141
    MARKET_DATA_FEED_STATUS = 100
    MARKET_DATA_FEED_SYMBOL_STATUS = 116
    TRADING_SYMBOL_STATUS = 138
    MARKET_ORDERS_REQUEST = 150
    MARKET_ORDERS_REJECT = 151
    MARKET_ORDERS_ADD = 152
    MARKET_ORDERS_MODIFY = 153
    MARKET_ORDERS_REMOVE = 154
    MARKET_ORDERS_SNAPSHOT_MESSAGE_BOUNDARY = 155
    # Order entry and modification
    SUBMIT_NEW_SINGLE_ORDER = 208
    SUBMIT_NEW_OCO_ORDER = 201
    SUBMIT_FLATTEN_POSITION_ORDER = 209
    FLATTEN_POSITIONS_FOR_TRADE_ACCOUNT = 210
    CANCEL_ORDER = 203
    CANCEL_REPLACE_ORDER = 204
    # Trading related
    OPEN_ORDERS_REQUEST = 300
    OPEN_ORDERS_REJECT = 302
    ORDER_UPDATE = 301
    HISTORICAL_ORDER_FILLS_REQUEST = 303
    HISTORICAL_ORDER_FILL_RESPONSE = 304
    HISTORICAL_ORDER_FILLS_REJECT = 308
    CURRENT_POSITIONS_REQUEST = 305
    CURRENT_POSITIONS_REJECT = 307
    POSITION_UPDATE = 306
    ADD_CORRECTING_ORDER_FILL = 309
    CORRECTING_ORDER_FILL_RESPONSE = 310
    # Account list
    TRADE_ACCOUNTS_REQUEST = 400
    TRADE_ACCOUNT_RESPONSE = 401
    # Symbol discovery and security definitions
    EXCHANGE_LIST_REQUEST = 500
    EXCHANGE_LIST_RESPONSE = 501
    SYMBOLS_FOR_EXCHANGE_REQUEST = 502
    UNDERLYING_SYMBOLS_FOR_EXCHANGE_REQUEST = 503
    SYMBOLS_FOR_UNDERLYING_REQUEST = 504
    SECURITY_DEFINITION_FOR_SYMBOL_REQUEST = 506
    SECURITY_DEFINITION_RESPONSE = 507
    SYMBOL_SEARCH_REQUEST = 508
    SECURITY_DEFINITION_REJECT = 509
    # Account balance
    ACCOUNT_BALANCE_REQUEST = 601
    ACCOUNT_BALANCE_REJECT = 602
    ACCOUNT_BALANCE_UPDATE = 600
    ACCOUNT_BALANCE_ADJUSTMENT = 607
    ACCOUNT_BALANCE_ADJUSTMENT_REJECT = 608
    ACCOUNT_BALANCE_ADJUSTMENT_COMPLETE = 609
    HISTORICAL_ACCOUNT_BALANCES_REQUEST = 603
    HISTORICAL_ACCOUNT_BALANCES_REJECT = 604
    HISTORICAL_ACCOUNT_BALANCE_RESPONSE = 606
    # Logging
    USER_MESSAGE = 700
    GENERAL_LOG_MESSAGE = 701
    ALERT_MESSAGE = 702
    JOURNAL_ENTRY_ADD = 703
    JOURNAL_ENTRIES_REQUEST = 704
    JOURNAL_ENTRIES_REJECT = 705
    JOURNAL_ENTRY_RESPONSE = 706
    # Historical price data
    HISTORICAL_PRICE_DATA_REQUEST = 800
    HISTORICAL_PRICE_DATA_RESPONSE_HEADER = 801
    HISTORICAL_PRICE_DATA_REJECT = 802
    HISTORICAL_PRICE_DATA_RECORD_RESPONSE = 803
    HISTORICAL_PRICE_DATA_TICK_RECORD_RESPONSE = 804
    HISTORICAL_PRICE_DATA_RESPONSE_TRAILER = 807
    # Historical market depth data
    HISTORICAL_MARKET_DEPTH_DATA_REQUEST = 900
    HISTORICAL_MARKET_DEPTH_DATA_RESPONSE_HEADER = 901
    HISTORICAL_MARKET_DEPTH_DATA_REJECT = 902
    HISTORICAL_MARKET_DEPTH_DATA_RECORD_RESPONSE = 903
    # Nonstandard
    TRADE_ACCOUNT_TRADING_IS_DISABLED_REQUEST = 10206
    TRADE_ACCOUNT_TRADING_IS_DISABLED_RESPONSE = 10207
    TRADE_ACCOUNT_DATA_DUPLICATE = 10208

class OpenCloseTradeEnum(IntEnum):
    TRADE_UNSET = 0
    TRADE_OPEN = 1
    TRADE_CLOSE = 2

class BuySellEnum(IntEnum):
    BUY_SELL_UNSET = 0
    BUY = 1
    SELL = 2

class LogonStatusEnum(IntEnum):
    LOGON_STATUS_UNSET = 0
    LOGON_SUCCESS = 1
    LOGON_ERROR = 2
    LOGON_ERROR_NO_RECONNECT = 3
    LOGON_RECONNECT_NEW_ADDRESS = 4

class HistoricalOrderFillResponse:
    def __init__(self, **kwargs):
        self.Type = kwargs.get('Type')
        self.RequestID = kwargs.get('RequestID')
        self.TotalNumberMessages = kwargs.get('TotalNumberMessages')
        self.MessageNumber = kwargs.get('MessageNumber')
        self.Symbol = kwargs.get('Symbol')
        self.Exchange = kwargs.get('Exchange')
        self.ServerOrderID = kwargs.get('ServerOrderID')
        self.BuySell = kwargs.get('BuySell')
        self.Price = kwargs.get('Price')
        self.DateTime = kwargs.get('DateTime')
        self.Quantity = kwargs.get('Quantity')
        self.UniqueExecutionID = kwargs.get('UniqueExecutionID')
        self.TradeAccount = kwargs.get('TradeAccount')
        self.OpenClose = kwargs.get('OpenClose')
        self.NoOrderFills = kwargs.get('NoOrderFills')
        self.InfoText = kwargs.get('InfoText')
        self.HighPriceDuringPosition = kwargs.get('HighPriceDuringPosition')
        self.LowPriceDuringPosition = kwargs.get('LowPriceDuringPosition')
        self.PositionQuantity = kwargs.get('PositionQuantity')
        self.Username = kwargs.get('Username')
        self.ExchangeOrderID = kwargs.get('ExchangeOrderID')
        self.SenderSubID = kwargs.get('SenderSubID')

class FillsRequest:
    def __init__(self, **kwargs):
        self.Type = kwargs.get('Type')
        self.RequestID = kwargs.get('RequestID')
        self.ServerOrderID = kwargs.get('ServerOrderID')
        self.TradeAccount = kwargs.get('TradeAccount')
        self.NumberOfDays = kwargs.get('NumberOfDays')
        self.StartDateTime = kwargs.get('StartDateTime')

class LogonRequest:
    def __init__(self, **kwargs):
        self.Type = kwargs.get('Type')
        self.ProtocolVersion = kwargs.get('ProtocolVersion')
        self.Username = kwargs.get('Username')
        self.Password = kwargs.get('Password')
        self.GeneralTextData = kwargs.get('GeneralTextData')
        self.Integer_1 = kwargs.get('Integer_1')
        self.Integer_2 = kwargs.get('Integer_2')
        self.HeartbeatIntervalInSeconds = kwargs.get('HeartbeatIntervalInSeconds')
        self.Unused1 = kwargs.get('Unused1')
        self.TradeAccount = kwargs.get('TradeAccount')
        self.HardwareIdentifier = kwargs.get('HardwareIdentifier')
        self.ClientName = kwargs.get('ClientName')
        self.MarketDataTransmissionInterval = kwargs.get('MarketDataTransmissionInterval')

class LogonResponse:
    def __init__(self, **kwargs):
        self.Type = kwargs.get('Type')
        self.ProtocolVersion = kwargs.get('ProtocolVersion')
        self.Result = kwargs.get('Result')
        self.ResultText = kwargs.get('ResultText')
        self.ReconnectAddress = kwargs.get('ReconnectAddress')
        self.Integer_1 = kwargs.get('Integer_1')
        self.ServerName = kwargs.get('ServerName')
        self.MarketDepthUpdatesBestBidAndAsk = kwargs.get('MarketDepthUpdatesBestBidAndAsk')
        self.TradingIsSupported = kwargs.get('TradingIsSupported')
        self.OCOOrdersSupported = kwargs.get('OCOOrdersSupported')
        self.OrderCancelReplaceSupported = kwargs.get('OrderCancelReplaceSupported')
        self.SymbolExchangeDelimiter = kwargs.get('SymbolExchangeDelimiter')
        self.SecurityDefinitionsSupported = kwargs.get('SecurityDefinitionsSupported')
        self.HistoricalPriceDataSupported = kwargs.get('HistoricalPriceDataSupported')
        self.ResubscribeWhenMarketDataFeedAvailable = kwargs.get('ResubscribeWhenMarketDataFeedAvailable')
        self.MarketDepthIsSupported = kwargs.get('MarketDepthIsSupported')
        self.OneHistoricalPriceDataRequestPerConnection = kwargs.get('OneHistoricalPriceDataRequestPerConnection')
        self.BracketOrdersSupported = kwargs.get('BracketOrdersSupported')
        self.Unused_1 = kwargs.get('Unused_1')
        self.UsesMultiplePositionsPerSymbolAndTradeAccount = kwargs.get('UsesMultiplePositionsPerSymbolAndTradeAccount')
        self.MarketDataSupported = kwargs.get('MarketDataSupported')

class Heartbeat:
    def __init__(self, **kwargs):
        self.Type = kwargs.get('Type')
        self.NumDroppedMessages = kwargs.get('NumDroppedMessages')
        self.CurrentDateTime = kwargs.get('CurrentDateTime')

class MessageBase:
    def __init__(self, **kwargs):
        self.Type = kwargs.get('Type')