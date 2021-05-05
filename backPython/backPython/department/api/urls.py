from django.urls import path
from django.conf.urls import url

from .views import DepartmentAPIView

app_name = 'department'
urlpatterns = [
  # # path('user/<int:id>/data/', UserViewSet.as_view()),
  # url('login/', LoginAPIView.as_view()),
  url('department/', DepartmentAPIView.as_view()),
  # path('user/<int:id>/data/', UserAPIView.as_view()),
]