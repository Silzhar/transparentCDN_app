
from django.urls import path
from . import views

urlpatterns =[
    path('www.transparentcdn.com/' , views.index, name='index'),
]