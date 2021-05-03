from django.db import models
from datetime import datetime, timedelta
from django.conf import settings
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
import jwt

class UserManager(BaseUserManager):
  def create_user(self, email, password):
    if email is None:
      raise TypeError('Email is not valid')

    if len(password) < 6:
      raise TypeError('Password length < 6')

    user = self.model(email=self.normalize_email(email))
    user.set_password(password)
    user.save()

    return user

  def create_superuser(self, email, password):
    if len(password) < 6:
      raise TypeError('Password length < 6')

    user = self.create_user(email, password)
    user.is_staff = True
    user.is_superuser = True

    user.save()

    return user


class User(AbstractBaseUser, PermissionsMixin):
  email = models.EmailField(unique=True, null=False)
  
  is_active = models.BooleanField(default=True)
  is_staff = models.BooleanField(default=False)
  
  date = models.DateTimeField(auto_now_add=True)

  last_update = models.DateTimeField(auto_now=True)

  USERNAME_FIELD = 'email'
  REQUIRED_FIELDS = []

  objects = UserManager()

  def __str__(self):
    return self.email

  @property
  def token(self):
    return self._generate_jwt_token()

  def get_full_name(self):
    return self.email

  def get_short_name(self):
    return self.email

  def _generate_jwt_token(self):
    dt = datetime.now() + timedelta(hours=1)

    token = jwt.encode({
      'id': self.pk,
      'exp': int(dt.strftime('%s'))
    }, settings.SECRET_KEY, algorithm='HS256')

    return token.decode('utf-8')