
from rest_framework import serializers
from backend.models import Item,JobCard,Customer


class ItemSerializer(serializers.ModelSerializer):
    class Meta:
        model=Item
        fields="__all__"



class JobCardSerializer(serializers.ModelSerializer):
    class Meta:
        model=JobCard
        fields="__all__"


class CustomerSerializer(serializers.ModelSerializer):

    class Meta:
        model = Customer 
        fields = ('pk','first_name', 'last_name', 'email', 'phone','address','description')
