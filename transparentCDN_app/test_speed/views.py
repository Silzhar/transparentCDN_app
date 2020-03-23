# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import TestSpeed

  
def index(request): 
    showTest = TestSpeed
    return render(request, 'test_speed/index.html', {'test': showTest})

    # template = loader.get_template('test_speed/index.html')
    # indexTemplate = {
    #     'Test speed query : ':showTest}
    # return HttpResponse(template.render(indexTemplate, request))


# def speedId(request):

#     showTest = TestSpeed.speedtester
#     return HttpResponse('Referencia :', showTest)


# def result(request):

#     resultResponse = 'Resultado de la petición : %s.'
#     return HttpResponse(resultResponse  )
