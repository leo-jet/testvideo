from django.conf.urls import include, url
from django.contrib import admin

from django.conf.urls import include, url
from django.contrib import admin
from chat import chat_url
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    url(r'^chat/', include(chat_url)),
    url(r'^admin/', include(admin.site.urls)),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)