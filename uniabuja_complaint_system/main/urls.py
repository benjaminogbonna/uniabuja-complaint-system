from django.urls import path
from .views import index, lodge_complain

app_name = 'main'

urlpatterns = [
    path('', index, name='index'),
    path('lodge-complain', lodge_complain, name='lodge_complain'),
]
