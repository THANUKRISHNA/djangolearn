from django.urls import path
from myapp import views


urlpatterns = [
    path('backend/',views.backend),
    path('dashboard/',views.dashboard),
    path('delete/<rid>',views.delete),
]