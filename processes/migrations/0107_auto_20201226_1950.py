# Generated by Django 3.0.8 on 2020-12-26 16:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('processes', '0106_auto_20201226_1950'),
    ]

    operations = [
        migrations.AlterField(
            model_name='process_5_2',
            name='q1',
            field=models.IntegerField(choices=[(0, 'Yes'), (1, 'No'), (2, 'Not Relavant')], verbose_name='The HPU is painted as requested in order form.'),
        ),
        migrations.AlterField(
            model_name='process_5_2',
            name='q2',
            field=models.IntegerField(choices=[(0, 'Yes'), (1, 'No'), (2, 'Not Relavant')], verbose_name='There is no any surface as not painted and surface quality of paint as requested.'),
        ),
    ]
