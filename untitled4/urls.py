"""untitled4 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Import the include() function: from django.conf.urls import url, include
    3. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import url, patterns
from django.contrib import admin
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = patterns('',
    url(r'^admin/', admin.site.urls),
    url(r'^item/(?P<alias>[^/]+)', 'fourapp.views.item'),
    url(r'^$', 'fourapp.views.home'),
    url(r'^order', 'fourapp.views.order'),
    url(r'^(?P<alias>[^/]+)', 'fourapp.views.get_category'),
    #url(r'^zakaz$', 'fourapp.views.zakaz'),

) #+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
