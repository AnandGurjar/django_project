# Generated by Django 3.2.5 on 2021-07-21 16:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_rename_images_images_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='client',
            name='ad',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='client',
            name='anand',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='mail',
            field=models.EmailField(max_length=70),
        ),
    ]
