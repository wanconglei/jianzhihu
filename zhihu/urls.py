from django.conf.urls import url
from . import views


app_name = 'zhihu'
urlpatterns = [
    url(r'^index/', views.zhihu_index, name='zhihu_index'),
    url(r'^issue/(?P<pk>[0-9]+)/$', views.detail, name='detail')
]
