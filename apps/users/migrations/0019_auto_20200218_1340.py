# Generated by Django 2.2.6 on 2020-02-18 13:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0018_investor_identity_number'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='borrower',
            name='identity_number',
        ),
        migrations.RemoveField(
            model_name='investor',
            name='identity_number',
        ),
        migrations.AddField(
            model_name='userprofile',
            name='identity_number',
            field=models.CharField(blank=True, max_length=25, null=True, verbose_name='身份证号码'),
        ),
    ]
