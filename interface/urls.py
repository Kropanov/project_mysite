from django.conf.urls import url
from . import views


urlpatterns = [
    # Домашная страница
    url(r'^$', views.index, name='index'),
    url(r'^contacts$', views.contacts, name='contacts'),
    url(r'^basket$', views.basket, name='basket'),
]
