from django.urls import reverse_lazy
from .forms import *
from django.shortcuts import get_object_or_404,render,redirect
from django.views.generic.edit import CreateView,  UpdateView,DeleteView
from django.views.generic import ListView,DetailView


class PersonList(ListView):
    model=Person
    sucess_url=reverse_lazy('list-member')
    context_object_name='member'
    template_name='backend/list_member.html'

   
class PersonView(DetailView):
    model=Person
    queryset=Person.objects.all()
    sucess_url=reverse_lazy('view-member')
    context_object_name='member'
    template_name='backend/view_member.html'
    def view_member(request, member_id):
        current_member = Person.objects.get(is_active=True)
        member_details=Person.objects.filter(pk=member_id)
        context = {
            'member_details': member_details, 'current_member': current_member
        }
        return render(request,'view_member.html', context)

class PersonCreate(CreateView):
    model=Person
    form_class=PersonForm
    success_url=reverse_lazy('create-member')
    context_object_name='member'
    template_name='backend/add_member.html'

class PersonUpdate(UpdateView):
    model=Person
    fields='__all__'
    success_url=reverse_lazy('view-member')
    context_object_name='member'
    template_name='backend/update_member.html'

class PersonDelete(DeleteView):
    model=Person
    success_url=reverse_lazy('delete-member')
    context_object_name='member'
    template_name='backend/delete_member.html'

#  Getting Social Fund Class View
class SocialFundList(ListView):
    model=SocialFund
    sucess_url=reverse_lazy('list-fund')
    context_object_name='fund'
    template_name='backend/list_social_fund.html'

   
class SocialFundView(DetailView):
    model=SocialFund
    queryset=SocialFund.objects.all()
    sucess_url=reverse_lazy('view-fund')
    context_object_name='fund'
    template_name='backend/view_social_fund.html'
    def view_member(request, fund_id):
        current_fund = SocialFund.objects.get(is_active=True)
        fund_details=SocialFund.objects.filter(pk=fund_id)
        context = {
            'fund_details': fund_details, 'current_member': current_fund
        }
        return render(request,'view_social_fund.html', context)

class SocialFundCreate(CreateView):
    model=SocialFund
    form_class=SocialFundForm
    success_url=reverse_lazy('create-fund')
    context_object_name='fund'
    template_name='backend/add_social_fund.html'

class SocialFundUpdate(UpdateView):
    model=SocialFund
    fields='__all__'
    success_url=reverse_lazy('view-fund')
    context_object_name='fund'
    template_name='backend/update_social_fund.html'

class SocialFundDelete(DeleteView):
    model=SocialFund
    success_url=reverse_lazy('delete-fund')
    context_object_name='fund'
    template_name='backend/delete_social_fund.html'


# Getting Saving class based view

class SavingList(ListView):
    model=Saving
    sucess_url=reverse_lazy('savings-list')
    context_object_name='saving'
    template_name='backend/list_saving.html'

   
class SavingView(DetailView):
    model=Saving
    queryset=Saving.objects.all()
    sucess_url=reverse_lazy('view-saving')
    context_object_name='saving'
    template_name='backend/view_saving.html'
    def view_member(request, saving_id):
        current_saving = Saving.objects.get(is_active=True)
        saving_details=Saving.objects.filter(pk=saving_id)
        context = {
            'saving_details': saving_details, 'current_saving': current_saving
        }
        return render(request,'view_saving.html', context)

class SavingCreate(CreateView):
    model=Saving
    form_class=SavingsForm
    success_url=reverse_lazy('create-saving')
    context_object_name='fund'
    template_name='backend/add_saving.html'

class SavingUpdate(UpdateView):
    model=Saving
    fields='__all__'
    success_url=reverse_lazy('view-saving')
    context_object_name='saving'
    template_name='backend/update_saving.html'

class SavingDelete(DeleteView):
    model=Saving
    success_url=reverse_lazy('delete-saving')
    context_object_name='saving'
    template_name='backend/delete_saving.html'

# Getting Loan with Class Based View
class LoanList(ListView):
    model=Loan
    sucess_url=reverse_lazy('loans-list')
    context_object_name='loan'
    template_name='backend/list_loan.html'

   
class LoanView(DetailView):
    model=Loan
    queryset=Loan.objects.all()
    sucess_url=reverse_lazy('view-loan')
    context_object_name='loan'
    template_name='backend/view_loan.html'
    def view_loan(request, loan_id):
        current_laon = Loan.objects.get(pk=loan_id)
        loan_details=Loan.objects.filter(pk=loan_id)
        context = {
            'loan_details': loan_details, 'current_loan': current_laon
        }
        return render(request,'view_loan.html', context)

class LoanCreate(CreateView):
    model=Loan
    form_class=LoanForm
    success_url=reverse_lazy('create-loan')
    context_object_name='loan'
    template_name='backend/add_loan.html'

class LoanUpdate(UpdateView):
    model=Loan
    fields='__all__'
    success_url=reverse_lazy('view-loan')
    context_object_name='loan'
    template_name='backend/update_loan.html'

class LoanDelete(DeleteView):
    model=Loan
    success_url=reverse_lazy('delete-loan')
    context_object_name='loan'
    template_name='backend/delete_loan.html'