# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models
# import dns.resolver
import speedtest
import socket, threading

class TestSpeed(models.Model):

    urlExternal = 'www.transparentcdn.com'
    hostAddressIP = socket.gethostbyname(urlExternal)
    speedtester = speedtest.Speedtest('', hostAddressIP)
    # speedtester = speedtest.Speedtest()
    

    server = speedtester.get_best_server()
    downloadSpeed = speedtester.download()
    uploadSpeed = speedtester.upload()

    ouputDates = []
    ouputDates.append(server)
    ouputDates.append(downloadSpeed)
    ouputDates.append(uploadSpeed)

    ouput = str(ouputDates)

    def conect(self, socket_client):
      pass


    def __str__(self):
        return self.ouput
      #  return self.server , self.totalQuery
