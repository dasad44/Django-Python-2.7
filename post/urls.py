from django.conf.urls import url

from . import views


app_name = 'post'
urlpatterns = [
    url(r'post/$', views.index, name='index'),
    url(r'search/$', views.PostView.as_view(), name='search'),
]