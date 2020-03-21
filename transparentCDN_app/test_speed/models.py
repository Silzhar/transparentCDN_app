# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

import dns.resolver


class TestSpeed(models.Model):

    speedtester = dns.resolver.query('transparentcdn.com', 'MX')
    dnsDates = []
    for rdata in speedtester:
        host = rdata.exchange
        server = rdata.preference
        dnsDates.append(host)
        dnsDates.append(server)
        
    print(dnsDates)



    

