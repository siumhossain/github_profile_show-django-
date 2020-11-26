from django.urls import path
from . import views

urlpatterns = [
    path('',views.github,name='home'),
]
