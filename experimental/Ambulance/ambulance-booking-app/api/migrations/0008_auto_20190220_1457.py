# Generated by Django 2.1.7 on 2019-02-20 14:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0007_auto_20190220_1456'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user',
            old_name='email',
            new_name='user_email',
        ),
    ]