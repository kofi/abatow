from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.IndexView.as_view(), name='index'),
    # url(r'^$', views.index, name='index'),
    url(r'^create/$', views.create, name='create'),
    url(r'^(?P<pk>[A-Za-z0-9\-]+)/$', views.DetailView.as_view(), name='detail'),
    url(r'^json/(?P<election_id>[A-Za-z0-9\-]+)/$', views.detail_json, name='detail_json'),
    # url(r'^(?P<election_id>[A-Za-z0-9\-]+)/$', views.detail, name='detail'),
]