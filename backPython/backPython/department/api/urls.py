from django.urls import path
from django.conf.urls import url

from .views import DepartmentAPIView, DepartmentReviewAPIView, DepartmentCreateAPIView, DepartmentChangeAPIView, RemoveEmployeeAPIView

app_name = 'department'
urlpatterns = [
  # # path('user/<int:id>/data/', UserViewSet.as_view()),
  # url('login/', LoginAPIView.as_view()),
  path('department/<int:id>/change/', DepartmentChangeAPIView.as_view()),
  path('department/<int:id>/', DepartmentAPIView.as_view()),
  path('department/<int:dep>/workers/<int:id>/', RemoveEmployeeAPIView.as_view()),
  path('department/', DepartmentReviewAPIView.as_view()),
  path('department/create/', DepartmentCreateAPIView.as_view()),

  # path('user/<int:id>/data/', UserAPIView.as_view()),
]