from django.urls import path, include
from rest_framework import routers
from . import api_views

urlpatterns = [
	path('/todo_api_home', api_views.Lists.as_view(), name='todo_api_home'),
	path('/add_item', api_views.Lists.as_view(), name='add_item'),
]