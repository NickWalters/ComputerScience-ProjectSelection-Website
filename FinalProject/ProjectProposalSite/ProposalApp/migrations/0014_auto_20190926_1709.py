# Generated by Django 2.2.5 on 2019-09-26 09:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ProposalApp', '0013_remove_unitmodel_contentinfo'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='unitmodel',
            name='assessmentInfo',
        ),
        migrations.RemoveField(
            model_name='unitmodel',
            name='coordinatorName',
        ),
        migrations.RemoveField(
            model_name='unitmodel',
            name='credit',
        ),
        migrations.RemoveField(
            model_name='unitmodel',
            name='fieldOfDiscipline',
        ),
        migrations.RemoveField(
            model_name='unitmodel',
            name='outcomes',
        ),
        migrations.RemoveField(
            model_name='unitmodel',
            name='prerequisites',
        ),
        migrations.RemoveField(
            model_name='unitmodel',
            name='semester',
        ),
    ]
