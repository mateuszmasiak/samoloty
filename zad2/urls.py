from django.conf.urls import url
from django.urls import path
from django.contrib.auth import views as auth_views

from . import views

urlpatterns = [
    url(r'^$', views.HomePageView.as_view()),
    #url(r'^planelist/$', views.Flightlist.as_view()),
    url(r'^login/$', auth_views.login, name='login'),
    url(r'^logout/$', views.Loggout.as_view(), name='logout'),
    url(r'^flightlist/$', views.Flightlist.as_view()),
    url(r'^flightlist/(?P<fid>\d+)/$', views.Flightview.as_view()),
    url(r'^planecrew/$', views.planecrew_list),
    url(r'^planecrew/(?P<fid>\d+)/(?P<slug>\w+)/(?P<str1>\w+)/$', views.planecrew_el),
    url(r'^planecrew/json/$', views.planecrew_list_json),
    #url(r'^login/$', auth_views.login, name='login'),
    #url(r'^logout/$', auth_views.logout, name='logout'),
]
