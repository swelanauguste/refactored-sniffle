# Generated by Django 3.2.5 on 2021-07-27 09:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('applicants', '0002_auto_20210727_0500'),
    ]

    operations = [
        migrations.AlterField(
            model_name='applicant',
            name='email',
            field=models.EmailField(blank=True, max_length=254),
        ),
    ]
