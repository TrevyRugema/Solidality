from django.db import models
from dateutil.relativedelta import relativedelta
from accounts.auth.models import User
import uuid
from accounts.auth.models import User

class Loan(models.Model):
    LOAN_TYPE_CHOICES = (
        ('ordinary', 'Ordinary'),
        ('emergency', 'Emergency'),
    )

    STATUS_CHOICES = (
        ('active', 'Active'),
        ('closed', 'Closed'),
        ('default', 'Default'),
    )
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='active')
    loan_id=models.UUIDField(
         primary_key = True,
         default = uuid.uuid4,
         editable = False)
    loan_type = models.CharField(max_length=10, choices=LOAN_TYPE_CHOICES)
    principal = models.DecimalField(max_digits=10, decimal_places=2)
    num_payments = models.PositiveIntegerField()
    member=models.ForeignKey(User,on_delete=models.CASCADE)
    application_date = models.DateField()
    verified_by =models.ForeignKey(User,on_delete=models.CASCADE,related_name='Verified_by',null=True,)
    authorized_by =models.ForeignKey(User,on_delete=models.CASCADE,related_name='Authorized_by',null=True,)
    approved_by =models.ForeignKey(User,on_delete=models.CASCADE,related_name='Approved_by',null=True,)

    def monthly_payment(self):
        # Set the interest rate based on the loan type
        if self.loan_type == 'ordinary':
            interest_rate = 0.05
        elif self.loan_type == 'emergency':
            interest_rate = 0.1
        else:
            interest_rate = 0

        # Calculate the monthly interest rate
        monthly_interest_rate = interest_rate / 12
        # Calculate the monthly payment
        monthly_payment = (self.principal * monthly_interest_rate) / (1 - (1 + monthly_interest_rate)**(-self.num_payments))
        return monthly_payment

    def remaining_balance(self, num_payments_made):
        # Calculate the remaining balance on the loan
        remaining_balance = self.principal * ((1 + (self.interest_rate / 12))**(self.num_payments - num_payments_made) - 1) / (self.interest_rate / 12)
        return remaining_balance

    def total_amount_due(self):
        # Calculate the total amount due on the loan
        total_amount_due = self.principal + (self.monthly_payment() * self.num_payments)
        return total_amount_due

    def update_status(self, total_payments_made):
        # Calculate the unpaid amount
        unpaid_amount = self.total_amount_due() - total_payments_made
        # Update the status based on the unpaid amount
        if unpaid_amount == 0:
            self.status = 'closed'
        elif unpaid_amount < 0:
            self.status = 'default'
        else:
            self.status = 'active'
        self.save()

    def deadline(self):
        # Calculate the deadline for the loan
        deadline = self.application_date + relativedelta(months=self.num_payments)
        return deadline

    def grace_period_end(self):
        # Calculate the end date for the grace period
        grace_period_end = self.deadline() + relativedelta(days=self.grace_period)
        return grace_period_end

    def penalties(self, total_payments_made):
        # Calculate the unpaid amount
        unpaid_amount = self.total_amount_due() - total_payments_made
        # Calculate the penalties based on the unpaid amount and the terms of the loan
        penalties = unpaid_amount * 0.1
        return penalties