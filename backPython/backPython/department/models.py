from django.db import models

# Create your models here.

from main.models import User

class Department(models.Model):

  name=models.CharField(max_length=254, null=False)
  date=models.DateField(auto_now_add=True)
  update=models.DateField(auto_now=True)
  bossId=models.OneToOneField(User, on_delete=models.CASCADE)
  type=models.CharField(max_length=254, null=False)

  def __str__():
    return self.name