from django.conf.urls import url, include
from . import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns=[

    url('^$',views.welcome,name = 'welcome'),
    url(r'^accounts/', include('registration.backends.simple.urls')),
    url(r'^new/post$', views.new_post, name='new-post'),
    url(r'^profile', views.profile, name='profile'),
    url(r'^search/', views.search_results, name='search_results'),
    url(r'^comment/(\d+)', views.add_comment, name='comment'),
    url(r'^edit/profile', views.profile_edit, name='profile_edit'),
    # url(r'^unfollow/<to_unfollow>', views.unfollow, name='unfollow'),
    # url(r'^follow/<to_follow>', views.follow, name='follow'),
    # url(r'^likes/', views.likes, name="likes")
]

if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
