from enum import Enum, unique

Trading_Macro_v2 = 'https://api.cointiger.pro/exchange/trading/api/v2'
Trading_Macro = 'https://api.cointiger.pro/exchange/trading/api'
Market_Macro = 'https://api.cointiger.pro/exchange/trading/api/market'
Market_List = 'https://www.cointiger.pro/exchange/api/public/market/detail'
Wss_Url = 'wss://api.cointiger.pro/exchange-market/ws'


@unique
class SideType(Enum):
    BUY = 'BUY'
    SELL = 'SELL'


@unique
class OrderType(Enum):
    LimitOrder = 1
    MarketOrder = 2


@unique
class SubType(Enum):
    Ticker = 'ticker'
    TradeTicker = 'trade_ticker'
    Depth = 'depth'
    Kline = 'kline'
