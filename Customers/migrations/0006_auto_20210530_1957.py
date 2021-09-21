# Generated by Django 3.1.7 on 2021-05-30 14:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Customers', '0005_order_orderupdt'),
    ]

    operations = [
        migrations.CreateModel(
            name='Process',
            fields=[
                ('processid', models.AutoField(primary_key=True, serialize=False)),
                ('order_id', models.IntegerField()),
                ('raw_material', models.CharField(max_length=122)),
                ('design', models.CharField(max_length=122)),
                ('printing', models.CharField(max_length=122)),
                ('cylsize', models.IntegerField(blank=True, null=True)),
                ('date', models.DateField()),
            ],
        ),
        migrations.AlterField(
            model_name='userinfo',
            name='UserID',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]
