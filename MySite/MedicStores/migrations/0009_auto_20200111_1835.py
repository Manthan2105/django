# Generated by Django 3.0 on 2020-01-11 13:05

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import phone_field.models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('MedicStores', '0008_auto_20200110_1530'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='clientmodel',
            name='phone',
        ),
        migrations.AddField(
            model_name='clientmodel',
            name='age',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='clientmodel',
            name='phone_number',
            field=phone_field.models.PhoneField(blank=True, default='', help_text='Contact phone number', max_length=31),
        ),
        migrations.AddField(
            model_name='clientmodel',
            name='profile_pic',
            field=models.ImageField(blank=True, default='', upload_to='profile_pics'),
        ),
        migrations.AlterField(
            model_name='clientmodel',
            name='gender',
            field=models.CharField(choices=[('M', 'Male'), ('F', 'Female')], default='', max_length=1),
        ),
        migrations.AlterField(
            model_name='clientmodel',
            name='user',
            field=models.OneToOneField(default='', on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.DeleteModel(
            name='deliveryboyModel',
        ),
    ]
