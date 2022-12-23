
from django import forms
from backend.models import *
from django.forms import Textarea, TextInput, ChoiceField
# from bootstrap_datepicker_plus import DatePickerInput, TimePickerInput, MonthPickerInput


class MembershipAccountForm(forms.ModelForm):
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput(
        attrs={'placeholder': 'Password'}))
    password2 = forms.CharField(label='Password confirmation',
                                widget=forms.PasswordInput(attrs={'placeholder': 'Confirm Password'}))

    class Meta:
        model = User
        fields = [ 'username', 'email']
        # 'roles'
        labels = {
            'username': 'Username',
        }
    def clean_password2(self):
        # Check that the two password entries match
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("Passwords don't match")
        return password2

    def save(self, commit=True):
        # Save the provided password in hashed format
        user = super(MembershipAccountForm, self).save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        if commit:
            user.save()
        return user

class MemberForm(forms.ModelForm):
    query_set=Member.objects.all()
    class Meta:
        model=Member
        fields = ('telephone',
                  'application_fee','roles','member','loan')


class SocialFundForm(forms.ModelForm):
    class Meta:
        model = SocialFund
        fields = ('member','social_fund', 'date')
        widgets={
            'date': forms.DateInput(
                format=('%Y-%m-%d'),
                attrs={'class': 'form-control', 
                    'placeholder': 'Select a date',
                    'type': 'date'
                    })
        }

# class MembersForm(forms.ModelForm):
#     class Meta:
#         model=Member
#         fields=('member_name','member_period_start','member_period_end','rate','is_active')


# class EditMemberForm(forms.ModelForm):
#     class Meta:
#         model = Member
#         fields = ('member_name', 'member_period_start',
#                   'member_period_end', 'rate')
#         widgets = {
#             'date': TextInput(attrs={'placeholder': 'Date(YYY-MM-DD)'})
#         }
class AttendanceForm(forms.ModelForm):
    class Meta:
        model=Attendance
        fields=('member','status')
        status = forms.MultipleChoiceField(widget=forms.CheckboxSelectMultiple)

class SavingsForm(forms.ModelForm):
    class Meta:
        model=Saving
        fields=('member','date','amount')
        widgets={
            'date': forms.DateInput(
                format=('%Y-%m-%d'),
                attrs={'class': 'form-control', 
                    'placeholder': 'Select a date',
                    'type': 'date'
                    })
        }

class LoanForm(forms.ModelForm):
    class Meta:
        model=Loan
        fields = ('member', 'date', 'amount', 'loan_interest',
                  'loan_period','verified_by','authorized_by','approved_by')

        widgets={
            'date': forms.DateInput(
                format=('%Y-%m-%d'),
                attrs={'class': 'form-control', 
                    'placeholder': 'Select a date',
                    'type': 'date'
                    })
        }
                  
class PayingLoanForm(forms.ModelForm):
    class Meta:
        model=PayingLoan
        fields = ('loan_id', 'member', 'date', 'amount_paid')

class EditLoanForm(forms.ModelForm):
    class Meta:
        model=Loan
        fields = ('member', 'date', 'amount', 'loan_interest',
                  'loan_period', 'verified_by','authorized_by','approved_by')
        labels = {
            'date': 'Date (YYY-MM-DD)'
        }
class LookupForm(forms.ModelForm):
    class Meta:
        model=LookUp
        fields=('name',)

class LookupDetailsForm(forms.ModelForm):
    class Meta:
        model=LookupDetail
        fields=('Lookup_Name','Details')