# Generated by Django 2.1.7 on 2019-02-27 08:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0021_auto_20190227_0809'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ambulancetype',
            name='cost_per_km',
            field=models.FloatField(default=0.0),
        ),
        migrations.AlterField(
            model_name='ambulancetype',
            name='cost_per_minute',
            field=models.FloatField(default=0.0),
        ),
    ]