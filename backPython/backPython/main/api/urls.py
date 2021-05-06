from django.urls import path
from django.conf.urls import url

from .views import RegistrationAPIView, LoginAPIView, UserAPIView, UserReviewAPIView

app_name = 'main'
urlpatterns = [
  path('user/<int:id>/data/', UserAPIView.as_view()),
  url('login/', LoginAPIView.as_view()),
  url('registr/', RegistrationAPIView.as_view()),
  path('user/', UserReviewAPIView.as_view())
]
