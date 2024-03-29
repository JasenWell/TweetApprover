# coding = utf-8
"""TweetApprover URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin

from django.contrib.auth.views import login,logout,LoginView,LogoutView
urlpatterns = [
    url(r'^admin/',admin.site.urls),
    url(r'^$',include(('poster.urls','poster'),namespace='poster')),
    url(r'^post/',include(('poster.urls','poster'),namespace='poster')),
    url(r'^approve/',include(('approver.urls','approver'),namespace='approver')),
    #url(r'^login',login),
    #url(r'^logout',logout),
    url(r'^login',LoginView.as_view(template_name='login.html'),name='login'),

]
