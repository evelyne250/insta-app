from django.conf.urls import url, include
from . import views
from django.conf import settings
from django.conf.urls.static import static
# from django.contrib.auth import views 

urlpatterns=[
    # url('signup/', views.signup, name='signup'),
    url('^$',views.welcome,name = 'welcome'),
    url(r'^accounts/', include('registration.backends.simple.urls')),
    # url(r'^logout/$', views.logout, {"next_page": '/'}),
    url(r'^new/post$', views.new_post, name='new-post'),
    url(r'^profile', views.profile, name='profile')
    # url('^$',views.pictures,name='pictures'),
]
if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
