# Generated by Django 5.0.1 on 2024-02-06 17:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('empapp', '0002_alter_employee_employee_image'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='employee',
            name='employee_id',
        ),
    ]
