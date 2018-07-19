import gzip
import json
import ssl

import websocket

from const import Wss_Url, SubType


class CoinTigerWebSocket(object):
    pairs = []
    sub_type_dict = {}
    sub_dict = {
        'ticker': 'market_{}_ticker',
        'trade_ticker': 'market_{}_trade_ticker',
        'depth': 'market_{}_depth_{}',
        'kline': 'market_{}_kline_{}',
    }

    channel_dict = {}

    def on_open(self, ws):
        for pair in self.pairs:
            # 订阅
            for sub_type in self.sub_type_dict.keys():
                if sub_type in [SubType.Depth.value, SubType.Kline.value]:
                    channel = self.sub_dict[sub_type].format(pair, self.sub_type_dict[sub_type]['param'])
                else:
                    channel = self.sub_dict[sub_type].format(pair)

                json_send = {
                    'event': 'sub',
                    'params': {
                        'channel': channel,
                        'id': '{0}-{1}'.format(sub_type, pair),
                    }
                }
                ws.send(json.dumps(json_send))
                self.channel_dict[channel] = {
                    'type': sub_type,
                    'pair': pair
                }

    def on_message(self, ws, evt):
        try:
            data = json.loads(gzip.decompress(evt))
            if 'ping' in data.keys():  # 心跳
                json_send = {
                    'pong': data['ping']
                }
                ws.send(json.dumps(json_send))
                print('heartbeat')
            elif 'channel' in data.keys():
                pair = self.channel_dict[data['channel']]['pair']
                tick_type = self.channel_dict[data['channel']]['type']
                self.sub_type_dict[tick_type]['callback'](pair, data)
        except Exception as e:
            print('msg error: {}'.format(e))

    def on_error(self, ws, evt):
        print('error: {}'.format(evt))

    def on_close(self, ws):
        print('websocket closed')

    def set_pairs(self, pairs):
        if not isinstance(pairs, list):
            exit(1)
        self.pairs = pairs

    def set_sub_type_dict(self, sub_type_dict):
        self.sub_type_dict = sub_type_dict
        for item in sub_type_dict.keys():
            if item not in self.sub_dict.keys():
                exit(1)

    def req_once(self, channel):



    def tick_forever(self):
        if not self.sub_type_dict:
            print('set sub type first')
            exit(1)
        if not self.pairs:
            print('set pairs first')
            exit(1)

        ws = websocket.WebSocketApp(Wss_Url,
                                    on_message=self.on_message,
                                    on_error=self.on_error,
                                    on_close=self.on_close,
                                    on_open=self.on_open)
        print('websocket started')
        ws.run_forever(sslopt={"cert_reqs": ssl.CERT_NONE})


cointiger_websocket = CoinTigerWebSocket()
