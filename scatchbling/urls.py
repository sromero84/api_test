"""scatchbling URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import include, url
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from tastypie.api import Api
from scratchers.api import ScratcherResource, SizeResource


v1_api = Api(api_name='v1')
v1_api.register(ScratcherResource())
v1_api.register(SizeResource())

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^scratchers/', include('scratchers.urls', namespace='scratchers')),
    url(r'^api/', include(v1_api.urls, namespace='api')),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
