# Generated by Django 2.2.5 on 2019-10-05 08:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ProposalApp', '0003_auto_20191003_1005'),
    ]

    operations = [
        migrations.AddField(
            model_name='unitmodel',
            name='name',
            field=models.CharField(blank=True, max_length=64),
        ),
    ]