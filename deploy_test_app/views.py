from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def default_view(request):
	return HttpResponse("Hello, world, you're at the index. Thanks for stopping by!")