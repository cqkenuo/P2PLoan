# Generated by Django 2.2.6 on 2020-02-18 02:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0017_auto_20200217_2244'),
    ]

    operations = [
        migrations.AddField(
            model_name='investor',
            name='identity_number',
            field=models.CharField(blank=True, max_length=25, null=True, verbose_name='身份证号码'),
        ),
    ]
