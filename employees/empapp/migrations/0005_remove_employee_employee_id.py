# Generated by Django 5.0.1 on 2024-02-06 17:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('empapp', '0004_employee_employee_id'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='employee',
            name='employee_id',
        ),
    ]