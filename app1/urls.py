from django.urls import path
from app1.views import *
app_name='Bramhi'
urlpatterns=[
    path('gajala/',gajala,name='gajala'),
]