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
from django.contrib import admin

from apidata.views import *

urlpatterns = [

    url(r'^trans/$', simple, name="simple"),
    url(r'^forecast/$', forecastview, name="apiforecast"),
    url(r'^simple/$', simple, name="apiforecast"),
    url(r'^graph/$', Graph.as_view(), name="Graph"),
    # url(r'^your_url/?$', 'apidata.views.your_view', name='your_url_name'),

]
