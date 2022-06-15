from django.db import models

from recruit.models import Recruit

# Create your models here.
class User(models.Model):
    name = models.CharField(max_length=15)

    class Meta:
        db_table = 'users'


class ApplyDetail(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    recruit = models.ForeignKey(Recruit, on_delete=models.CASCADE)

    class Meta:
        db_table = 'apply_details'