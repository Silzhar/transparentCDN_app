
from django.conf.urls import url
from django.urls import path

from . import views

urlpatterns = [
    url('' , views.index, name='index'),
 #   url('<int:speed_id>/', views.speedId, name='speedId'),
    # path('<int:speed_id>/result', views.result, name='result'),
    # url('/transparentcdn.com/', views.index)
]