#!/usr/bin/env python
# -*- config: utf-8 -*-

import base64
import random


class ProxyMiddleware(object):

    def process_request(self, request, spider):
        proxy_ip_port = self.getProxy()
        proxy_user_pass = 'psinc:Hc5iGdS3'
        # Set the location of the proxy
        request.meta['proxy'] = "http://%s" % proxy_ip_port

        basic_auth = 'Basic ' + base64.b64encode(proxy_user_pass.encode()).decode()
        request.headers['Proxy-Authorization'] = basic_auth

    @staticmethod
    def getProxy():
        proxy = ["160.16.238.204:8080", "160.16.235.12:8080", "153.126.173.91:8080", "153.126.173.134:8080",
                 "163.44.169.145:8080", "150.95.157.222:8080", "150.95.143.66:8080", "157.7.140.17:8080",
                 "157.7.196.73:8080", "157.7.140.128:8080"]

        select_proxy = random.randint(0, 9)
        return proxy[select_proxy]
