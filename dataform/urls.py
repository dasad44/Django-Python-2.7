from django.conf.urls import url

from . import views


app_name = 'dataform'
urlpatterns = [
    url(r'data/$', views.post, name='data'),
]