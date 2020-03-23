# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
import speedtest
import dns.resolver


class TestSpeed(models.Model):

    speedtester = dns.resolver.query('transparentcdn.com', 'MX')
    dnsDates = []
    for rdata in speedtester:
        host = rdata.exchange
        server = rdata.preference
        dnsDates.append(host)
        dnsDates.append(server)
        
    def __str__(self):
        ouput = self.dnsDates[0] + ',' + self.dnsDates[1]
        return ouput




"""
    
        speedtester = speedtest.Speedtest()
    server = speedtester.get_best_server()
    totalQuery = speedtester.download()

    def __str__(self):
        return self.server , self.totalQuery

    """



    

