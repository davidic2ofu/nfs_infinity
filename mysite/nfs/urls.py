from django.conf.urls import url
from django.contrib.auth import views as auth_views
from django.conf import settings
from django.conf.urls.static import static

from . import views

app_name = 'nfs'

urlpatterns = [
    url(r'^$', auth_views.login, name='login'),
	
	url(r'^logout/$', auth_views.logout, {'next_page': settings.LOGOUT_REDIRECT_URL}, name='logout'),
	
	url(r'^index/$', views.index, name='index'),
	
	url(r'^upload/$', views.upload, name='upload'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)