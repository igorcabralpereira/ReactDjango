# Generated by Django 4.1 on 2022-10-04 19:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('EmployeeApp', '0002_rename_employeesid_employees_employeeid'),
    ]

    operations = [
        migrations.RenameField(
            model_name='employees',
            old_name='EmployeesName',
            new_name='EmployeeName',
        ),
    ]
