from django.urls import path
from .views import home,about,contact,login,registration,pizzadetail,logout
from django.contrib.auth import views as auth_view 


urlpatterns = [
   path('',home,name='home'),
   path('about/',about,name='about'),
   path('contact/',contact,name='contact'),
   path('login/',auth_view.LoginView.as_view(),name='login'),
   path('logout/',auth_view.LogoutView.as_view(),name='logout'),
   path('registration/',registration,name='registration'),
   path('pizzadetail/<int:pk>/',pizzadetail,name='pizzadetail'),
   
]
