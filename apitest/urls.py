from django.conf.urls import url, include
from django.contrib import admin
from albums.api import urls as AlbumsUrl
from django.conf import settings
from django.views.static import serve

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^api/', include(AlbumsUrl, namespace="API")),
    url(
    		r'^media/(?P<path>.*)$',
    		serve, 
    		{'document_root':settings.MEDIA_ROOT}
    ),
]
