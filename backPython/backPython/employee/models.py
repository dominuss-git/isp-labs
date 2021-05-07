from django.db import models

# Create your models here.

from main.models import User
from department.models import Department

from main.models import User

class EmployeeManager(models.Manager):

  def find(self, userId, departmentId):
    employee = self.filter(userId=userId, departmentId=departmentId)
    if not employee:
      return ({"message" : 'Not found'})

    return ({'userId' : employee.values('userId_id')[0].get('userId_id'), \
      'departmentId' : employee.values('departmentId_id')[0].get('departmentId_id') \
    })

  def find_by_user_id(self, userId):
    employees = self.filter(userId=userId)
    employee_out = []
    for val in employees.values_list():
      employee_out.append({
        'id' : val[0],
        'userId' : val[1],
        'departmentId' : val[2]
      })

    return employee_out

  def create_c(self, userId, departmentId):
    if not self.filter(userId=userId).values_list():
      
      user = User.objects.filter(id=userId)

      if not user.values():
        return {'message' : 'User not found'}

      department = Department.objects.filter(id=departmentId)

      if not department.values():
        return {'message' : 'Department not found'}

      employee = Employee(userId=user.first(), departmentId=department.first())
      employee.save()

      return employee

    return {'message': 'User work in another department'}    


  def findAll(self, departmentId):
    employees = self.filter(departmentId=departmentId)
    employee_out = []
    for val in employees.values_list():
      employee_out.append({
        'id' : val[0],
        'userId' : val[1],
        'departmentId' : val[2]
      })

    return employee_out

  def remove(self, userId, departmentId):
    self.filter(userId=userId, departmentId=departmentId).delete()
    return {
      'message' : 'Employee is delete'
    }

  def remove_all(self, departmentId):
    self.filter(departmentId=departmentId).delete()
    return {
      'message' : 'Department is delete'
    }

class Employee(models.Model):
  userId = models.ForeignKey(User, on_delete=models.CASCADE, null=False)
  departmentId = models.ForeignKey(Department, null=False, on_delete=models.CASCADE)
  objects=EmployeeManager()

  def __str__(self):
    return str(self.pk)
