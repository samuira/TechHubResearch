# Generated by Django 2.1.7 on 2019-02-21 12:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0010_user_profile_picture'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='country_code',
            field=models.CharField(default='', max_length=5),
        ),
        migrations.AddField(
            model_name='user',
            name='rating',
            field=models.CharField(default='0', max_length=2),
        ),
        migrations.AlterField(
            model_name='user',
            name='profile_picture',
            field=models.ImageField(blank=True, null=True, upload_to='profile/%Y/%m/%d'),
        ),
    ]