# Generated by Django 3.2.15 on 2022-10-20 08:58

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('aflink', '0003_alter_season_document'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='drop',
            name='created_date',
        ),
        migrations.RemoveField(
            model_name='drop',
            name='name',
        ),
        migrations.AddField(
            model_name='drop',
            name='auhorisedby',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='auhorisedby', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='drop',
            name='cost',
            field=models.DecimalField(decimal_places=0, max_digits=20, null=True),
        ),
        migrations.AddField(
            model_name='drop',
            name='destination',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='drop',
            name='item',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='drop',
            name='quantity',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='drop',
            name='requestedby',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='requestedby', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='drop',
            name='status',
            field=models.CharField(choices=[('pending', 'Pending'), ('decline', 'Decline'), ('approved', 'Approved'), ('processing', 'Processing'), ('complete', 'Complete'), ('bulk', 'Bulk')], max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='drop',
            name='verifiedby',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='verifiedby', to=settings.AUTH_USER_MODEL),
        ),
    ]