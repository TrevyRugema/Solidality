from django.contrib import admin
from django.contrib.contenttypes.models import ContentType
from django.http import HttpResponseRedirect
from .forms import*
from .models import *

admin.site.site_title='Solidaltiy Fund'
admin.site.site_header='Solidaltiy-Dashboard '

@admin.register(Person)
class MemberAdmin(admin.ModelAdmin):
    list_display=('id','first_name','last_name','Role','joining_date','status','telephone','email','application_fee')   
@admin.register(Loan)
class LoanAdmin(admin.ModelAdmin):
    list_display = ['id','loan_id', 'loan_status', 'member','amount','status']
@admin.register(Saving)
class SavingAdmin(admin.ModelAdmin):
    list_display = ['id','member', 'date', 'amount',]
@admin.register(PayingLoan)
class PayingLoanAdmin(admin.ModelAdmin):
    list_display=['loan_id','amount_paid','member','total_repayment','loan_balance','date']
@admin.register(Attendance)
class AttendanceAdmin(admin.ModelAdmin):
    list_display=['id','member','status']
