from django.db import models
from datetime import datetime, timedelta
from django.conf import settings
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
import jwt

class UserManager(BaseUserManager):
  def create_user(self, username, email, password=None):
    if username is None:
      raise TypeError('Users must have a username.')

    if email is None:
      raise TypeError('Users must have an email address.')

    user = self.model(username=username, email=self.normalize_email(email))
    user.set_password(password)
    user.save()

    return user

  def create_superuser(self, username, email, password):
    if password is None:
      raise TypeError('Superusers must have a password.')

    user = self.create_user(username, email, password)
    user.is_superuser = True
    user.is_staff = True
    user.save()

    return user

class User(AbstractBaseUser, PermissionsMixin):
  username = models.CharField(db_index=True, max_length=255, unique=True)
  email = models.EmailField(db_index=True, unique=True)

  is_active = models.BooleanField(default=True)

  is_staff = models.BooleanField(default=False)

  created_at = models.DateTimeField(auto_now_add=True)
  updated_at = models.DateTimeField(auto_now=True)

  USERNAME_FIELD = 'email'
  REQUIRED_FIELDS = ['username']

  objects = UserManager()

  def __str__(self):
    return self.email

  @property
  def token(self):
    return self._generate_jwt_token()

  def get_full_name(self):
    return self.username

  def get_short_name(self):
    return self.username

  def _generate_jwt_token(self):
    dt = datetime.now() + timedelta(days=1)

    token = jwt.encode({
      'id': self.pk,
      'exp': int(dt.strftime('%s'))
    }, settings.SECRET_KEY, algorithm='HS256')

    return token.decode('utf-8')



# from django.contrib.auth.models import BaseUserManager, AbstractBaseUser, PermissionsMixin
# import datetime

# class UserQuerySet(models.QuerySet):

#   def find_by_id(self, id):
#     return self.filter(pk=id)

# class UserManager(models.Manager):#BaseUserManager):
#   def get_queryset(self):
#     return UserQuerySet(self.model, using=self._db)

#   def all(self):
#     return self.get_queryset()

#   def find_by_email(self, email):
#     return self.get_queryset().filter(email=email)

#   # def create_superuser(self, email, password, **extra_fiedls):
#   #   # if (password != confirnPassword):
#   #   #   raise ValueError('Passwords mismatch')

#   #   extra_fiedls.setdefault('is_staff', True)
#   #   extra_fiedls.setdefault('is_superuser', True)
#   #   addr = Address.objects.create(
#   #     street="admin",
#   #     home=1,
#   #     flat=1
#   #   )
#   #   addr.save()

#   #   user = self.model(
#   #     email=email, 
#   #     password=password,
#   #     name="admin",
#   #     surname="admin",
#   #     skils="anything",
#   #     is_staff=True,
#   #     is_superuser=True,
#   #     addressId=addr,
#   #   )
#   #   user.save()

#   #   return user

# class Address(models.Model):

#   street = models.CharField(max_length=254, null=False)
#   home = models.IntegerField(null=False)
#   flat = models.BigIntegerField(null=False)

#   def __str__(self):
#     return self.street



# class User(models.Model):#AbstractBaseUser, PermissionsMixin):

#   is_superuser = models.BooleanField(default=False)
#   is_staff = models.BooleanField(default=False)

#   name = models.CharField(max_length=254, null=False)
#   email = models.EmailField(max_length=70, unique=True, null=False)
#   surname = models.CharField(max_length=254, null=False)
#   skils = models.CharField(max_length=254, blank=True, null=True)
#   password = models.CharField(max_length=254, null=False)
#   date = models.DateField(default=datetime.date.today())
#   addressId = models.ForeignKey(Address, verbose_name="address", on_delete=models.CASCADE)
#   objects = UserManager()

#   USERNAME_FIELD = 'email'
#   REQUIRED_FIELDS = []

#   def __str__(self):
#     return self.name

#   def _generate_jwt_token(self):
#     dt = datetime.now() + datetime.timedelta(hours=1)
#     print("ok")
#     token = jwt.encode({
#       'id': self.pk,
#       'password': self.password
#     }, 'super secret key', algorithm='HS256')

#     return token