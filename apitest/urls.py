from django.conf.urls import url, include
from django.contrib import admin
from albums.api import urls as AlbumsUrl

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^api/', include(AlbumsUrl, namespace="API")),
]
