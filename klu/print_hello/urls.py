from django.urls import path
from . import views

urlpatterns = [
    path('about',views.about, name = 'about'),
    path('',views.login, name='login'),
    path('contact',views.contact, name='contact'),
    path('newuserregister',views.newuserregister, name='newuserregister'),
    path('sucess',views.sucess, name='sucess'),
    path('index',views.index, name='index'),
    path('welcomepage',views.welcomepage, name='welcomepage'),
    path('news',views.news, name ='news'),
    path('Order',views.Order, name= 'Order'),
    path('billing',views.billing, name='billing'),
]


