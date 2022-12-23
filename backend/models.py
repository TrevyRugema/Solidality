from accounts.auth.models import User
from django.db import models
from datetime import datetime, date, timedelta
# from dateutil.relativedelta import *
from dateutil.relativedelta import relativedelta
from django.db.models import Sum
from phonenumber_field.modelfields import PhoneNumberField
from django.utils.translation import gettext_lazy as _
from django.contrib.auth import get_user_model
import uuid
from backend.interest.models import Loan

User=get_user_model()
class Member(User):
    member=models.ForeignKey(User,on_delete=models.CASCADE)
    telephone = PhoneNumberField(null=True,unique=True)
    application_fee = models.IntegerField(default=10000, blank=True, null=True)
    roles = models.CharField(max_length=250, choices=User.Roles,default=User.Roles.MEMBER,unique=False)
    loan=models.ForeignKey(User,on_delete=models.CASCADE)

    
    def __str__(self):
        return str(self.last_name) + ' ' + str(self.first_name)

    class Meta:
        db_table="Sofu Member"

    #decoratiing the Person model with a wtrapper.
   
class SocialFund(models.Model):
    member = models.ForeignKey(Member,on_delete=models.CASCADE)
    date = models.DateField(blank=True, null=True)
    social_fund = models.IntegerField('Social Fund',default=0, blank=True, null=True)
    def __str__(self):
        return str(self.member)

    @property
    def total_social_fund(self):
        members = Member.objects.filter(is_active=True)
        for i in members:
            if (self.first_name != None and self.last_name != None):
                name = (self.first_name + " " + self.last_name)
                startdate = i.period_start
                enddate = i.period_end
                results = SocialFund.objects.filter(date__range=(
                        startdate, enddate), member=name).aggregate(totals=models.Sum("social_fund"))
                if (results['totals']):
                    return results["totals"]
                else:
                    return 0

class Attendance(models.Model):
    STATUS_ATTENDANCE= (('Present', 'Present'), ('Absent', 'Absent'))
    today = datetime.now()
    years=today.year
    months = today.month
    today=today
    member = models.ForeignKey(User,on_delete=models.CASCADE)
    status=models.CharField(max_length=20,choices=STATUS_ATTENDANCE,unique=True,default='Absent')
    attendance_year = models.CharField(max_length=255, blank=True, null=True, default=years)
    attendance_month = models.CharField(max_length=255, blank=True, null=True, default=months)
    attendance_day = models.CharField(max_length=255, blank=True, null=True, default=today)
    def __str__(self):
        return str(self.member)

# class Member(models.Model):
#     member_name =  models.CharField('Member Name', max_length=220, null=True, blank=True, unique=True)
#     rate = models.IntegerField(default=15, null=True, blank=True)
#     member_period_start = models.DateField('Ikibina Period Start',max_length=255, blank=False, null=False, unique=True)
#     member_period_end = models.DateField('Ikibina Period End',max_length=255, blank=False, null=False, unique=True)
#     is_active = models.BooleanField(default=True) 
#     def __str__(self):
#         return str(self.member_period_start.year) + "/" + str(self.member_period_end.year)

class Saving(models.Model):
    date = models.DateField(max_length=100, blank=True, null=True)
    member = models.ForeignKey(
        Member, on_delete=models.CASCADE, max_length=100, null=True, blank=True)
    amount = models.IntegerField(default=0, null=True, blank=True)
    def __str__(self):
        return str(self.member) 

    @property 
    def total_saving(self):
        members = Member.objects.filter(is_active=True)
        for i in members:
            startdate= i.period_start
            enddate= i.period_end
            results=Saving.objects.filter(date__range=(startdate, enddate),name=self.id).aggregate(totals=models.Sum("amount"))
            if (results['totals']):
                return results["totals"]
            else:
                return 0 

        
# class Loan(models.Model):
#     loan_id=models.UUIDField(
#          primary_key = True,
#          default = uuid.uuid4,
#          editable = False)
#     member = models.ForeignKey(Member, on_delete=models.CASCADE,
#                          max_length=100, null=True, blank=True)
#     amount = models.IntegerField(default=0, null=True, blank=True)
#     loan_interest=models.ForeignKey(Loan,on_delete=models.CASCADE,null=True)
#     date = models.DateField(max_length=100, blank=True, null=True)
#     loan_period = models.IntegerField(default=0, null=True, blank=True)
#     verified_by =models.ForeignKey(Member,on_delete=models.CASCADE,related_name='Verified_by',null=True,)
#     authorized_by =models.ForeignKey(Member,on_delete=models.CASCADE,related_name='Authorized_by',null=True,)
#     approved_by =models.ForeignKey(Member,on_delete=models.CASCADE,related_name='Approved_by',null=True,)
    

#     def __str__(self):
#         return str(self.member)

#     @property
#     def total_repayments(self):
#         if PayingLoan.objects.filter(loan_id=self.loan_id).exists():
#             get_loan = PayingLoan.objects.filter(loan_id=self.loan_id)
#             for i in get_loan:
#                 return i.total_paid
#         else:
#             return 0
#     @property
#     def loan_balance(self):
#         if PayingLoan.objects.filter(loan_id=self.loan_id).exists():
#             get_loan = PayingLoan.objects.filter(loan_id=self.loan_id)
#             for i in get_loan:
#                 i.amount - i.amount_paid
#                 return i.balance
#         else:
#             return self.amount
#     @property
#     def loan_status(self):
#         if PayingLoan.objects.filter(loan_id=self.loan_id).exists():
#             get_loan = PayingLoan.objects.filter(loan_id=self.status)
#             for i in get_loan:
#                 return i.loan_status
#         else:
#             return 'RUNNING'

#     @property
#     def deadline(self):
#         end_date = (self.date)+relativedelta(months=+self.loan_period)
#         return end_date
   
#     @property
#     def repayment(self):
#         interest = ((self.loan_interest / 100) * self.loan_period * self.amount)
#         loan_repayment = interest + self.amount
#         return loan_repayment

#     @property
#     def grace_period(self):
#         grace_date = (self.date)+relativedelta(months=+(self.loan_period + 1))
#         return grace_date
    
#     @property
#     def penalties(self):
#         pen_date=date.today()
#         if pen_date >= self.grace_period and self.status == 'RUNNING':
#             # penalted=(self.repay) + (self.interest)
#             # self.amount=penalted
#             # self.save() 
#             return (self.repayment/2)
#         elif pen_date >= self.grace_period and self.status == 'SETTLED':
#             return 'Not Penalized'
#         else:
#             return 'No Penalty Yet'

    # @property
    # def loan_interest(self):
    #     interest = ((self.interest_rate / 100) * self.loan_period * self.amount)
    #     return interest
        
    # @property
    # def maximum_loan_amount(self,user_id):
    #     members = Member.objects.filter(user_id)
    #     for i in members:
    #         startdate = i.period_start
    #         enddate = i.period_end
    #         results = Saving.objects.filter(date__range=(
    #                 startdate, enddate), name=self.id).aggregate(totals=models.Sum("amount"))
    #         if (results['totals']):
    #             x=(results["totals"]*2)
    #             return x
    #         else:
    #             return 0

class PayingLoan(models.Model):
    status = (("RUNNING", "RUNNING"), ("SETTLED", "SETTLED"))
    loan_id = models.ForeignKey(Loan,on_delete=models.CASCADE,null=True)
    date = models.DateField(max_length=100, blank=True, null=True)
    member=models.ForeignKey(Member,on_delete=models.CASCADE)
    amount_paid = models.IntegerField(null=True, blank=True, default=0)
    total_repayment = models.IntegerField(blank=True, default=0)
    # loan_balance = models.ForeignKey(Loan,on_delete=models.CASCADE,related_name='loan balance +')
    loan_status = models.CharField(max_length=100, choices=status, default='RUNNING', null=True, blank=True)
    
    @property
    def total_repayment(self):
        get_all_loans = Loan.objects.all()
        for j in get_all_loans:
            member = User.objects.filter(is_active=True)
            for i in member:
                startdate = i.member_period_start
                enddate = i.member_period_end
            results = PayingLoan.objects.filter(date__range=(
                startdate, enddate), loan_id=j.loan_id).aggregate(totals=models.Sum("total_paid"))
            if (results['totals']):
                x=(results["totals"])
                return x
            else:
                return 0
    def loan_balance(self):
        pass
    def __str__(self):
        return str(self.member)

class Stock(models.Model):
    ticker = models.CharField(max_length=10)
    openn = models.FloatField()
    close = models.FloatField()
    volume = models.IntegerField()
    def __str__(self):
        return str(self.ticker)

class LookUp(models.Model):
    name = models.CharField(unique=True, max_length=220, blank=False, null=False)
    def __str__(self):
        return self.name

class LookupDetail(models.Model):
    Lookup_Name = models.ForeignKey(LookUp, on_delete=models.CASCADE, max_length=220, blank=False, null=False)
    Details = models.CharField(max_length=220, blank=False, null=False)
    def __str__(self):
        return self.Lookup_Name
