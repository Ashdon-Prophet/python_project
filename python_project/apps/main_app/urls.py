from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^faq$', views.faq),
    url(r'^blog$', views.blog),
    url(r'^contact$', views.contact),
]
