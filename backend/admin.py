from django.contrib import admin
from django.contrib.contenttypes.models import ContentType
from django.http import HttpResponseRedirect
from .forms import*
from .models import *
from backend.interest.models import models

admin.site.site_title='Solidaltiy Fund'
admin.site.site_header='Solidaltiy-Dashboard '

# @admin.register(Person)
# class MemberAdmin(admin.ModelAdmin):
#     list_display=('id','Role','joining_date','attendance_status','telephone','email','application_fee')   
@admin.register(Loan)
class LoanAdmin(admin.ModelAdmin):
    list_display = ['loan_id', 'member','amount','loan_interest','total_repayments','loan_balance','deadline','grace_period','penalties','loan_status']
    
@admin.register(Saving)
class SavingAdmin(admin.ModelAdmin):
    list_display = ['id','member', 'date', 'amount','total_saving']
@admin.register(PayingLoan)
class PayingLoanAdmin(admin.ModelAdmin):
    list_display=['loan_id','amount_paid','member','total_repayment','loan_balance','date']
@admin.register(Attendance)
class AttendanceAdmin(admin.ModelAdmin):
    list_display=['id','member','status']

@admin.register(SocialFund)
class SocialFundAdmin(admin.ModelAdmin):
    list_display=['member','social_fund','date','total_social_fund']
