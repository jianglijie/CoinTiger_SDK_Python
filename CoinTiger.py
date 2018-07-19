import hashlib
import hmac

from const import *
from function import request_get, request_post


class CoinTiger(object):
    _api_key = None
    _secret = None

    def set_key_and_secret(self, api_key, secret):
        self._api_key = api_key
        self._secret = secret

    @staticmethod
    def timestamp():
        return request_get('{}/timestamp'.format(Trading_Macro_v2))

    @staticmethod
    def currencys():
        return request_get('{}/currencys'.format(Trading_Macro_v2))

    @staticmethod
    def tickers():
        return request_get(Market_List)

    @staticmethod
    def ticker(symbol):
        return request_get('{0}/market/detail?symbol={1}'.format(Trading_Macro, symbol))

    @staticmethod
    def ticker(symbol):
        return request_get('{0}/market/detail?symbol={1}'.format(Trading_Macro, symbol))

    @staticmethod
    def depth(symbol, type='step0'):
        return request_get('{0}/market/depth?symbol={1}&type={2}'.format(Trading_Macro, symbol, type))

    @staticmethod
    def kline(symbol, period, size=150):
        return request_get(
            '{0}/market/history/kline?symbol={1}&period={2}&size={3}'.format(Trading_Macro, symbol, period, size))

    @staticmethod
    def trade(symbol, size=1):
        return request_get('{0}/market/history/trade?symbol={1}&size={2}'.format(Trading_Macro, symbol, size))

    def get_sign(self, data):
        if not isinstance(data, dict) or not self._secret:
            return ''
        string = ''
        for item in [(k, data[k]) for k in sorted(data.keys())]:
            if item[0] == 'api_key':
                continue
            string = '{}{}{}'.format(string, item[0], item[1])
        string = '{}{}'.format(string, self._secret)
        sign = hmac.new(bytes(self._secret.encode()), string.encode(), hashlib.sha512).hexdigest()
        return sign

    @staticmethod
    def order(data):
        return request_post('{}/order'.format(Trading_Macro_v2), data)

    @staticmethod
    def batch_cancel(data):
        return request_post('{}/order/batch_cancel'.format(Trading_Macro_v2), data)

    def orders(self, symbol, states, time, **kwargs):
        params = dict({
            'api_key': self._api_key,
            'symbol': symbol,
            'states': states,
            'time': time,
        }, **kwargs)
        return request_get('{}/order/orders'.format(Trading_Macro_v2),
                           params=dict(params, **{'sign': self.get_sign(params)}))

    def match_results(self, symbol, start_date, end_date, time, **kwargs):
        params = dict({
            'api_key': self._api_key,
            'symbol': symbol,
            'start-date': start_date,
            'end-date': end_date,
            'time': time,
        }, **kwargs)
        return request_get('{}/order/match_results'.format(Trading_Macro_v2),
                           params=dict(params, **{'sign': self.get_sign(params)}))

    def make_detail(self, symbol, order_id, time):
        params = {
            'api_key': self._api_key,
            'symbol': symbol,
            'order_id': order_id,
            'time': time,
        }
        return request_get('{}/order/make_detail'.format(Trading_Macro_v2),
                           params=dict(params, **{'sign': self.get_sign(params)}))

    def details(self, symbol, order_id, time):
        params = {
            'api_key': self._api_key,
            'symbol': symbol,
            'order_id': order_id,
            'time': time,
        }
        return request_get('{}/order/make_detail'.format(Trading_Macro_v2),
                           params=dict(params, **{'sign': self.get_sign(params)}))


cointiger = CoinTiger()
