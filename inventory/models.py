
from django.db import models
from backend.models import  Supplier
from accounts.models import User
class Department(models.Model):
    pass

class Stock(models.Model):
    item=models.CharField(max_length=100)
    quantity=models.IntegerField(blank=False,null=True)
    cost=models.FloatField(blank=False,null=True)
    batch_no=models.CharField('Batch No', max_length=0)
    delivery_no=models.CharField('Delivery No', max_length=50)
    received_date =models.DateField('Created Date',blank=False, null=True)
    expiry_date=models.CharField('Expiry Date')
    supplier=models.ForeignKey(Supplier,on_delete=models.CASCADE)
    received_by=models.ForeignKey(User,on_delete=models.CASCADE) 
    position=models.CharField(max_length=100)
    document=models.FileField(upload_to='media',blank=True)

    def __str__(self):
        return self.item 
    class Meta:
        abstract=True

    @property

    def total_stock(self):
        total_cost= self.quantity * self.cost
        total_stock +=total_cost
        return  total_stock

    @property
    def check_stock_availability(total_stock):

        qty=total_stock
        stocks=Stock.objects.get(total_stock=total_stock)

        for stock in stocks:
            if qty > 0:
                qty_letf=qty
                qty -=total_stock

            elif qty >=0:
                pass

    @property
    def __main__(self,total_stock):
        return total_stock()

    


    