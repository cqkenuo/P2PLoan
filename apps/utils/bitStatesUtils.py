# coding=gbk

#Լ��  GET������ͷ��ֻ���𷵻�����
      # ������Ա�������𷵻����ݣ������������ݿ��״̬λ

class BitStatesUtils:
    __OP_BIND_PHONE = 1 << 0# �û����ֻ�״̬��
    __OP_BIND_EMAIL = 1 <<1# �û�������
    __OP_BASIC_INFO = 1 <<2# �û��Ƿ���д��������
    __OP_REAL_AUTH = 1 <<3# �û��Ƿ�ʵ����֤
    __OP_VEDIO_AUTH = 1 <<4# �û��Ƿ���Ƶ��֤
    __OP_HAS_BIDREQUEST_PROCESS = 1 <<5# �û��Ƿ���һ��������ڴ������̵���
    __OP_BIND_BANKINFO = 1 <<6# �û��Ƿ�����п�
    __OP_HAS_MONEYWITHDRAW_PROCESS = 1 <<7 # �û��Ƿ���һ�����������ڴ�����

    #��̨���״̬��Ϣ

    __STATE_NORMAL = 0 # ����
    __STATE_AUDIT = 1 # ���ͨ��
    __STATE_REJECT = 2 # ��˾ܾ�


    @classmethod
    def GET_OP_BIND_PHONE(cls):
        return cls.__OP_BIND_PHONE

    @classmethod
    def GET_OP_BIND_EMAIL(cls):
        return cls.__OP_BIND_EMAIL

    @classmethod
    def GET_OP_BASIC_INFO(cls):
        return cls.__OP_BASIC_INFO

    @classmethod
    def GET_OP_REAL_AUTH(cls):
        return cls.__OP_REAL_AUTH

    @classmethod
    def GET_OP_VEDIO_AUTH(cls):
        return cls.__OP_VEDIO_AUTH

    @classmethod
    def GET_OP_HAS_BIDREQUEST_PROCESS(cls):
        return cls.__OP_HAS_BIDREQUEST_PROCESS

    @classmethod
    def GET_OP_BIND_BANKINFO(cls):
        return cls.__OP_BIND_BANKINFO

    @classmethod
    def GET_HAS_MONEYWITHDRAW_PROCESS(cls):
        return cls.__OP_HAS_MONEYWITHDRAW_PROCESS

    @classmethod
    def STATE_NORMAL(cls):
        return cls.__STATE_NORMAL
    @classmethod
    def STATE_AUDIT(cls):
        return cls.__STATE_AUDIT
    @classmethod
    def STATE_REJECT(cls):
        return cls.__STATE_REJECT

    # / **
    # * @ param
    # states
    # *����״ֵ̬
    # * @ param
    # value
    # *��Ҫ�ж�״ֵ̬
    # * @ return �Ƿ����
    # * /
    @classmethod
    def hasState(cls, states, value):
        return (states & value !=0)

    # / **
    # * @ param
    # states
    # *����״ֵ̬
    # * @ param
    # value
    # *��Ҫ���״ֵ̬
    # * @ return �µ�״ֵ̬
    # * /
    @classmethod
    def addState(cls, states, value):
        if BitStatesUtils.hasState(states, value):
            return states
        return (states | value)

    # / **
    # * @ param
    # states
    # *����״ֵ̬
    # * @ param
    # value
    # *��Ҫɾ��״ֵ̬
    # * @ return �µ�״ֵ̬
    # * /
    @classmethod
    def removeState(cls, states, value):
        if not BitStatesUtils.removeState(states, value):
            return states
        return states ^ value



