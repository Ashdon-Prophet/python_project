from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^faq$', views.faq),
    url(r'^four$', views.four),
    url(r'^contact$', views.contact),
    url(r'^about$', views.about),
    url(r'^blog1$', views.blog1),
    url(r'^blog2$', views.blog2),
    url(r'^blog-post$', views.blog_post),
    url(r'^full-width$', views.full_width),
    url(r'^portfolio1$', views.portfolio1),
    url(r'^portfolio2$', views.portfolio2),
    url(r'^portfolio3$', views.portfolio3),
    url(r'^portfolio4$', views.portfolio4),
    url(r'^portfolio_item$', views.portfolio_item),
    url(r'^pricing$', views.pricing),
    url(r'^services$', views.services),
    url(r'^sidebar$', views.sidebar),
]
