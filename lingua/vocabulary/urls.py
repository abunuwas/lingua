from django.conf.urls import url

from . import views

urlpatterns = [
	url(r'^$', views.index, name='index'),
	url(r'^create/$', views.createTable, name='create'),
	url(r'^(?P<table_id>[0-9]+)/edit/$', views.editTable, name='edit'),
	url(r'^(?P<table_id>[0-9]+)/$', views.viewTable, name='view'),
	]