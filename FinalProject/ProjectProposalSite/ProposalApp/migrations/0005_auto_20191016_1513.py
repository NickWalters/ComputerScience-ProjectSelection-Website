# Generated by Django 2.2.5 on 2019-10-16 07:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ProposalApp', '0004_auto_20191014_2209'),
    ]

    operations = [
        migrations.AlterField(
            model_name='unitmodel',
            name='unitCode',
            field=models.CharField(max_length=32, unique=True),
        ),
    ]
