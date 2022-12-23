from django.db import models

class Saving(models.Model):
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    interest_rate = models.DecimalField(max_digits=5, decimal_places=2)
    num_months = models.PositiveIntegerField()

    def total_saving(self):
        # Calculate the total saving amount
        total_saving = self.amount * (1 + (self.interest_rate / 100))**self.num_months
        return total_saving