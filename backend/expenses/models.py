from django.db import models


class Expenses(models.Model):
    name_of_expense=models.CharField(max_length=255,blank=False,null=True)
    reason_for_expense=models.TextField()
    