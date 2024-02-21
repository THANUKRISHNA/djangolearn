from django.shortcuts import render
from django.http import HttpResponse
from django.views import View

def fun1(request):
    return HttpResponse('hii')
def fun2(request,x):
    return HttpResponse("welcome"+x)
class thanu(View):
    def get(self,request):
        return HttpResponse("no")    
def home(request):
    return render(request,'index.html')
