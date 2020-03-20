# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
# import speedtest
import dns.resolver

# speedtester = dns.resolver.query('dnspython.org', 'MX')
# for rdata in speedtester:
#     print('Host ', rdata.exchange, 'preference ', rdata.preference)

class TestSpeed(models.Model):

    speedtester = dns.resolver.query('dnspython.org', 'MX')
    for rdata in speedtester:
        print('Host ', rdata.exchange, 'preference ', rdata.preference)


    # speedtester = speedtest.Speedtest()
    # server = speedtester.get_best_server()

    # print(speedtester.download())
    # print(server)
