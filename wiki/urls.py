

from django.contrib import admin  
from django.urls import include, path
from user import views  
 
urlpatterns = [  
    path('admin/', admin.site.urls), 
    path('encyclopedia/', include("encyclopedia.urls")), 
    path('',views.home),
    path('signin/',views.signin),
    path('signout/',views.signout),
    path('signup/',views.signup),
    path('profile/',views.profile),
] 