from django.db import models

class CustomUser(models.Model):
    f_name = models.CharField(max_length = 70)
    l_name = models.CharField(max_length = 100)
    email = models.EmailField()

class Task(models.Model):
    user = models.ForeignKey(CustomUser,on_delete = models.CASCADE)
    title = models.CharField(max_length = 100)
    descripiton = models.TextField()
    create_at = models.DateTimeField(auto_now=False)
    is_active = models.BooleanField(default=False)
