from django.conf.urls import url
from django.urls import include, path
from django.contrib import admin

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),
    path('', include('api.urls'))
]