#!/usr/bin/env python3
# encoding: utf-8
'''
@author: aseaday
@updated: 2014-11-15
'''

from __future__ import absolute_import, division, print_function, with_statement

from urllib.parse import urlencode
import base64
from hashlib import md5
import time
import json

from tornado.httpclient import AsyncHTTPClient as AClient
from tornado.httpclient import HTTPRequest as Request
from tornado.ioloop import IOLoop

def sig_sum(appkey, stamp, master = None):
    if master is not None:
        raise('I do not know how to deal with master key')
    else:
        return md5((stamp + appkey).encode('utf-8')).hexdigest()

def print_res(res):
    print(res)


class Client(object):
    host = "https://leancloud.cn"
    api_prefix = '/1.1/'
    def __init__(self, *args, **kwargs):
        for  (key, value) in kwargs.items():
            setattr(self, key, value)
        self.client = AClient()
        super(Client, self).__init__()

    def api(self, data, classname = None):
        stamp = str(int(time.time()))
        sig = sig_sum(self.appkey, stamp)
        print(self.appkey)
        headers = {
                'Content-Type' : 'application/json',
                'X-AVOSCloud-Application-Id' : self.appid,
                'X-AVOSCloud-Application-Key' : self.appkey
                }
        url = self.host + self.api_prefix + 'classes/' + classname
        body = json.dumps(data)
        request = Request(url, method = 'POST', headers = headers, body = body)
        self.client.fetch(request, callback = print_res)

if __name__ == '__main__':
    test = Client(appid = 'b62lnfvd5g9bfxv4d300hw5mwo6hs5wttityd2hgnqhom5ko', appkey = 'niae179004ogcjdumj5uep0o5qluy2cjg9kox2swcjnyex9p')
    test.api({'a':1}, 'test')
    IOLoop.instance().start()
