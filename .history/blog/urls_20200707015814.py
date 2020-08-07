from django.conf import settings
from django.conf.urls import include, url
from django.urls import re_path, path
from django.conf.urls.static import static
from django.contrib import admin


from rest_framework_jwt.views import obtain_jwt_token

from accounts.views import (login_view, register_view, logout_view)

urlpatterns = [
        # re_path(r'^admin/', admin.site.urls),
    
    path('admin/', admin.site.urls),
    path('comments/', include("comments.urls",)),
    path('register/', register_view, name='register'),
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
    path('', include("posts.urls", )),
    path('api/auth/token/', obtain_jwt_token),
    path('api/users/', include("accounts.api.urls",)),
    path('api/comments/', include("comments.api.urls", )),
    path('api/posts/', include("posts.api.urls",)),
    #url(r'^posts/$', "<appname>.views.<function_name>"),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)