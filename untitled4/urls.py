from django.conf.urls import url
from django.contrib import admin
from fourapp import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^item/(?P<alias>[^/]+)', views.item),
    url(r'^$', views.home),
    url(r'^order', views.order),
    url(r'^(?P<alias>[^/]+)', views.get_category),
]

