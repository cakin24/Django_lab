from django.conf.urls import url,include
from . import views
urlpatterns = [
    url(r'^histogram/$', views.showHistogram),
    url(r'^linediagram/$', views.showlinediagram),


]