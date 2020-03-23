# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render
from .models import TestSpeed

  
def index(request): 
    showTest = TestSpeed
    return render(request, 'test_speed/index.html', {'test': showTest})
