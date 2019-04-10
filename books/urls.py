from django.conf.urls import url
from .import views

urlpatterns = [
    url(r'^$',views.index, name='index'),
    url(r'^(?P<book_id>[0-9]+)/$',views.detail, name='detail'),
    url(r'^cat/(?P<cat_id>[0-9]+)/$',views.cat_detail, name='cat_detail'),
    url(r'^search/',views.search_bar, name='search_bar'),
    
]
