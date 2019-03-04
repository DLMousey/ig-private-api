from django.conf.urls import url
from django.urls import include, path
from django.contrib import admin
from rest_framework_jwt.views import obtain_jwt_token, refresh_jwt_token

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^auth/', obtain_jwt_token),
    url(r'^auth/refresh/', refresh_jwt_token),
    path('api-auth/', include('rest_framework.urls')),
    path('', include('api.urls'))
]