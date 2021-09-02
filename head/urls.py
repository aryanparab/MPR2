from django.urls import path

from .views import homeView,startquizView

app_name = 'head'

urlpatterns=[
path("",homeView,name='head-home'),
path("startquiz/",startquizView,name='head-startquiz'),
]