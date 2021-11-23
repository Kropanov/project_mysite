from django.conf.urls import url
from . import views


urlpatterns = [
    # Домашная страница
    url(r'^$', views.index, name='index'),
]
