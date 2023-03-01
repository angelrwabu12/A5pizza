from django.urls import path
from .views import home,about,contact,login,registration,pizzadetail


urlpatterns = [
   path('',home,name='home'),
   path('about/',about,name='about'),
   path('contact/',contact,name='contact'),
   path('login/',login,name='login'),
   path('registration/',registration,name='registration'),
   path('pizzadetail/<int:pk>/',pizzadetail,name='pizzadetail'),
   
]
