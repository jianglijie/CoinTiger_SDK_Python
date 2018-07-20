from cointiger_sdk import cointiger_websocket
from cointiger_sdk import const


def ticker_callback(pair, data):
    print('ticker', pair, data)


def trade_ticker_callback(pair, data):
    print('trade_ticker', pair, data)


def depth_callback(pair, data):
    print('depth', pair, data)


def kline_callback(pair, data):
    print('kline', pair, data)


type_dict = {
    const.SubType.TradeTicker.value: {
        'callback': trade_ticker_callback
    },
    const.SubType.Ticker.value: {
        'callback': ticker_callback
    },
    const.SubType.Depth.value: {
        'callback': depth_callback,
        'param': 'step0'
    },
    const.SubType.Kline.value: {
        'callback': kline_callback,
        'param': '1min'
    },
}
cointiger_websocket.set_sub_type_dict(type_dict)
cointiger_websocket.set_pairs(['btcusdt', 'ethusdt'])
cointiger_websocket.tick_forever()