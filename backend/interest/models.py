from django.db import models
from backend.models import *

class Interest(Loan):
    oridinary=models.IntegerField(primary_key=True,editable=False,blank=False,default=5)
    emergency=models.IntegerField(primary_key=True,editable=False,blank=False,default=10)

    @property

    def loan_interest(self):
        user=User.objects.all()
        if Loan.amount==self.oridinary:
            oridinary_loan_interest= Loan.amount*5/100
            return oridinary_loan_interest
        if Loan.amount==self.emergency:
            emergency_loan_interest=Loan.amount*10/100
            return emergency_loan_interest
            
        user.save()

        return super().loan_interest
