from django.contrib import admin
from django.urls import path, include
# from main.views import index

urlpatterns = [
    path('admin/', admin.site.urls),
    # path('', index),
    path('api/', include('main.api.urls')),

    # path('api/v1/auth', include('djoser.urls')),
    # path('api/v1/auth-token', include('djoser.urls.authtoken'))
]
