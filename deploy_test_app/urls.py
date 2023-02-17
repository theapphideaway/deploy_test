#!/usr/bin/env python3
from django.urls import include, path
from . import views


urlpatterns = [
	path('', views.default_view, name='default_view'),
]