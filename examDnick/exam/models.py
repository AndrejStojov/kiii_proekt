from django.contrib.auth.models import User
from django.db import models
# Create your models here.
class Profesor(models.Model):
    name = models.CharField(max_length=50)
    age = models.IntegerField()
    email = models.EmailField()

    def __str__(self):
        return self.name


class Exam(models.Model):

    SEMESTER_CHOICES = [
        ("W", "Winter"),
        ("S", "Sumer"),
    ]
    name = models.CharField(max_length=50)
    date = models.DateField()
    semester = models.CharField(max_length=3, choices=SEMESTER_CHOICES, null=True, blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    profesors = models.CharField(max_length=100, blank=True, null=True)
    image = models.ImageField(upload_to='')

    def __str__(self):
        return self.name


class ExamProfesor(models.Model):
    exam = models.ForeignKey(Exam, on_delete=models.CASCADE)
    profesor = models.ForeignKey(Profesor, on_delete=models.CASCADE)

    def __str__(self):
        return self.profesor.name+" "+self.exam.name
