"""A2SL URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
#from django.urls import include, re_path
#from django.contrib.assets.urls import staticfiles_urlpatterns
from . import views
from myapp.views import contactus, user_signup, user_login

urlpatterns = [
    path('admin/', admin.site.urls),
    path('about/',views.about_view,name='about'),
    path('aboutus/',views.aboutus_view,name='aboutus'),
    path('contact/',views.contact_view,name='contact'),
    path('contactus',contactus,name='contactus'),
    path('try1/',views.try1_view,name='try1'),
    path('',views.home_page,name='home'),
    path('login/',views.login_view,name='login'),
    path('logout/',views.logout_view,name='logout'),
    path('signup/',views.signup_view,name='signup'),
    path('animation/',views.animation_view,name='animation'),
    path('header/',views.header_view,name='header'),
    path('footer/',views.footer_view,name='footer'),
    path('register/', views.user_register, name='user_register'),
    path('user_signup',user_signup,name='user_signup'),
    path('user_login',user_login,name='user_login'),
    #re_path(r'^register/$', views.user_register, name='user_register')
    #path('',views.home_view,name='home'),
    #path('animation/',views.animation_view,name='animation')
]
