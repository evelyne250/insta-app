from django.conf.urls import url, include
from . import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns=[

    url('^$',views.welcome,name = 'welcome'),
    url(r'^accounts/', include('registration.backends.simple.urls')),
    url(r'^new/post$', views.new_post, name='new-post'),
    url(r'^profile', views.profile, name='profile'),
    url(r'^search/', views.search_profile, name='search'),
    url(r'^comment/(\d+)', views.comment_on, name='comment'),
    # url(r'^user_profile/', views.user_profile, name='user_profile'),

]
if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
