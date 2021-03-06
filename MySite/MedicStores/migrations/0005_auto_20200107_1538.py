# Generated by Django 3.0.1 on 2020-01-07 10:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('MedicStores', '0004_auto_20200106_1551'),
    ]

    operations = [
        migrations.CreateModel(
            name='category',
            fields=[
                ('c_id', models.AutoField(primary_key=True, serialize=False)),
                ('c_name', models.CharField(max_length=50)),
                ('c_desc', models.CharField(max_length=150)),
            ],
        ),
        migrations.CreateModel(
            name='faq',
            fields=[
                ('faq_id', models.AutoField(primary_key=True, serialize=False)),
                ('faq_que', models.CharField(max_length=100)),
                ('faq_ans', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='inquiry',
            fields=[
                ('in_id', models.AutoField(primary_key=True, serialize=False)),
                ('in_desc', models.CharField(max_length=100)),
                ('in_mail', models.EmailField(max_length=254)),
                ('in_msg', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='order',
            fields=[
                ('o_id', models.AutoField(primary_key=True, serialize=False)),
                ('total', models.IntegerField(blank=True)),
                ('cl_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='MedicStores.client')),
                ('db_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='MedicStores.deliveryboy')),
            ],
        ),
        migrations.CreateModel(
            name='status',
            fields=[
                ('s_id', models.AutoField(primary_key=True, serialize=False)),
                ('s_name', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Subcategory',
            fields=[
                ('sc_id', models.AutoField(primary_key=True, serialize=False)),
                ('sc_name', models.CharField(max_length=20)),
                ('sc_desc', models.CharField(max_length=100)),
                ('c_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='MedicStores.category')),
            ],
        ),
        migrations.CreateModel(
            name='product',
            fields=[
                ('p_id', models.AutoField(primary_key=True, serialize=False)),
                ('p_name', models.CharField(max_length=20)),
                ('p_desc', models.CharField(max_length=100)),
                ('p_price', models.IntegerField()),
                ('sc_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='MedicStores.Subcategory')),
            ],
        ),
        migrations.CreateModel(
            name='prescription',
            fields=[
                ('pr_id', models.AutoField(primary_key=True, serialize=False)),
                ('pr_photo', models.ImageField(upload_to='')),
                ('cl_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='MedicStores.client')),
                ('s_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='MedicStores.status')),
            ],
        ),
        migrations.CreateModel(
            name='order_details',
            fields=[
                ('od_id', models.AutoField(primary_key=True, serialize=False)),
                ('quantity', models.IntegerField()),
                ('o_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='MedicStores.order')),
                ('p_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='MedicStores.product')),
            ],
        ),
        migrations.AddField(
            model_name='order',
            name='s_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='MedicStores.status'),
        ),
        migrations.CreateModel(
            name='feedback',
            fields=[
                ('f_id', models.AutoField(primary_key=True, serialize=False)),
                ('f_msg', models.CharField(blank=True, max_length=150)),
                ('f_reply', models.CharField(max_length=150)),
                ('o_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='MedicStores.order')),
            ],
        ),
        migrations.CreateModel(
            name='delivery',
            fields=[
                ('d_id', models.AutoField(primary_key=True, serialize=False)),
                ('d_address1', models.CharField(max_length=200)),
                ('d_address2', models.CharField(max_length=200)),
                ('d_address3', models.CharField(max_length=200)),
                ('d_pincode', models.IntegerField()),
                ('cl_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='MedicStores.client')),
            ],
        ),
    ]
