# Generated by Django 4.1.7 on 2023-04-01 13:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employee', '0002_alter_employee_eemail_alter_employee_eid_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='employee',
            name='imagen',
            field=models.ImageField(default='SOME STRING', upload_to='img/'),
        ),
    ]
