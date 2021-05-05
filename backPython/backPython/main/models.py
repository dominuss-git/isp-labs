from django.db import models
from datetime import datetime, timedelta
from django.conf import settings
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
import jwt

class UserQuerySet(models.QuerySet):
  def find_by_id(self, id):
    return self.filter(pk=id)

class Profile(models.Model):
  skils = models.CharField(max_length=254, null=True, blank=True)
  street = models.CharField(max_length=254, null=False)
  home = models.IntegerField(null=False)
  flat = models.IntegerField(null=False)

  def __str__(self):
    return self.street

class UserManager(BaseUserManager):
  def create_user(
    self, 
    email, 
    password,
    name,
    surname,
    home,
    flat,
    street,
    skils
  ):

    addr = Profile(
      street=street,
      home = int(home),
      flat = int(flat)
    )

    addr.save()

    user = self.model(
      email=self.normalize_email(email), 
      name=name,
      surname=surname,
      addresId=addr
    )
    if email is None:
      raise TypeError('Users must have an email address.')

    
    user.set_password(password)
    user.save()

    return {"id": user.pk, "token" : user.token}

  def create_superuser(self, email, password):
    if password is None:
      raise TypeError('Superusers must have a password.')

    user = self.model(
      email=self.normalize_email(email), 
      name="admin",
      surname="admin",
      addresId=None
    )

    user.set_password(password)

    user.is_superuser = True
    user.is_staff = True
    user.save()

    return user

  def get_queryset(self):
    return UserQuerySet(self.model, using=self._db)

  def all(self):
    return self.get_queryset()

  def find_by_id(self, id):
    return self.get_queryset().filter(id=id)


  def find_by_email(self, email):
    return self.get_queryset().filter(email=email)

class User(AbstractBaseUser, PermissionsMixin):
  name = models.CharField(max_length=254, null=False)
  surname = models.CharField(max_length=254, null=False)
  email = models.EmailField(db_index=True, unique=True)
  addresId = models.ForeignKey(
    Profile, 
    null=True, 
    blank=True, 
    verbose_name="address", 
    on_delete=models.CASCADE
  )

  is_active = models.BooleanField(default=True)

  is_staff = models.BooleanField(default=False)

  created_at = models.DateTimeField(auto_now_add=True)
  updated_at = models.DateTimeField(auto_now=True)

  USERNAME_FIELD = 'email'
  # REQUIRED_FIELDS = ['username']

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
    dt = datetime.now() + timedelta(days=1)

    token = jwt.encode({
      'id': self.pk,
      'exp': int(dt.strftime('%s'))
    }, settings.SECRET_KEY, algorithm='HS256')

    return token.decode('utf-8')




# class UserManager(models.Manager):#BaseUserManager):


# class User(models.Model):#AbstractBaseUser, PermissionsMixin):

#   is_superuser = models.BooleanField(default=False)
#   is_staff = models.BooleanField(default=False)
#     return self.name

#   def _generate_jwt_token(self):
#     dt = datetime.now() + datetime.timedelta(hours=1)
#     print("ok")
#     token = jwt.encode({
#       'id': self.pk,
#       'password': self.password
#     }, 'super secret key', algorithm='HS256')

#     return token