# Generated by Django 2.1.4 on 2019-04-05 13:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0012_auto_20190122_0927'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='is_alert_send',
            field=models.CharField(default='0', help_text='0=No, 1=Yes', max_length=10),
        ),
    ]
