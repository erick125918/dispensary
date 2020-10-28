from django.db import models


class Student(models.Model):
    name = models.CharField(max_length=30)
    student_number = models.CharField(max_length=15, primary_key=True)
    age = models.IntegerField()
    gender = models.CharField(max_length=7)
    graduate = models.BooleanField()

    def _str_(self):
       return self.student_number
