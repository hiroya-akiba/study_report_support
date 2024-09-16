from django.db import models
from django.utils import timezone

# Create your models here.
class User(models.Model):
    user_name = models.CharField(max_length=20)
    is_admin = models.BooleanField(default=False)
    create_time = models.DateTimeField(default=timezone.now)

class Subject(models.Model):
    subject_name = models.CharField(max_length=20)
    create_time = models.DateTimeField(default=timezone.now)
    update_time = models.DateTimeField(default=timezone.now)

class Report(models.Model):
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    time = models.IntegerField(default=0) # 勉強時間：分で記録
    create_time = models.DateTimeField(default=timezone.now)
    update_time = models.DateTimeField(default=timezone.now)


