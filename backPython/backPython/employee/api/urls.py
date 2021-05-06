from django.urls import path
from django.conf.urls import url

from .views import EmployeeAPIView, EmployeeDataAPIView

app_name = 'employee'
urlpatterns = [
  # # path('user/<int:id>/data/', UserViewSet.as_view()),
  path('employee/<int:id>/', EmployeeDataAPIView.as_view()),
  url('employee/', EmployeeAPIView.as_view()),
  # url('department/', DepartmentAPIView.as_view()),
  # path('user/<int:id>/data/', UserAPIView.as_view()),
]