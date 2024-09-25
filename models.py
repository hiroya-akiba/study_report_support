from django.db import models

# Create your models here.
class User(models.Model):
    user_name = models.CharField(max_length=20)
    is_admin = models.BooleanField(default=False)
    create_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user_name

class Subject(models.Model):
    subject_name = models.CharField(max_length=20)
    create_time = models.DateTimeField(auto_now_add=True)
    update_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.subject_name

class Report(models.Model):
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    time = models.IntegerField(default=0) # 勉強時間：分で記録
    create_time = models.DateTimeField(auto_now_add=True)
    update_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        ret = self.subject.subject_name + '|' + str(self.create_time)
        return ret

