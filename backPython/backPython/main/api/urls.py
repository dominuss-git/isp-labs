from django.urls import path
from django.conf.urls import url

from .views import RegistrationAPIView, LoginAPIView, UserRetrieveUpdateAPIView

app_name = 'main'
urlpatterns = [
  # path('user/<int:id>/data/', UserViewSet.as_view()),
  url('login/', LoginAPIView.as_view()),
  url('registr/', RegistrationAPIView.as_view()),
  url('user', UserRetrieveUpdateAPIView.as_view()),
]
