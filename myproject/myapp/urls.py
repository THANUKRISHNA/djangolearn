from django.urls import path

from myapp import views

urlpatterns = [
    path('add/',views.fun1),
    path('abc/<x>',views.fun2),
    path('xyz',views.thanu.as_view()),
    path('home/', views.home, name='home'),
    path('test/', views.test, name='test'),
]