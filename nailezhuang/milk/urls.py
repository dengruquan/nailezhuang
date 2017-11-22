from django.conf.urls import url
from . import views

app_name="milk"
urlpatterns =[
	url(r'^$', views.index, name='index'),
	url(r'^StasticsReq/', views.StasticsReq, name='StasticsReq'),
	url(r'^StasticsRes/', views.StasticsRes, name='StasticsRes'),
	url(r'^VIPStasticsReq/', views.VIPStasticsReq, name='VIPStasticsReq'),
	url(r'^VIPStasticsRes/', views.VIPStasticsRes, name='VIPStasticsRes'),
]