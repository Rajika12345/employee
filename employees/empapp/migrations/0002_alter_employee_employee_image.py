# Generated by Django 5.0.1 on 2024-02-06 17:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('empapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='employee_image',
            field=models.ImageField(blank=True, default='images/default.jpg', upload_to='images'),
        ),
    ]