from django.conf.urls import url, include
from . import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns=[

    url('^$',views.welcome,name = 'welcome'),
    url(r'^accounts/', include('registration.backends.simple.urls')),
    url(r'^new/post$', views.new_post, name='new-post'),
    url(r'^profile', views.profile, name='profile'),

]
if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
