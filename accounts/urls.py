"""sms URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
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
from django.conf.urls import url, include
from django.contrib.auth import views as auth_views
from accounts.views import *
#signup, activate, account_activation_sent, home, subscriberView, home1,user_login
from django.conf.urls import url, include
from django.contrib import admin  # THIS LINE

admin.autodiscover()

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^signup/$', signup, name='signup'),
    url(r'^home/$', home, name='home'),
    url(r'^homezz/$', homezz, name='homezz'),
    url(r'^login/$', user_login, name='login'),
    url(r'^logout/$', auth_views.logout, {'next_page': 'login'}, name='logout'),
    url(r'^login/home1/$', home1, name='home1'),
    url(r'^login/home2/$', home2, name='home2'),
    url(r'^account_activation_sent/$', account_activation_sent, name='account_activation_sent'),
    url(r'^login/subscriberView/$', subscriberView, name='subscriberView'),
    url(r'^newsubscView',newsubscView,name='newsubscView'),
    url(r'^reCommCrop',reCommCrop,name='reCommCrop'),
    url(r'^activate/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$', activate,
        name='activate'),
    url(r'^created/$', created, name='created'),


]
