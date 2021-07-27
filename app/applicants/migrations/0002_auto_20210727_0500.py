# Generated by Django 3.2.5 on 2021-07-27 09:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('applicants', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='nationality',
            options={'ordering': ['name'], 'verbose_name_plural': 'nationalities'},
        ),
        migrations.AddField(
            model_name='applicant',
            name='occupation',
            field=models.CharField(max_length=100, null=True),
        ),
    ]
