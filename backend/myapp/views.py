from django.db import models
from django.http import HttpResponse
from django.shortcuts import redirect,render
from myapp.models import Enquiry  

def backend(request):
    if request.method == 'GET':
        return render(request, 'backend.html')
    else:
        name = request.POST.get('name')
        email = request.POST.get('email')
        mobile = request.POST.get('mobile')
        message = request.POST.get('message')
        a=Enquiry.objects.create(name=name, email=email, mobile=mobile, message=message) #orm for select
        a.save()
        return redirect('/dashboard')
    
def dashboard(request):
    a=Enquiry.objects.all()   #orm for select
    print(a)
    b={}
    b['data']=a
    return render(request,"dashboard.html",b)

def delete(request,rid):
    a=Enquiry.objects.filter(id=rid) #orm for delete
    a.delete()
    return redirect('/dashboard')