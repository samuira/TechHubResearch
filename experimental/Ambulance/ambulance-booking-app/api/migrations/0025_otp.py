# Generated by Django 2.1.7 on 2019-03-07 14:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0024_auto_20190227_1326'),
    ]

    operations = [
        migrations.CreateModel(
            name='OTP',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('otp_type', models.CharField(max_length=50, unique=True)),
                ('counter', models.IntegerField(default=0)),
                ('secret_key', models.CharField(max_length=20)),
                ('is_verified', models.SmallIntegerField(default=0)),
            ],
        ),
    ]