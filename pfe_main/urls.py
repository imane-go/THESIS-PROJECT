from django.contrib import admin
from django.urls import path

from django.urls import path, include

urlpatterns = [
    path('', include('main_app.urls')),
    path('admin/', admin.site.urls),
    path('api/auth/', include('dj_rest_auth.urls')),
    path('api/auth/registration/', include('dj_rest_auth.registration.urls'))
]
