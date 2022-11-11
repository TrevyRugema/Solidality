# Generated by Django 3.2.16 on 2022-11-10 08:14

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import django_fsm


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=120, unique=True)),
                ('address', models.CharField(max_length=220)),
                ('created_date', models.DateField(auto_now_add=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('supplier_name', models.CharField(max_length=150, null=True, verbose_name='Supplier Name')),
                ('item_name', models.CharField(max_length=150, verbose_name='Item Name')),
                ('delivery_no', models.CharField(max_length=100, verbose_name='Delivery Number')),
                ('batch_no', models.CharField(max_length=100, verbose_name='Batch Number')),
                ('quantity', models.FloatField(verbose_name='Quantity')),
                ('unit_cost', models.FloatField(verbose_name='Unit Cost')),
                ('date_received', models.DateTimeField(default=django.utils.timezone.now)),
                ('expiry_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('position', models.CharField(max_length=100)),
                ('document', models.FileField(blank=True, upload_to='media')),
                ('receivedBy', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'Item Receiving',
            },
        ),
        migrations.CreateModel(
            name='JobCard',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('job_type', models.CharField(max_length=50, null=True, verbose_name='Job Type')),
                ('order_number', models.CharField(max_length=50, null=True, verbose_name='Order Number')),
                ('date', models.DateField(null=True)),
                ('customer', models.CharField(max_length=200, null=True)),
                ('contact', models.CharField(max_length=13, null=True)),
                ('job_descritpion', models.TextField(null=True, verbose_name='Job Description')),
            ],
        ),
        migrations.CreateModel(
            name='Supplier',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=120)),
                ('address', models.CharField(max_length=220)),
                ('created_date', models.DateField(auto_now_add=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Requisition',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('item', models.CharField(max_length=100, null=True)),
                ('quantity', models.IntegerField(null=True)),
                ('cost', models.DecimalField(decimal_places=0, max_digits=20, null=True)),
                ('destination', models.CharField(max_length=255, null=True)),
                ('auhorisedby', models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='auhorisedby', to=settings.AUTH_USER_MODEL)),
                ('requestedby', models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='requestedby', to=settings.AUTH_USER_MODEL)),
                ('verifiedby', models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='verifiedby', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('design', models.CharField(max_length=50)),
                ('color', models.CharField(max_length=50)),
                ('status', models.CharField(choices=[('pending', 'Pending'), ('decline', 'Decline'), ('approved', 'Approved'), ('processing', 'Processing'), ('complete', 'Complete')], max_length=10)),
                ('created_date', models.DateField(auto_now_add=True)),
                ('customer', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='aflink.customer')),
                ('drop', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='aflink.requisition')),
                ('item_name', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='aflink.item')),
                ('jobcard', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='aflink.jobcard')),
                ('supplier', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='aflink.supplier')),
            ],
        ),
        migrations.CreateModel(
            name='JobCardFLow',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('state', django_fsm.FSMField(default='new', max_length=50)),
                ('jobcard', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='aflink.jobcard')),
            ],
        ),
        migrations.CreateModel(
            name='Delivery',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('courier_name', models.CharField(max_length=120)),
                ('created_date', models.DateField(auto_now_add=True)),
                ('order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='aflink.order')),
            ],
        ),
    ]
