"""tenmins URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from website.views import listing, index_login, index_register, detail, detail_vote
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth.views import logout

from website.mobile_views import video_list
from website.api import video, video_card
from rest_framework.authtoken import views


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^list/$', listing, name='list'),
    url(r'^list/(?P<cate>[A-Za-z]+)$', listing, name='list'),
    url(r'^detail/(?P<id>\d+)$', detail, name='detail'),
    url(r'^detail/vote/(?P<id>\d+)$', detail_vote, name='vote'),
    url(r'^login/$', index_login, name='login'),
    url(r'^register/$', index_register, name='register'),
    url(r'^logout/$', logout, {'next_page': '/register'}, name='logout'),



    url(r'^api/videos/$', video),
    url(r'^api/videos/(?P<id>\d+)$', video_card),
    url(r'^api/token-auth$', views.obtain_auth_token),

    url(r'^m/videolist/', video_list),


]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
