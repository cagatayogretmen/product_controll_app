# Generated by Django 3.0.8 on 2020-10-15 12:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('processes', '0075_auto_20201014_1640'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='process_3_2',
            name='q12',
        ),
        migrations.AddField(
            model_name='process_3',
            name='q12',
            field=models.TextField(blank=True, verbose_name='Remarks'),
        ),
    ]
