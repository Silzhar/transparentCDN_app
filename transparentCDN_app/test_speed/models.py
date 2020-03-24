# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models
import dns.resolver
import speedtest
import socket


class TestSpeed(models.Model):

    urlExternal = 'www.transparentcdn.com'
    hostAddress = socket.gethostbyname(urlExternal)

    speedtester = speedtest.Speedtest(source_address=hostAddress)
    
    server = speedtester.get_best_server()
    downloadSpeed = speedtester.download()
    uploadSpeed = speedtester.upload()

    ouputDates = []
    ouputDates.append(server)
    ouputDates.append(downloadSpeed)
    ouputDates.append(uploadSpeed)

    ouput = str(ouputDates)

    def __str__(self):
        return self.ouput
      #  return self.server , self.totalQuery
