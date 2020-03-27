# coding=gbk
from decimal import *
from utils.BidConst import BidConst
from utils.DecimalFormatUtil import DecimalFormatUtil



class CalculatetUtil:
    __ONE_HUNDRED = Decimal('100.0000')#1/100
    __NUMBER_MONTHS_OF_YEAR = Decimal('12.0000')
    __ACCOUNT_MANAGER_CHARGE_RATE = Decimal('0.050') #�������
    __INTEREST_MANAGER_CHARGE_RATE = Decimal('0.1000')# ������Ϣ

    # ����ÿ�µ�����
    @classmethod
    def getMonthlyRate(cls, yearRate):
        if yearRate == 0:
            return 0
        return yearRate / cls.__ONE_HUNDRED / cls.__NUMBER_MONTHS_OF_YEAR

#���bug�����ţ����ݲ���ȷ
    @classmethod
    def cal_set(cls):
        # ����ȫ�ļ��㾫�Ⱥ�ȡֵ��ʽ
        mycontext = Context(prec=BidConst.CAL_SCALE(), rounding=ROUND_HALF_UP)
        setcontext(mycontext)
        # �������㾫��
    # / **
    # *����������Ϣ
    # *
    # * @ param
    # returnType
    # *��������
    # * @ param
    # bidRequestAmount
    # *�����
    # * @ param
    # yearRate
    # *������
    # * @ param
    # monthes2Return
    # *��������
    # * @ return
    # * /    # *����������Ϣ
    @classmethod
    def calTotalInterest(cls,returnType, bidRequestAmount, yearRate, monthes2Return):
        # cls.cal_set()

        bidRequestAmount = Decimal(str(bidRequestAmount))
        yearRate = Decimal(str(yearRate))
        totalInterest = Decimal('0.0000')
        monthlyRate = cls.getMonthlyRate(yearRate)
        if returnType == BidConst.GET_RETURN_TYPE_MONTH_INTEREST_PRINCIPAL(): #���·���
            #ֻ���һ����
            if monthes2Return == 1:
                totalInterest = bidRequestAmount * monthlyRate
            else:
                temp1 = bidRequestAmount * monthlyRate
                temp2 = pow((Decimal('1') + monthlyRate), monthes2Return)
                temp3 = pow((Decimal('1') + monthlyRate),monthes2Return) - Decimal('1')
                #����ÿ�»���
                monthToReturnMoney = (temp1 * temp2) / temp3
                #�����ܻ���
                totalReturnMoney = monthToReturnMoney * Decimal(str(monthes2Return))
                #�����Ϣ
                totalInterest = totalReturnMoney - bidRequestAmount
        elif returnType == BidConst.GET_RETURN_TYPE_MONTH_INTEREST(): #���µ���
            monthlyInterest = DecimalFormatUtil.amountformat((bidRequestAmount * monthlyRate))
            totalInterest = monthlyInterest * monthes2Return

        return  DecimalFormatUtil.formatBigDecimal(totalInterest, BidConst.STORE_SCALE())

# / **
# *����ÿ����Ϣ
# *
# * @ param
# returnType
# *��������
# * @ param
# bidRequestAmount
# *�����
# * @ param
# yearRate
# *������
# * @ param
# monthIndex
# *�ڼ���
# * @ param
# monthes2Return
# *��������
# * @ return
# * /
    @classmethod
    def calMonthlyInterest(cls, returnType,  bidRequestAmount, yearRate, monthIndex, monthes2Return):
        # cls.cal_set()

        bidRequestAmount = Decimal(str(bidRequestAmount))
        yearRate = Decimal(str(yearRate))
        monthlyInterest = Decimal('0.0000')
        monthlyRate = cls.getMonthlyRate(yearRate)
        if returnType == BidConst.GET_RETURN_TYPE_MONTH_INTEREST_PRINCIPAL(): #���·���
            if monthes2Return == 1: #ֻ��һ����
                monthlyInterest = bidRequestAmount * monthlyRate
            else:
                temp1 = bidRequestAmount * monthlyRate
                temp2 = pow(Decimal('1') + monthlyRate, monthes2Return)
                temp3 = pow(Decimal('1') + monthlyRate, monthes2Return) - Decimal('1')
                temp4 = pow(Decimal('1') + monthlyRate, monthIndex-1)
                #����ÿ�»���
                monthToReturnMoney = (temp1 * temp2) / temp3
                #����ܻ���
                totalReturnMoney = monthToReturnMoney * Decimal(str(monthes2Return))
                #�����Ϣ
                totalInterest = totalReturnMoney - bidRequestAmount

                if monthIndex < monthes2Return:
                    monthlyInterest = ((temp1 - monthToReturnMoney) * temp4)+monthToReturnMoney

                elif monthIndex == monthes2Return:
                    temp6 = Decimal('0.0000')
                    # �������һ��֮ǰ������Ϣ֮��
                    for i in range(1,monthes2Return):
                        temp5 = pow(Decimal('1') + monthlyRate, i-1)
                        monthlyInterest = ((temp1 - monthToReturnMoney) * temp5) + monthToReturnMoney
                        temp6 = temp6 + monthlyInterest

                    monthlyInterest = totalInterest - temp6

                    # for
        elif returnType == BidConst.GET_RETURN_TYPE_MONTH_INTEREST(): #���µ���
            monthlyInterest = DecimalFormatUtil.amountformat((bidRequestAmount * monthlyRate))

        return monthlyInterest

# / **
# *����ÿ�ڻ���
# *
# * @ param
# returnType
# *��������
# * @ param
# bidRequestAmount
# *�����
# * @ param
# yearRate
# *������
# * @ param
# monthIndex
# *�ڼ���
# * @ param
# monthes2Return
# *��������
# * @ return
# * /
    @classmethod
    def calMonthToReturnMoney(cls, returnType, bidRequestAmount,  yearRate, monthIndex, monthes2Return):
        # cls.cal_set()

        bidRequestAmount = Decimal(str(bidRequestAmount))
        yearRate = Decimal(str(yearRate))
        monthToReturnMoney =  Decimal('0.0000')
        monthlyRate = cls.getMonthlyRate(yearRate)
        if returnType == BidConst.GET_RETURN_TYPE_MONTH_INTEREST_PRINCIPAL():#���·���
            if monthes2Return == 1:  # ֻ��һ����
                monthlyInterest = bidRequestAmount + (bidRequestAmount * monthlyRate)
            else:
                temp1 = bidRequestAmount * monthlyRate
                temp2 = pow(Decimal('1') + monthlyRate, monthes2Return)
                temp3 = pow(Decimal('1') + monthlyRate, monthes2Return) - Decimal('1')
                #����ÿ�»���
                monthToReturnMoney = (temp1 * temp2) / temp3
        elif returnType == BidConst.GET_RETURN_TYPE_MONTH_INTEREST(): #���µ���
            monthlyInterest = bidRequestAmount * monthlyRate
            if monthIndex == monthes2Return:
                monthToReturnMoney = bidRequestAmount + monthlyInterest
            elif monthIndex < monthes2Return:
                monthToReturnMoney = monthlyInterest
        return DecimalFormatUtil.formatBigDecimal(monthToReturnMoney,BidConst.STORE_SCALE())

# / **
# *����һ��Ͷ��ʵ�ʻ�õ���Ϣ = Ͷ���� / ����� * ����Ϣ
# *
# * @ param
# bidRequestAmount
# *�����
# * @ param
# monthes2Return
# *��������
# * @ param
# yearRate
# *������
# * @ param
# returnType
# *��������
# * @ param
# acturalBidAmount
# *Ͷ����
# * @ return
# * /
    @classmethod
    def calBidInterest(cls, bidRequestAmount, monthes2Return,yearRate,  returnType, acturalBidAmount):
        cls.cal_set()

        acturalBidAmount =Decimal(str(acturalBidAmount))
        #// ������������Ϣ
        totalInterest = cls.calTotalInterest(returnType, bidRequestAmount, yearRate, monthes2Return)
        #// ��ռ����
        proportion = acturalBidAmount / bidRequestAmount
        bidInterest = totalInterest * proportion
        return DecimalFormatUtil.formatBigDecimal(bidInterest, BidConst.STORE_SCALE())

# / **
# *������Ϣ�����
# *
# * @ param
# interest
# *��Ϣ
# * @ param
# interestManagerChargeRate
# *��Ϣ����ѱ���
# * @ return
# * /
    @classmethod
    def calInterestManagerCharge(cls, interest):
        interest =Decimal(str(interest))
        return DecimalFormatUtil.formatBigDecimal(interest * cls.__INTEREST_MANAGER_CHARGE_RATE, BidConst.STORE_SCALE())


# / **
# *����������
# *
# * @ param
# bidRequestAmount
# *�����
# * @ param
# returnType
# *��������
# * @ param
# monthes2Return
# *��������
# * @ return
# * /
    @classmethod
    def calAccountManagementCharge(cls,bidRequestAmount):
        bidRequestAmount = Decimal(str(bidRequestAmount))
        accountManagementCharge = DecimalFormatUtil.formatBigDecimal(bidRequestAmount * cls.__ACCOUNT_MANAGER_CHARGE_RATE, BidConst.STORE_SCALE())
        return accountManagementCharge