from django.contrib import admin
from django.urls import path
from django.conf.urls import url, include
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf import settings
from accounts import urls
from home import urls
from blog import urls
from .import views

urlpatterns = [
    path('admin/', admin.site.urls),
    url('^home/', include('home.urls', namespace="home")),
    url('^accounts/', include('accounts.urls',namespace="accounts")),
    url('^blog/', include('blog.urls',namespace="blog")),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

urlpatterns += staticfiles_urlpatterns()