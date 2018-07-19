import requests
import urllib3

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)


def request_get(url, timeout=10, connection='keep-alive', params=None):
    with requests.Session() as session:
        header = {'Connection': connection,
                  'Cache-Control': 'max-age=0',
                  'Upgrade-Insecure-Requests': '1',
                  'User-Agent': "Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.0.8) Gecko Fedora/1.9.0.8-1.fc10 Kazehakase/0.5.6",
                  'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
                  'Accept-Encoding': 'gzip, deflate, sdch',
                  'Accept-Language': 'zh-CN,zh;q=0.8',
                  }
        data = session.get(url, headers=header, timeout=timeout, verify=False, params=params).json()
        if data:
            if data.get('code', None) == '0':
                return data['data']
            else:
                return data
        else:
            return {}


def request_post(url, data):
    with requests.Session() as session:
        res = session.post(url, data=data)
        return res.text
