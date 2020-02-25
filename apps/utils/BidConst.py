# coding=gbk

#Լ��  GET������ͷ��ֻ���𷵻�����
      # ������Ա�������𷵻����ݣ������������ݿ�


class BidConst:

        # /**
     # * ����洢����
     # */
    __STORE_SCALE = 4
    # /**
    #  * �������㾫��
    #  */
    __CAL_SCALE = 8

    # /**
    #  * ������ʾ����
    #  */
    __DISPLAY_SCALE = 2

    # /**
    #  * ����ϵͳ�����0
    #  */
    __ZERO = 0.0

    # /**
    #  * �����ʼ���Ŷ��
    #  */
    __INIT_BORROW_LIMIT = 5000.0000

    # / **
    # *Ҫ�ܽ����Ҫ�ﵽ����ͷ�ط���
    # * /
    __BASE_BORROW_SCORE = 30

    # // --------------------�������� - --------------------------
    __RETURN_TYPE_MONTH_INTEREST_PRINCIPAL = 0  #// ���ʽ
                                                # // ���·��ڻ���(�ȶϢ)

    __RETURN_TYPE_MONTH_INTEREST = 1 #// ���ʽ
                                     # // ���µ��ڻ���(ÿ�»���Ϣ, ���ڻ���Ϣ)


    # // ---------------------������� - -------------------------
    __BIDREQUEST_TYPE_NORMAL = 0 #// ��ͨ���ñ�


    #// ---------------------���״̬ - --------------------------

    __BIDREQUEST_STATE_PUBLISH_PENDING = 0 #// ������
    __BIDREQUEST_STATE_BIDDING = 1 #// �б���
    __BIDREQUEST_STATE_UNDO = 2 #// �ѳ���
    __BIDREQUEST_STATE_BIDDING_OVERDUE = 3 #// ����
    __BIDREQUEST_STATE_APPROVE_PENDING_1 = 4 #// ����1��
    __BIDREQUEST_STATE_APPROVE_PENDING_2 = 5 #// ����2��
    __BIDREQUEST_STATE_REJECTED = 6 #// ������˱��ܾ�
    __BIDREQUEST_STATE_PAYING_BACK = 7 #// ������
    __BIDREQUEST_STATE_COMPLETE_PAY_BACK = 8 #// �ѻ���
    __BIDREQUEST_STATE_PAY_BACK_OVERDUE = 9 #// ����
    __BIDREQUEST_STATE_PUBLISH_REFUSE = 10 #// ������˾ܾ�״̬

    __SMALLEST_BID_AMOUNT = 50.0000 #// ϵͳ�涨����СͶ����
    __SMALLEST_BIDREQUEST_AMOUNT = 500.0000 #// ϵͳ�涨����С�����
    __SMALLEST_CURRENT_RATE = 5.0000 #// ϵͳ��С�����Ϣ
    __MAX_CURRENT_RATE = 20.0000 #// ϵͳ�������Ϣ
    __MIN_WITHDRAW_AMOUNT = 500.0000 #// ϵͳ��С���ֽ��
    __MONEY_WITHDRAW_CHARGEFEE = 2.0000 #// ϵͳ����������

 # == == == == == == == == == == == == == == =�˻���ˮ���� == == == == == == == == == == == == == == == ==

    __ACCOUNT_ACTIONTYPE_RECHARGE_OFFLINE = 0    #// �ʽ���ˮ������³�ֵ
                                           # // �����������

    __ACCOUNT_ACTIONTYPE_WITHDRAW = 1 #// �ʽ���ˮ������ֳɹ�
                                    #// ���������

    __ACCOUNT_ACTIONTYPE_BIDREQUEST_SUCCESSFUL = 2# // �ʽ���ˮ��𣺳ɹ����
                                                #// �����������

    __ACCOUNT_ACTIONTYPE_BID_SUCCESSFUL = 3 #// �ʽ���ˮ��𣺳ɹ�Ͷ��
                                            #// ���������

    __ACCOUNT_ACTIONTYPE_RETURN_MONEY = 4 #// �ʽ���ˮ��𣺻���
                                            #// ����������

    __ACCOUNT_ACTIONTYPE_CALLBACK_MONEY = 5 #// �ʽ���ˮ��𣺻ؿ�
                                            #// �����������

    __ACCOUNT_ACTIONTYPE_CHARGE = 6 #// �ʽ���ˮ���֧��ƽ̨�����
                                    #// ����������

    __ACCOUNT_ACTIONTYPE_INTEREST_SHARE = 7 #// �ʽ���ˮ�����Ϣ�����
                                            #// ����������

    __ACCOUNT_ACTIONTYPE_WITHDRAW_MANAGE_CHARGE = 8 #// �ʽ���ˮ�������������
                                                    #// ����������

    __ACCOUNT_ACTIONTYPE_RECHARGE_CHARGE = 9 #// �ʽ���ˮ��𣺳�ֵ������
                                            #// ����������

    __ACCOUNT_ACTIONTYPE_BID_FREEZED = 10 #// �ʽ���ˮ���Ͷ�궳����
                                        #// ����������
                                        #//����������

    __ACCOUNT_ACTIONTYPE_BID_UNFREEZED = 11 #// �ʽ���ˮ���ȡ��Ͷ�궳����
                                            #// �����ʧ��
                                            #// ���������
                                            #// �����������

    __ACCOUNT_ACTIONTYPE_WITHDRAW_FREEZED = 12 #// �ʽ���ˮ����������붳����
                                            #// ����������
                                            #// ����������

    __ACCOUNT_ACTIONTYPE_WITHDRAW_UNFREEZED = 13 #// �ʽ���ˮ���: ��������ʧ��ȡ��������
                                                #// ���������
                                                #// �����������


# / ** == == == == == == ϵͳ�˻���ˮ���� == == == == == == = * /

    __SYSTEM_ACCOUNT_ACTIONTYPE_MANAGE_CHARGE = 1 #// ϵͳ�˻��յ��˻�����ѣ�������ѣ�

    __SYSTEM_ACCOUNT_ACTIONTYPE_INTREST_MANAGE_CHARGE = 2 #// ϵͳ�˻��յ���Ϣ�����

    __SYSTEM_ACCOUNT_ACTIONTYPE_WITHDRAW_MANAGE_CHARGE = 3 #// ϵͳ�˻��յ�����������


# / ** == == == == =����״̬ == == == == == == == = * /

    __PAYMENT_STATE_NORMAL = 0 #// ��������

    __PAYMENT_STATE_DONE = 1 #// �ѻ�

    __PAYMENT_STATE_OVERDUE = 2 #// ����



#�෽��--------------------------------------------------------------------------����
# =============================#Լ��  GET������ͷ��ֻ���𷵻�����====================

    @classmethod
    def GET_RETURN_TYPE_MONTH_INTEREST_PRINCIPAL(cls):
        return cls.__RETURN_TYPE_MONTH_INTEREST_PRINCIPAL

    @classmethod
    def GET_RETURN_TYPE_MONTH_INTEREST(cls):
        return cls.__RETURN_TYPE_MONTH_INTEREST

    @classmethod
    def GET_BIDREQUEST_TYPE_NORMAL(cls):
        return cls.__BIDREQUEST_TYPE_NORMAL  # // ��ͨ���ñ�
# // ---------------------���״̬ - --------------------------
    @classmethod
    def GET_BIDREQUEST_STATE_PUBLISH_PENDING(cls):
        return cls.__BIDREQUEST_STATE_PUBLISH_PENDING  # // ������

    @classmethod
    def GET_BIDREQUEST_STATE_BIDDING(cls):
        return cls.__BIDREQUEST_STATE_BIDDING  # // �б���

    @classmethod
    def GET_BIDREQUEST_STATE_UNDO(cls):
        return cls.__BIDREQUEST_STATE_UNDO  # // �ѳ���

    @classmethod
    def GET_BIDREQUEST_STATE_BIDDING_OVERDUE(cls):
        return cls.__BIDREQUEST_STATE_BIDDING_OVERDUE  # // ����

    @classmethod
    def GET_BIDREQUEST_STATE_APPROVE_PENDING_1(cls):
        return cls.__BIDREQUEST_STATE_APPROVE_PENDING_1  # // ����1��

    @classmethod
    def GET_BIDREQUEST_STATE_APPROVE_PENDING_2(cls):
        return cls.__BIDREQUEST_STATE_APPROVE_PENDING_2  # // ����2��

    @classmethod
    def GET_BIDREQUEST_STATE_REJECTED(cls):
        return cls.__BIDREQUEST_STATE_REJECTED  # // ������˱��ܾ�

    @classmethod
    def GET_BIDREQUEST_STATE_PAYING_BACK(cls):
        return cls.__BIDREQUEST_STATE_PAYING_BACK  # // ������

    @classmethod
    def GET_BIDREQUEST_STATE_COMPLETE_PAY_BACK(cls):
        return cls.__BIDREQUEST_STATE_COMPLETE_PAY_BACK  # // �ѻ���

    @classmethod
    def GET_BIDREQUEST_STATE_PAY_BACK_OVERDUE(cls):
        return cls.__BIDREQUEST_STATE_PAY_BACK_OVERDUE  # // ����

    @classmethod
    def GET_BIDREQUEST_STATE_PUBLISH_REFUSE(cls):
        return cls.__BIDREQUEST_STATE_PUBLISH_REFUSE  # // ������˾ܾ�״̬

 # == == == == == == == == == == == == == == =�˻���ˮ���� == == == == == == == == == == == == == == == ==

    @classmethod
    def GET_ACCOUNT_ACTIONTYPE_RECHARGE_OFFLINE(cls):
        return cls.__ACCOUNT_ACTIONTYPE_RECHARGE_OFFLINE

    @classmethod
    def GET_ACCOUNT_ACTIONTYPE_WITHDRAW(cls):
        return cls.__ACCOUNT_ACTIONTYPE_WITHDRAW


    @classmethod
    def GET_ACCOUNT_ACTIONTYPE_BIDREQUEST_SUCCESSFUL(cls):
        return cls.__ACCOUNT_ACTIONTYPE_BIDREQUEST_SUCCESSFUL


    @classmethod
    def GET_ACCOUNT_ACTIONTYPE_BID_SUCCESSFUL(cls):
        return cls.__ACCOUNT_ACTIONTYPE_BID_SUCCESSFUL

    @classmethod
    def GET_ACCOUNT_ACTIONTYPE_RETURN_MONEY(cls):
        return cls.__ACCOUNT_ACTIONTYPE_RETURN_MONEY

    @classmethod
    def GET_ACCOUNT_ACTIONTYPE_CALLBACK_MONEY(cls):
        return cls.__ACCOUNT_ACTIONTYPE_CALLBACK_MONEY

    @classmethod
    def GET_ACCOUNT_ACTIONTYPE_CHARGE(cls):
        return cls.__ACCOUNT_ACTIONTYPE_CHARGE

    @classmethod
    def GET_ACCOUNT_ACTIONTYPE_INTEREST_SHARE(cls):
        return cls.__ACCOUNT_ACTIONTYPE_INTEREST_SHARE

    @classmethod
    def GET_ACCOUNT_ACTIONTYPE_WITHDRAW_MANAGE_CHARGE(cls):
        return cls.__ACCOUNT_ACTIONTYPE_WITHDRAW_MANAGE_CHARGE

    @classmethod
    def GET_ACCOUNT_ACTIONTYPE_RECHARGE_CHARGE(cls):
        return cls.__ACCOUNT_ACTIONTYPE_RECHARGE_CHARGE

    @classmethod
    def GET_ACCOUNT_ACTIONTYPE_BID_FREEZED(cls):
        return cls.__ACCOUNT_ACTIONTYPE_BID_FREEZED

    @classmethod
    def GET_ACCOUNT_ACTIONTYPE_BID_UNFREEZED(cls):
        return cls.__ACCOUNT_ACTIONTYPE_BID_UNFREEZED

    @classmethod
    def GET_ACCOUNT_ACTIONTYPE_WITHDRAW_FREEZED(cls):
        return cls.__ACCOUNT_ACTIONTYPE_WITHDRAW_FREEZED

    @classmethod
    def GET_ACCOUNT_ACTIONTYPE_WITHDRAW_UNFREEZED(cls):
        return cls.__ACCOUNT_ACTIONTYPE_WITHDRAW_UNFREEZED


# / ** == == == == == == ϵͳ�˻���ˮ���� == == == == == == = * /
    @classmethod
    def GET_SYSTEM_ACCOUNT_ACTIONTYPE_MANAGE_CHARGE(cls):
        return cls.__SYSTEM_ACCOUNT_ACTIONTYPE_MANAGE_CHARGE

    @classmethod
    def GET_SYSTEM_ACCOUNT_ACTIONTYPE_INTREST_MANAGE_CHARGE(cls):
        return cls.__SYSTEM_ACCOUNT_ACTIONTYPE_INTREST_MANAGE_CHARGE

    @classmethod
    def GET_SYSTEM_ACCOUNT_ACTIONTYPE_WITHDRAW_MANAGE_CHARGE(cls):
        return cls.__SYSTEM_ACCOUNT_ACTIONTYPE_WITHDRAW_MANAGE_CHARGE


# / ** == == == == =����״̬ == == == == == == == = * /
    @classmethod
    def GET_PAYMENT_STATE_NORMAL(cls):
        return cls.__PAYMENT_STATE_NORMAL
    @classmethod
    def GET_PAYMENT_STATE_DONE(cls):
        return cls.__PAYMENT_STATE_DONE
    @classmethod
    def GET_PAYMENT_STATE_OVERDUE(cls):
        return cls.__PAYMENT_STATE_OVERDUE


#�෽��--------------------------------------------------------------------------����
# =============================������Ա�������𷵻����ݣ������������ݿ�====================

    @classmethod
    def STORE_SCALE(cls):
        return cls.__STORE_SCALE

    @classmethod
    def CAL_SCALE(cls):
        return cls.__CAL_SCALE

    @classmethod
    def DISPLAY_SCALE(cls):
        return cls.__DISPLAY_SCALE

    @classmethod
    def ZERO(cls):
        return cls.__ZERO

    @classmethod
    def INIT_BORROW_LIMIT(cls):
        return cls.__INIT_BORROW_LIMIT

    @classmethod
    def BASE_BORROW_SCORE(cls):
        return cls.__BASE_BORROW_SCORE


    #// ---------------------���״̬ - --------------------------
    @classmethod
    def SMALLEST_BID_AMOUNT(cls):
        return cls.__SMALLEST_BID_AMOUNT

    @classmethod
    def SMALLEST_BIDREQUEST_AMOUNT(cls):
        return cls.__SMALLEST_BIDREQUEST_AMOUNT

    @classmethod
    def SMALLEST_CURRENT_RATE(cls):
        return cls.__SMALLEST_CURRENT_RATE

    @classmethod
    def MAX_CURRENT_RATE(cls):
        return cls.__MAX_CURRENT_RATE

    @classmethod
    def MIN_WITHDRAW_AMOUNT(cls):
        return cls.__MIN_WITHDRAW_AMOUNT

    @classmethod
    def MONEY_WITHDRAW_CHARGEFEE(cls):
        return cls.__MONEY_WITHDRAW_CHARGEFEE