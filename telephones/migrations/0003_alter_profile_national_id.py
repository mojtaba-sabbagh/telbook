# Generated by Django 4.0.4 on 2022-06-14 13:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('telephones', '0002_alter_department_super_dep'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='national_id',
            field=models.CharField(blank=True, max_length=10, null=True, unique=True),
        ),
    ]
