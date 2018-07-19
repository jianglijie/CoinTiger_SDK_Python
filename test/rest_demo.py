import time

from cointiger_sdk.CoinTiger import cointiger
from cointiger_sdk.const import SideType, OrderType

# 时间戳
print(cointiger.timestamp())
# 支持币种
print(cointiger.currencys())

# 24小时行情
print(cointiger.ticker('btcusdt'))
# 深度
print(cointiger.depth('btcusdt'))
# k线
print(cointiger.kline('btcusdt', '1min'))
# 成交历史
print(cointiger.trade('btcusdt'))
# 24小时行情列表
print(cointiger.tickers())

api_key = 'xxxxxx'
secret = 'xxxxxxxxxxx'
cointiger.set_key_and_secret(api_key, secret)

order_data = {
    'api_key': api_key,
    'symbol': 'btcusdt',
    'price': '0.01',
    'volume': '1',
    'side': SideType.BUY.value,
    'type': OrderType.LimitOrder.value,
    'time': int(time.time())
}
# 签名
print(cointiger.get_sign(order_data))
# 创建订单
print(cointiger.order(dict(order_data, **{'sign': cointiger.get_sign(order_data)})))

# 撤销订单
cancel_data = {
    'api_key': api_key,
    'orderIdList': '{"btcusdt":["1","2"],"ethusdt":["11","22"]}',
    'time': int(time.time()),
}
print(cointiger.batch_cancel(dict(cancel_data, **{'sign': cointiger.get_sign(cancel_data)})))

# 查询委托
print(cointiger.orders('btcusdt', 'canceled', int(time.time()), types='buy-market'))

# 查询成交
print(cointiger.match_results('btcusdt', '2018-07-18', '2018-07-19', int(time.time())))

# 查询成交明细
print(cointiger.make_detail('btcusdt', '123', int(time.time())))

# 查询订单详情
print(cointiger.details('btcusdt', '123', int(time.time())))
