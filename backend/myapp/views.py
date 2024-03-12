from django.db import models
from django.http import HttpResponse
from django.shortcuts import render
from myapp.models import Enquiry  # Change the import statement to import Enquiry

def backend(request):
    if request.method == 'GET':
        return render(request, 'backend.html')
    else:
        name = request.POST.get('name')
        email = request.POST.get('email')
        mobile = request.POST.get('mobile')
        message = request.POST.get('message')
        
        # Create an instance of Enquiry and save it to the database
        enquiry_form = Enquiry.objects.create(name=name, email=email, mobile=mobile, message=message)
        return HttpResponse("Done")
    
