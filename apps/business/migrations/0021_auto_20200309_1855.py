# Generated by Django 2.2.6 on 2020-03-09 18:55

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('business', '0020_auto_20200309_0255'),
    ]

    operations = [
        migrations.AlterField(
            model_name='accountflow',
            name='accountId',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.Account', verbose_name='用户账户'),
        ),
        migrations.CreateModel(
            name='MoneyWithdraw',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('remark', models.TextField(blank=True, max_length=40, null=True, verbose_name='审核备注')),
                ('state', models.IntegerField(blank=True, choices=[(0, '未审核'), (1, '审核通过'), (2, '审核拒绝')], default=0, null=True, verbose_name='审核状态')),
                ('auditor', models.CharField(blank=True, max_length=10, null=True, verbose_name='审核人')),
                ('applyTime', models.DateTimeField(auto_now_add=True, verbose_name='申请时间')),
                ('audiTime', models.DateTimeField(blank=True, null=True, verbose_name='审核时间')),
                ('amount', models.DecimalField(decimal_places=4, default=0.0, max_digits=18, verbose_name='提现金额')),
                ('charge', models.DecimalField(decimal_places=4, default=0.0, max_digits=18, verbose_name='提现手续费')),
                ('bankName', models.CharField(blank=True, max_length=50, null=True, verbose_name='银行名称')),
                ('accountName', models.CharField(blank=True, max_length=50, null=True, verbose_name='开户人姓名')),
                ('accountNumber', models.CharField(blank=True, max_length=50, null=True, verbose_name='银行账号')),
                ('bankForkName', models.CharField(blank=True, max_length=50, null=True, verbose_name='开户支行')),
                ('applier', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='申请人')),
            ],
            options={
                'verbose_name': '提现审核',
                'verbose_name_plural': '提现审核',
            },
        ),
    ]
