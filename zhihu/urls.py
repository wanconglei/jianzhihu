from django.conf.urls import url
from . import views


app_name = 'zhihu'
urlpatterns = [
    url(r'^index/', views.index, name='zhihu_index')
]