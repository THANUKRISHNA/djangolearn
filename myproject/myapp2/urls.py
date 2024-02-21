from django.urls import path,include

from myapp2 import views


urlpatterns = [
    path('add2/',views.fun1)
]