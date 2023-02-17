#!/usr/bin/env python3
from django.urls import include, path
from . import views


urlpatterns = [
	path('test/', views.default_view),
]