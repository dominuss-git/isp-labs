from django.contrib import admin
from django.urls import path, include
# from main.views import index

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('main.api.urls')),
    path('api/', include('department.api.urls')),
    path('api/', include('employee.api.urls')),
]
