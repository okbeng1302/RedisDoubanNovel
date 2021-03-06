import random
import base64
from ZhihuCS.settings import PROXIES

class RandomProxy(object):
    def process_request(self, request, spider):
        proxy = random.choice(PROXIES)
        if proxy['user_pass'] is not None:
            request.meta['proxy'] = "http://%s" % proxy['ip_port']
            encoded_user_pass = base64.encodestring(proxy['user_pass'])
            request.headers['Proxy-Authorization'] = 'Basic' + encoded_user_pass
        else:
            request.meta['proxy'] = "http://%s" % proxy['ip_port']
