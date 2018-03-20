"""mushrooms URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
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
url(r'^data/(?P<z>\d+)/(?P<x>\d+)/(?P<y>\d+).json$',GeoJSONTile(WeatherStation, geometry_field='geom', trim_to_boundary=True), name='tiled_data')
#url(r'^data.geojson$', GeoJSONLayerView.as_view(model=MushroomSpot, properties=('title', 'description', 'picture_url')), name='data')

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT),
"""
from django.conf import settings
from django.conf.urls import url
from django.conf.urls.static import static
from django.contrib import admin
from django.views.generic import TemplateView
from djgeojson.views import GeoJSONLayerView

from .models import MushroomSpot


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    #url(r'^sdf$', TemplateView.as_view(template_name='index.html'), name='home'),
    url(r'^data.geojson$', GeoJSONLayerView.as_view(model=MushroomSpot), name='data'),
    
] #+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT),