# Generated by Django 2.2.5 on 2019-09-26 08:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ProposalApp', '0010_unitmodel'),
    ]

    operations = [
        migrations.AlterField(
            model_name='unitmodel',
            name='assessmentInfo',
            field=models.CharField(blank=True, max_length=256),
        ),
        migrations.AlterField(
            model_name='unitmodel',
            name='contentInfo',
            field=models.CharField(blank=True, max_length=256),
        ),
        migrations.AlterField(
            model_name='unitmodel',
            name='outcomes',
            field=models.CharField(blank=True, max_length=256),
        ),
    ]