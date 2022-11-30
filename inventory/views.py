from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from backend.models import *

@login_required(login_url='login')
def dashboard(request):
    total_member = Person.objects.count()
    total_saving = Saving.objects.count()
    total_loan = Loan.objects.count()
    total_fund = SocialFund.objects.count()
    total_active = Attendance.objects.count()
    # loans = Loan.objects.all().order_by('-id')
    context = {
        'member':total_member,
        'saving': total_saving,
        'loan': total_loan,
        'fund': total_fund,
        'attendees': total_active,
        # 'loan': loans
    }
    return render(request, 'dashboard.html', context)