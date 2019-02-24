from django.http.response import HttpResponse
from django.shortcuts import render


# Create your views here.
def testview(request):
    print("11")
    return HttpResponse('这是测试')
