# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

from django.http import HttpResponse
from django.template import loader

from .models import TestSpeed


    
def index(request): 
    showTest = TestSpeed
    ouput = ', ', showTest

    template = loader.get_template('test/index.html')
    indexTemplate = {
        'Test speed query : ':ouput,
    }
    return HttpResponse(template.render(indexTemplate, request))
  #  return HttpResponse("index transparent cdn" )


# def speedId(request):

#     showTest = TestSpeed.speedtester
#     return HttpResponse('Referencia :', showTest)


# def result(request):

#     resultResponse = 'Resultado de la petición : %s.'
#     return HttpResponse(resultResponse  )
