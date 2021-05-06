from django.db import models
import datetime

# Create your models here.

from main.models import User
# from employee.models import Employee

class DepartmentManager(models.Manager):
  def find_by_id(self, id):
    department = self.filter(id=id)
    if not department:
      return ({"message" : 'Not found'})

    return ({
      'name' : department.values()[0].get('name'),
      'type' : department.values()[0].get('type'),
      'id' : department.values()[0].get('id'),
      'bossId' : department.values()[0].get('bossId_id'),
      'date' : department.values()[0].get('date'),
      'update' : department.values()[0].get('update')
    })

  def find_all(self):
    departments = self.filter()
    department_out = []
    for val in departments.values_list():
      department_out.append({
        'name' : val[1],
        'type' : val[5],
        'id' : val[0],
        'bossId' : val[4],
        'date' : val[2],
        'update' : val[3]
      })
# 
    return department_out

  def create_c(self, name, type, bossId):
    boss = User.objects.find_by_id(bossId)
    
    if not boss.values():
      return {'message' : 'Boss not found'}

    return Department(name=name, type=type, bossId=boss.first())

  def change_boss(self, id, bossId):
    boss = User.objects.filter(id=bossId)

    return self.filter(id=id).update(id=id, bossId=boss.first())

  def last_update(self, id):
    return self.filter(id=id).update(update=datetime.date.today())

class Department(models.Model):

  name=models.CharField(max_length=254, null=False)
  date=models.DateField(auto_now_add=True)
  update=models.DateField(auto_now=True)
  bossId=models.OneToOneField(User, on_delete=models.CASCADE)
  type=models.CharField(max_length=254, null=False)
  objects=DepartmentManager()

  def __str__(self):
    return self.name