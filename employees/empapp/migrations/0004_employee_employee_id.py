# Generated by Django 5.0.1 on 2024-02-06 17:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('empapp', '0003_remove_employee_employee_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='employee',
            name='employee_id',
            field=models.CharField(default=1, max_length=200, unique=True),
            preserve_default=False,
        ),
    ]
