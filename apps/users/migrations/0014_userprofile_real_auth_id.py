# Generated by Django 2.2.6 on 2020-02-14 18:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0013_auto_20200213_1214'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='real_auth_id',
            field=models.CharField(blank=True, max_length=20, null=True, verbose_name='实名认证表'),
        ),
    ]
