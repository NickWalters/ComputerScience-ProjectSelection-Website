# Generated by Django 2.2.5 on 2019-09-23 12:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ProposalApp', '0008_auto_20190912_1339'),
    ]

    operations = [
        migrations.AlterField(
            model_name='projectmodel',
            name='draft',
            field=models.BooleanField(default=False),
        ),
    ]
