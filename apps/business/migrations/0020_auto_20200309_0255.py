# Generated by Django 2.2.6 on 2020-03-09 02:55

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('business', '0019_auto_20200308_1935'),
    ]

    operations = [
        migrations.AlterField(
            model_name='accountflow',
            name='accountId',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.Account', verbose_name='用户账户'),
        ),
        migrations.CreateModel(
            name='UserBanknInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bankName', models.CharField(blank=True, max_length=50, null=True, verbose_name='银行名称')),
                ('accountName', models.CharField(blank=True, max_length=50, null=True, verbose_name='开户人姓名')),
                ('accountNumber', models.CharField(blank=True, max_length=50, null=True, verbose_name='银行账号')),
                ('bankForkName', models.CharField(blank=True, max_length=50, null=True, verbose_name='开户支行')),
                ('userProfile', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='userBanknInfos', to=settings.AUTH_USER_MODEL, verbose_name='用户')),
            ],
            options={
                'verbose_name': '投资人的回款明细',
                'verbose_name_plural': '投资人的回款明细',
            },
        ),
    ]
