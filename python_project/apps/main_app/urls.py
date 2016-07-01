from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^trade$', views.trade),
    url(r'^page_not_found$', views.page_not_found),
    url(r'^trade_room$', views.trade_room),
    url(r'^profile$', views.profile),
    url(r'^creator$', views.creator),
    url(r'^login$', views.loginandreg),
    url(r'^process_login$', views.process_login),
    url(r'^process_register$', views.process_register),
]
