
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
from django.db.models import Sum

User=get_user_model()
#table for Persons of the sacco.
class Person(models.Model):
    is_active = models.BooleanField(default=True)   # can login
    roles = (('Admin', 'Admin'), ('Ordinary', 'Ordinary'))
    atte = (('Present', 'Present'), ('Absent', 'Absent'))
    joining_date =models.DateTimeField(default=datetime.now, blank=True,null=True)
    status = models.CharField(max_length=30,choices=atte,default='Absent', blank=True, null=True)
    email = models.EmailField(max_length=255, blank=True, null=True)
    telephone = PhoneNumberField(null=True,unique=True)
    first_name = models.CharField(max_length=30, blank=True, null=True)
    last_name = models.CharField(max_length=255, blank=True, null=True)
    username = models.CharField(max_length=30, unique=True, blank=True, null=True)
    application_fee = models.IntegerField(default=10000, blank=True, null=True)
    Role = models.CharField(max_length=250, choices=roles)
    
    def __str__(self):
        return str(self.last_name) + ' ' + str(self.first_name)

    class Meta:
        db_table="Sofu Member"

    #decoratiing the Person model with a wtrapper.
   
    @property
    def maximum_loan_amount(self):
        member = User.objects.filter(member.pk)
        for i in member:
            startdate = i.period_start
            enddate = i.period_end
            results = Saving.objects.filter(date__range=(
                    startdate, enddate), name=self.id).aggregate(totals=models.Sum("amount"))
            if (results['totals']):
                x=(results["totals"]*2)
                return x
            else:
                return 0

    @property
    def loan_status(self):
        get_loans=Loan.objects.all()
        for i in get_loans:
            filtering=PayingLoan.objects.filter(loan_id=i.id, name=self.member)
            for j in filtering:
                if j.loan_status == 'SETTLED':
                    return 'No Running Loan'
                else:
                    return 'Running Loan'   
        return j.loan_status        
                


class SocialFund(models.Model):
    member = models.ForeignKey(Person,on_delete=models.CASCADE)
    date = models.DateField(blank=True, null=True)
    social_fund = models.IntegerField('Social Fund',default=0, blank=True, null=True)
    def __str__(self):
        return str(self.member)

    @property
    def total_social_fund(self):
        person = Person.objects.filter(is_active=True)
        for i in person:
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

class Member(models.Model):
    member_name =  models.CharField('Member Name', max_length=220, null=True, blank=True, unique=True)
    rate = models.IntegerField(default=15, null=True, blank=True)
    member_period_start = models.DateField('Ikibina Period Start',max_length=255, blank=False, null=False, unique=True)
    member_period_end = models.DateField('Ikibina Period End',max_length=255, blank=False, null=False, unique=True)
    is_active = models.BooleanField(default=True) 
    def __str__(self):
        return str(self.member_period_start.year) + "/" + str(self.member_period_end.year)

class Saving(models.Model):
    date = models.DateField(max_length=100, blank=True, null=True)
    member = models.ForeignKey(
        Person, on_delete=models.CASCADE, max_length=100, null=True, blank=True)
    amount = models.IntegerField(default=0, null=True, blank=True)
    def __str__(self):
        return str(self.member) 

    @property 
    def total_saving(self):
        person = Person.objects.filter(is_active=True)
        for i in person:
            startdate= i.period_start
            enddate= i.period_end
            results=Saving.objects.filter(date__range=(startdate, enddate),name=self.id).aggregate(totals=models.Sum("amount"))
            if (results['totals']):
                return results["totals"]
            else:
                return 0 

        
class Loan(models.Model):
    class LoanTypes(models.TextChoices):
        ORIDINARY_LOAN='ORIDINARY_LOAN','Oridinary-Loan',
        EMERGENCY_LOAN='EMERGENCY_LOAN','Emergency-Loan',
    status = (("RUNNING", "RUNNING"), ("SETTLED", "SETTLED"))
    date = models.DateField(max_length=100, blank=True, null=True)
    member = models.ForeignKey(Person, on_delete=models.CASCADE,
                         max_length=100, null=True, blank=True)
    loan_types=models.CharField(_('Loan Types'),max_length=80,choices=LoanTypes.choices, default=LoanTypes.EMERGENCY_LOAN,serialize=True)
    amount = models.IntegerField(default=0, null=True, blank=True)
    interest_rate = models.IntegerField(default=0)
    loan_period = models.IntegerField(default=0, null=True, blank=True)
    loan_status = models.CharField(max_length=100,choices=status, default='RUNNING', null=True, blank=True)
    loan_id=models.UUIDField(
         primary_key = True,
         default = uuid.uuid4,
         editable = False)
    recorded_by =models.ForeignKey(User,on_delete=models.CASCADE)
    
    def __str__(self):
        return str(self.member)

    @property
    def total_repayments(self):
        if PayingLoan.objects.filter(loan_id=self.loan_id).exists():
            get_loan = PayingLoan.objects.filter(loan_id=self.loan_id)
            for i in get_loan:
                return i.total_paid
        else:
            return 0
    @property
    def balance(self):
        if PayingLoan.objects.filter(loan_id=self.loan_id).exists():
            get_loan = PayingLoan.objects.filter(loan_id=self.loan_id)
            for i in get_loan:
                i.loan_balance - i.amount_paid
                return i.balance
        else:
            return self.amount
    @property
    def status(self):
        if PayingLoan.objects.filter(loan_id=self.loan_id).exists():
            get_loan = PayingLoan.objects.filter(loan_id=self.status)
            for i in get_loan:
                return i.loan_status
        else:
            return 'RUNNING'

    @property
    def deadline(self):
        end_date = (self.date)+relativedelta(months=+self.loan_period)
        return end_date
   
    @property
    def repayment(self):
        interest = ((self.interest_rate / 100) * self.loan_period * self.amount)
        loan_repayment = interest + self.amount
        return loan_repayment

    @property
    def grace_period(self):
        grace_date = (self.date)+relativedelta(months=+(self.loan_period + 1))
        return grace_date
    
    @property
    def penalties(self):
        pen_date=date.today()
        if pen_date >= self.grace_period and self.status == 'RUNNING':
            # penalted=(self.repay) + (self.interest)
            # self.amount=penalted
            # self.save() 
            return (self.repayment/2)
        elif pen_date >= self.grace_period and self.status == 'SETTLED':
            return 'Not Penalized'
        else:
            return 'No Penalty Yet'

    @property
    def loan_interest(self):
        interest = ((self.interest_rate / 100) * self.loan_period * self.amount)
        return interest
        
class PayingLoan(models.Model):
    status = (("RUNNING", "RUNNING"), ("SETTLED", "SETTLED"))
    loan_id = models.ForeignKey(Loan,on_delete=models.CASCADE,null=True)
    date = models.DateField(max_length=100, blank=True, null=True)
    member=models.ForeignKey(Person,on_delete=models.CASCADE)
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
