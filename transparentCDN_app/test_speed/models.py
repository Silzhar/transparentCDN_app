# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models
# import dns.resolver
import speedtest
# import requests, socket

class TestSpeed(models.Model):

    # urlExternal = requests.get('http://www.transparentcdn.com/')
    # hostAddress = str((urlExternal, '',  socket.SOCK_DGRAM))

    # speedtester = speedtest.Speedtest(source_address=hostAddress)
    speedtester = speedtest.Speedtest()
    

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
