from django.http.response import HttpResponse


# Create your views here.
def testview(request):
    print("1122")
    return HttpResponse('这是测试')
