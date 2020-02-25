# Generated by Django 2.2.6 on 2020-02-22 20:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0021_account'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='account',
            name='fee',
        ),
        migrations.AddField(
            model_name='account',
            name='borrowLimit',
            field=models.DecimalField(decimal_places=4, default=0.0, max_digits=18, verbose_name='账户授信额度'),
        ),
        migrations.AddField(
            model_name='account',
            name='freezedAmount',
            field=models.DecimalField(decimal_places=4, default=0.0, max_digits=18, verbose_name='账户冻结金额'),
        ),
        migrations.AddField(
            model_name='account',
            name='remainBorrowLimit',
            field=models.DecimalField(decimal_places=4, default=0.0, max_digits=18, verbose_name='账户剩余授信额度'),
        ),
        migrations.AddField(
            model_name='account',
            name='tradePassword',
            field=models.CharField(blank=True, max_length=128, null=True, verbose_name='交易密码'),
        ),
        migrations.AddField(
            model_name='account',
            name='unReceiveInterest',
            field=models.DecimalField(decimal_places=4, default=0.0, max_digits=18, verbose_name='账户待收利息'),
        ),
        migrations.AddField(
            model_name='account',
            name='unReceivePrincipal',
            field=models.DecimalField(decimal_places=4, default=0.0, max_digits=18, verbose_name='账户待收本金'),
        ),
        migrations.AddField(
            model_name='account',
            name='unReturnAmount',
            field=models.DecimalField(decimal_places=4, default=0.0, max_digits=18, verbose_name='账户待还金额'),
        ),
        migrations.AddField(
            model_name='account',
            name='usableAmount',
            field=models.DecimalField(decimal_places=4, default=0.0, max_digits=18, verbose_name='账户可用余额'),
        ),
        migrations.AddField(
            model_name='account',
            name='verifyCode',
            field=models.CharField(blank=True, max_length=128, null=True, verbose_name='数据校验'),
        ),
    ]