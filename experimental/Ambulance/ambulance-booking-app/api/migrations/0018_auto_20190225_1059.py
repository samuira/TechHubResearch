# Generated by Django 2.1.7 on 2019-02-25 10:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0017_auto_20190225_0659'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='otp',
        ),
        migrations.AddField(
            model_name='user',
            name='otp_secrect_key',
            field=models.CharField(default='', max_length=20),
        ),
    ]
