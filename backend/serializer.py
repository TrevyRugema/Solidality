
from rest_framework import serializers
from .models import *
from phonenumber_field.modelfields import PhoneNumberField
class MemberSerializer(serializers.ModelSerializer):
    is_active = serializers.BooleanField(default=True)   # can login
    roles = (('Admin', 'Admin'),('President','President'),
            ('Accountant','Accountant'), ('Ordinary', 'Ordinary')
            )
    atte = (('Present', 'Present'), ('Absent', 'Absent'))
    joining_date =serializers.DateTimeField(default=datetime.now)
    status = serializers.CharField(default='Absent',)
    email = serializers.EmailField(max_length=255)
    telephone = PhoneNumberField()
    application_fee = serializers.IntegerField(default=10000)
    Role = serializers.CharField(max_length=50)

    class Meta:
        model=Person
        fields=['id','joining_date','telephone','Role','application_fee']
    
class MemberDetailSerializer(serializers.ModelSerializer):
    is_active = serializers.BooleanField(default=True)   # can login
    roles = (('Admin', 'Admin'), ('Ordinary', 'Ordinary'))
    atte = (('Present', 'Present'), ('Absent', 'Absent'))
    joining_date =serializers.DateTimeField(default=datetime.now)
    status = serializers.CharField(max_length=50)
    email = serializers.EmailField(max_length=255)
    telephone = PhoneNumberField()
    first_name = serializers.CharField(max_length=30)
    last_name = serializers.CharField(max_length=255)
    username = serializers.CharField(max_length=30)
    application_fee = serializers.IntegerField(default=10000)
    Role = serializers.CharField(max_length=250)

    class Meta:
        model=Member
        fields='__all__'

class MemberUpdateStatus(serializers.ModelSerializer):
    model=Member
    fields=['status','roles']


class SocialFundSerializer(serializers.ModelSerializer):
    pass


class SocialFundDetailSerializer(serializers.ModelSerializer):
    pass

class AttendanceSerializer(serializers.ModelSerializer):
    pass


class AttendanceDetailSerializer(serializers.ModelSerializer):
    pass


class AttendanceUpdateStatusSerializer(serializers.ModelSerializer):
    pass


class SavingSerializer(serializers.ModelSerializer):
    pass

class SavingDetailSerializer(serializers.ModelSerializer):
    pass

class LoanSerializer(serializers.ModelSerializer):
    pass

class LoanDetailSerializer(serializers.ModelSerializer):
    pass

class LoanUpdateStatusSerializer(serializers.ModelSerializer):
    pass

class PayloanSerializer(serializers.ModelSerializer):
    pass

class PayloanDetailSerializer(serializers.ModelSerializer):
    pass

class PayLoanUpdateStatusSerializer(serializers.ModelSerializer):
    pass
