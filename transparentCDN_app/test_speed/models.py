# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

import dns.resolver


class TestSpeed(models.Model):

    speedtester = dns.resolver.query('transparentcdn.com', 'MX')
    for rdata in speedtester:
        print('Host ', rdata.exchange, 'preference ', rdata.preference)
    
    def __str__(self):
        return self.rdata.exchange , self.rdata.preference
    

