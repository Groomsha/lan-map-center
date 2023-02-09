from django.urls import path
from pcstatus import views

urlpatterns = [
    path('', views.index, name='index'),
]
