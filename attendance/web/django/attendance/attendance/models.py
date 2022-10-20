from django.db import models

class Attendance(models.Model):
    no = models.IntegerField()
    name = models.CharField(max_length=30)
    create_dt = models.DateTimeField()
    update_dt = models.DateTimeField()
