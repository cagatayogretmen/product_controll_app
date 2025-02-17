# Generated by Django 3.0.8 on 2021-01-22 09:20

from django.db import migrations, models
import processes.models


class Migration(migrations.Migration):

    dependencies = [
        ('processes', '0128_auto_20210122_1146'),
    ]

    operations = [
        migrations.AlterField(
            model_name='process_7',
            name='picture1',
            field=models.ImageField(blank=True, null=True, upload_to=processes.models.Process1_image, verbose_name='Upload Image 1'),
        ),
        migrations.AlterField(
            model_name='process_7',
            name='picture2',
            field=models.ImageField(blank=True, null=True, upload_to=processes.models.Process1_image, verbose_name='Upload Image 2'),
        ),
        migrations.AlterField(
            model_name='process_7',
            name='picture3',
            field=models.ImageField(blank=True, null=True, upload_to=processes.models.Process1_image, verbose_name='Upload Image 3'),
        ),
        migrations.AlterField(
            model_name='process_7',
            name='picture4',
            field=models.ImageField(blank=True, null=True, upload_to=processes.models.Process1_image, verbose_name='Upload Image 4'),
        ),
    ]
