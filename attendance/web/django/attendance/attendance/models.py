from django.db import models

class Attendance(models.Model):
    name = models.CharField(max_length=30)
    create_dt = models.DateTimeField()
