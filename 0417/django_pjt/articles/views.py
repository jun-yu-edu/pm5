from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def articles(request):
    return HttpResponse('서버에서 보낸 정보')