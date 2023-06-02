from django.urls import path,include
from . import views
urlpatterns = [
    path('',views.home,name='home'),
    path('gallery',views.gallery,name='gallery'),
    path('place',views.place,name='place'),
    path('signup',views.signup,name='signup'),
    path('login',views.login,name='login'),
 
]