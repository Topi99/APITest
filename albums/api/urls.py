from django.conf.urls import url
from . import views

urlpatterns = [
	url(r'^albums/$', views.AlbumListView.as_view(), name="albums_list"),
	url(r'^albums/(?P<pk>\d+)/$', views.AlbumDetailView.as_view(), name="album_detail"),
]