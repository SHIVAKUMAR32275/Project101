from django.db import models

# Create your models here.
class student(models.Model):
    name=models.CharField(max_length=12)
    age=models.IntegerField()
    is_going_school=models.BooleanField(default=True)




    





