# uncompyle6 version 2.9.10
# Python bytecode 2.7 (62211)
# Decompiled from: Python 2.7.10 (default, Feb  6 2017, 23:53:20) 
# [GCC 4.2.1 Compatible Apple LLVM 8.0.0 (clang-800.0.34)]
# Embedded file name: type_Result.py
from types import *
import array
RESULT_UNIQUE_NAME = 0
RESULT_REGISTERED = 4
RESULT_DEREGISTERED = 5
RESULT_DUPLICATE = 6
RESULT_DUPLICATE_DEREG = 7
RESULT_GROUP_NAME = 128
RESULT_NRC_GOODRET = 0
RESULT_NRC_BUFLEN = 1
RESULT_NRC_ILLCMD = 3
RESULT_NRC_CMDTMO = 5
RESULT_NRC_INCOMP = 6
RESULT_NRC_BADDR = 7
RESULT_NRC_SNUMOUT = 8
RESULT_NRC_NORES = 9
RESULT_NRC_SCLOSED = 10
RESULT_NRC_CMDCAN = 11
RESULT_NRC_DUPNAME = 13
RESULT_NRC_NAMTFUL = 14
RESULT_NRC_ACTSES = 15
RESULT_NRC_LOCTFUL = 17
RESULT_NRC_REMTFUL = 18
RESULT_NRC_ILLNN = 19
RESULT_NRC_NOCALL = 20
RESULT_NRC_NOWILD = 21
RESULT_NRC_INUSE = 22
RESULT_NRC_NAMERR = 23
RESULT_NRC_SABORT = 24
RESULT_NRC_NAMCONF = 25
RESULT_NRC_IFBUSY = 33
RESULT_NRC_TOOMANY = 34
RESULT_NRC_BRIDGE = 35
RESULT_NRC_CANOCCR = 36
RESULT_NRC_CANCEL = 38
RESULT_NRC_DUPENV = 48
RESULT_NRC_ENVNOTDEF = 52
RESULT_NRC_OSRESNOTAV = 53
RESULT_NRC_MAXAPPS = 54
RESULT_NRC_NOSAPS = 55
RESULT_NRC_NORESOURCES = 56
RESULT_NRC_INVADDRESS = 57
RESULT_NRC_INVDDID = 59
RESULT_NRC_LOCKFAIL = 60
RESULT_NRC_OPENERR = 63
RESULT_NRC_SYSTEM = 64
RESULT_NRC_PENDING = 255

class ResultNCB:

    def __init__(self):
        self.__dict__['ncb_command'] = 0
        self.__dict__['ncb_retcode'] = 0
        self.__dict__['ncb_lsn'] = 0
        self.__dict__['ncb_num'] = 0
        self.__dict__['ncb_rto'] = 0
        self.__dict__['ncb_sto'] = 0
        self.__dict__['ncb_lana_num'] = 0
        self.__dict__['ncb_cmd_cplt'] = 0
        self.__dict__['ncb_callname'] = ''
        self.__dict__['ncb_name'] = ''

    def __getattr__(self, name):
        if name == 'ncb_command':
            return self.__dict__['ncb_command']
        if name == 'ncb_retcode':
            return self.__dict__['ncb_retcode']
        if name == 'ncb_lsn':
            return self.__dict__['ncb_lsn']
        if name == 'ncb_num':
            return self.__dict__['ncb_num']
        if name == 'ncb_rto':
            return self.__dict__['ncb_rto']
        if name == 'ncb_sto':
            return self.__dict__['ncb_sto']
        if name == 'ncb_lana_num':
            return self.__dict__['ncb_lana_num']
        if name == 'ncb_cmd_cplt':
            return self.__dict__['ncb_cmd_cplt']
        if name == 'ncb_callname':
            return self.__dict__['ncb_callname']
        if name == 'ncb_name':
            return self.__dict__['ncb_name']
        raise AttributeError("Attribute '%s' not found" % name)

    def __setattr__(self, name, value):
        if name == 'ncb_command':
            self.__dict__['ncb_command'] = value
        elif name == 'ncb_retcode':
            self.__dict__['ncb_retcode'] = value
        elif name == 'ncb_lsn':
            self.__dict__['ncb_lsn'] = value
        elif name == 'ncb_num':
            self.__dict__['ncb_num'] = value
        elif name == 'ncb_rto':
            self.__dict__['ncb_rto'] = value
        elif name == 'ncb_sto':
            self.__dict__['ncb_sto'] = value
        elif name == 'ncb_lana_num':
            self.__dict__['ncb_lana_num'] = value
        elif name == 'ncb_cmd_cplt':
            self.__dict__['ncb_cmd_cplt'] = value
        elif name == 'ncb_callname':
            self.__dict__['ncb_callname'] = value
        elif name == 'ncb_name':
            self.__dict__['ncb_name'] = value
        else:
            raise AttributeError("Attribute '%s' not found" % name)

    def Marshal(self, mmsg):
        from mcl.object.Message import MarshalMessage
        submsg = MarshalMessage()
        submsg.AddU8(MSG_KEY_RESULT_NCB_COMMAND, self.__dict__['ncb_command'])
        submsg.AddU8(MSG_KEY_RESULT_NCB_RETCODE, self.__dict__['ncb_retcode'])
        submsg.AddU8(MSG_KEY_RESULT_NCB_LSN, self.__dict__['ncb_lsn'])
        submsg.AddU8(MSG_KEY_RESULT_NCB_NUM, self.__dict__['ncb_num'])
        submsg.AddU8(MSG_KEY_RESULT_NCB_RTO, self.__dict__['ncb_rto'])
        submsg.AddU8(MSG_KEY_RESULT_NCB_STO, self.__dict__['ncb_sto'])
        submsg.AddU8(MSG_KEY_RESULT_NCB_LANA_NUM, self.__dict__['ncb_lana_num'])
        submsg.AddU8(MSG_KEY_RESULT_NCB_CMD_CPLT, self.__dict__['ncb_cmd_cplt'])
        submsg.AddStringUtf8(MSG_KEY_RESULT_NCB_CALLNAME, self.__dict__['ncb_callname'])
        submsg.AddStringUtf8(MSG_KEY_RESULT_NCB_NAME, self.__dict__['ncb_name'])
        mmsg.AddMessage(MSG_KEY_RESULT_NCB, submsg)

    def Demarshal(self, dmsg, instance=-1):
        import mcl.object.Message
        msgData = dmsg.FindData(MSG_KEY_RESULT_NCB, mcl.object.Message.MSG_TYPE_MSG, instance)
        submsg = mcl.object.Message.DemarshalMessage(msgData)
        self.__dict__['ncb_command'] = submsg.FindU8(MSG_KEY_RESULT_NCB_COMMAND)
        self.__dict__['ncb_retcode'] = submsg.FindU8(MSG_KEY_RESULT_NCB_RETCODE)
        self.__dict__['ncb_lsn'] = submsg.FindU8(MSG_KEY_RESULT_NCB_LSN)
        self.__dict__['ncb_num'] = submsg.FindU8(MSG_KEY_RESULT_NCB_NUM)
        self.__dict__['ncb_rto'] = submsg.FindU8(MSG_KEY_RESULT_NCB_RTO)
        self.__dict__['ncb_sto'] = submsg.FindU8(MSG_KEY_RESULT_NCB_STO)
        self.__dict__['ncb_lana_num'] = submsg.FindU8(MSG_KEY_RESULT_NCB_LANA_NUM)
        self.__dict__['ncb_cmd_cplt'] = submsg.FindU8(MSG_KEY_RESULT_NCB_CMD_CPLT)
        self.__dict__['ncb_callname'] = submsg.FindString(MSG_KEY_RESULT_NCB_CALLNAME)
        self.__dict__['ncb_name'] = submsg.FindString(MSG_KEY_RESULT_NCB_NAME)


class ResultAdapter:

    def __init__(self):
        self.__dict__['adapter_address'] = array.array('B')
        i = 0
        while i < 6:
            self.__dict__['adapter_address'].append(0)
            i = i + 1

        self.__dict__['adapter_type'] = 0
        self.__dict__['rev_major'] = 0
        self.__dict__['rev_minor'] = 0
        self.__dict__['duration'] = 0
        self.__dict__['name_count'] = 0
        self.__dict__['frmr_recv'] = 0
        self.__dict__['frmr_xmit'] = 0
        self.__dict__['iframe_recv_err'] = 0
        self.__dict__['xmit_aborts'] = 0
        self.__dict__['xmit_success'] = 0
        self.__dict__['recv_success'] = 0
        self.__dict__['iframe_xmit_err'] = 0
        self.__dict__['recv_buff_unavail'] = 0
        self.__dict__['t1_timeouts'] = 0
        self.__dict__['ti_timeouts'] = 0
        self.__dict__['free_ncbs'] = 0
        self.__dict__['max_dgram_size'] = 0
        self.__dict__['max_sess_pkt_size'] = 0
        self.__dict__['pending_sess'] = 0
        self.__dict__['max_cfg_sess'] = 0
        self.__dict__['max_cfg_ncbs'] = 0
        self.__dict__['max_ncbs'] = 0
        self.__dict__['xmit_buf_unavail'] = 0
        self.__dict__['max_sess'] = 0

    def __getattr__(self, name):
        if name == 'adapter_address':
            return self.__dict__['adapter_address']
        if name == 'adapter_type':
            return self.__dict__['adapter_type']
        if name == 'rev_major':
            return self.__dict__['rev_major']
        if name == 'rev_minor':
            return self.__dict__['rev_minor']
        if name == 'duration':
            return self.__dict__['duration']
        if name == 'name_count':
            return self.__dict__['name_count']
        if name == 'frmr_recv':
            return self.__dict__['frmr_recv']
        if name == 'frmr_xmit':
            return self.__dict__['frmr_xmit']
        if name == 'iframe_recv_err':
            return self.__dict__['iframe_recv_err']
        if name == 'xmit_aborts':
            return self.__dict__['xmit_aborts']
        if name == 'xmit_success':
            return self.__dict__['xmit_success']
        if name == 'recv_success':
            return self.__dict__['recv_success']
        if name == 'iframe_xmit_err':
            return self.__dict__['iframe_xmit_err']
        if name == 'recv_buff_unavail':
            return self.__dict__['recv_buff_unavail']
        if name == 't1_timeouts':
            return self.__dict__['t1_timeouts']
        if name == 'ti_timeouts':
            return self.__dict__['ti_timeouts']
        if name == 'free_ncbs':
            return self.__dict__['free_ncbs']
        if name == 'max_dgram_size':
            return self.__dict__['max_dgram_size']
        if name == 'max_sess_pkt_size':
            return self.__dict__['max_sess_pkt_size']
        if name == 'pending_sess':
            return self.__dict__['pending_sess']
        if name == 'max_cfg_sess':
            return self.__dict__['max_cfg_sess']
        if name == 'max_cfg_ncbs':
            return self.__dict__['max_cfg_ncbs']
        if name == 'max_ncbs':
            return self.__dict__['max_ncbs']
        if name == 'xmit_buf_unavail':
            return self.__dict__['xmit_buf_unavail']
        if name == 'max_sess':
            return self.__dict__['max_sess']
        raise AttributeError("Attribute '%s' not found" % name)

    def __setattr__(self, name, value):
        if name == 'adapter_address':
            self.__dict__['adapter_address'] = value
        elif name == 'adapter_type':
            self.__dict__['adapter_type'] = value
        elif name == 'rev_major':
            self.__dict__['rev_major'] = value
        elif name == 'rev_minor':
            self.__dict__['rev_minor'] = value
        elif name == 'duration':
            self.__dict__['duration'] = value
        elif name == 'name_count':
            self.__dict__['name_count'] = value
        elif name == 'frmr_recv':
            self.__dict__['frmr_recv'] = value
        elif name == 'frmr_xmit':
            self.__dict__['frmr_xmit'] = value
        elif name == 'iframe_recv_err':
            self.__dict__['iframe_recv_err'] = value
        elif name == 'xmit_aborts':
            self.__dict__['xmit_aborts'] = value
        elif name == 'xmit_success':
            self.__dict__['xmit_success'] = value
        elif name == 'recv_success':
            self.__dict__['recv_success'] = value
        elif name == 'iframe_xmit_err':
            self.__dict__['iframe_xmit_err'] = value
        elif name == 'recv_buff_unavail':
            self.__dict__['recv_buff_unavail'] = value
        elif name == 't1_timeouts':
            self.__dict__['t1_timeouts'] = value
        elif name == 'ti_timeouts':
            self.__dict__['ti_timeouts'] = value
        elif name == 'free_ncbs':
            self.__dict__['free_ncbs'] = value
        elif name == 'max_dgram_size':
            self.__dict__['max_dgram_size'] = value
        elif name == 'max_sess_pkt_size':
            self.__dict__['max_sess_pkt_size'] = value
        elif name == 'pending_sess':
            self.__dict__['pending_sess'] = value
        elif name == 'max_cfg_sess':
            self.__dict__['max_cfg_sess'] = value
        elif name == 'max_cfg_ncbs':
            self.__dict__['max_cfg_ncbs'] = value
        elif name == 'max_ncbs':
            self.__dict__['max_ncbs'] = value
        elif name == 'xmit_buf_unavail':
            self.__dict__['xmit_buf_unavail'] = value
        elif name == 'max_sess':
            self.__dict__['max_sess'] = value
        else:
            raise AttributeError("Attribute '%s' not found" % name)

    def Marshal(self, mmsg):
        from mcl.object.Message import MarshalMessage
        submsg = MarshalMessage()
        submsg.AddData(MSG_KEY_RESULT_ADAPTER_ADDRESS, self.__dict__['adapter_address'])
        submsg.AddU8(MSG_KEY_RESULT_ADAPTER_TYPE, self.__dict__['adapter_type'])
        submsg.AddU8(MSG_KEY_RESULT_ADAPTER_REV_MAJOR, self.__dict__['rev_major'])
        submsg.AddU8(MSG_KEY_RESULT_ADAPTER_REV_MINOR, self.__dict__['rev_minor'])
        submsg.AddU16(MSG_KEY_RESULT_ADAPTER_DURATION, self.__dict__['duration'])
        submsg.AddU16(MSG_KEY_RESULT_ADAPTER_NAME_COUNT, self.__dict__['name_count'])
        submsg.AddU16(MSG_KEY_RESULT_ADAPTER_FRMR_RECV, self.__dict__['frmr_recv'])
        submsg.AddU16(MSG_KEY_RESULT_ADAPTER_FRMR_XMIT, self.__dict__['frmr_xmit'])
        submsg.AddU16(MSG_KEY_RESULT_ADAPTER_IFRAME_RECV_ERR, self.__dict__['iframe_recv_err'])
        submsg.AddU16(MSG_KEY_RESULT_ADAPTER_XMIT_ABORTS, self.__dict__['xmit_aborts'])
        submsg.AddU32(MSG_KEY_RESULT_ADAPTER_XMIT_SUCCESS, self.__dict__['xmit_success'])
        submsg.AddU32(MSG_KEY_RESULT_ADAPTER_RECV_SUCCESS, self.__dict__['recv_success'])
        submsg.AddU16(MSG_KEY_RESULT_ADAPTER_IFRAME_XMIT_ERR, self.__dict__['iframe_xmit_err'])
        submsg.AddU16(MSG_KEY_RESULT_ADAPTER_RECV_BUFF_UNAVAIL, self.__dict__['recv_buff_unavail'])
        submsg.AddU16(MSG_KEY_RESULT_ADAPTER_T1_TIMEOUTS, self.__dict__['t1_timeouts'])
        submsg.AddU16(MSG_KEY_RESULT_ADAPTER_TI_TIMEOUTS, self.__dict__['ti_timeouts'])
        submsg.AddU16(MSG_KEY_RESULT_ADAPTER_FREE_NCBS, self.__dict__['free_ncbs'])
        submsg.AddU16(MSG_KEY_RESULT_ADAPTER_MAX_DGRAM_SIZE, self.__dict__['max_dgram_size'])
        submsg.AddU16(MSG_KEY_RESULT_ADAPTER_MAX_SESS_PKT_SIZE, self.__dict__['max_sess_pkt_size'])
        submsg.AddU16(MSG_KEY_RESULT_ADAPTER_PENDING_SESS, self.__dict__['pending_sess'])
        submsg.AddU16(MSG_KEY_RESULT_ADAPTER_MAX_CFG_SESS, self.__dict__['max_cfg_sess'])
        submsg.AddU16(MSG_KEY_RESULT_ADAPTER_MAX_CFG_NCBS, self.__dict__['max_cfg_ncbs'])
        submsg.AddU16(MSG_KEY_RESULT_ADAPTER_MAX_NCBS, self.__dict__['max_ncbs'])
        submsg.AddU16(MSG_KEY_RESULT_ADAPTER_XMIT_BUF_UNAVAIL, self.__dict__['xmit_buf_unavail'])
        submsg.AddU16(MSG_KEY_RESULT_ADAPTER_MAX_SESS, self.__dict__['max_sess'])
        mmsg.AddMessage(MSG_KEY_RESULT_ADAPTER, submsg)

    def Demarshal(self, dmsg, instance=-1):
        import mcl.object.Message
        msgData = dmsg.FindData(MSG_KEY_RESULT_ADAPTER, mcl.object.Message.MSG_TYPE_MSG, instance)
        submsg = mcl.object.Message.DemarshalMessage(msgData)
        self.__dict__['adapter_address'] = submsg.FindData(MSG_KEY_RESULT_ADAPTER_ADDRESS)
        self.__dict__['adapter_type'] = submsg.FindU8(MSG_KEY_RESULT_ADAPTER_TYPE)
        self.__dict__['rev_major'] = submsg.FindU8(MSG_KEY_RESULT_ADAPTER_REV_MAJOR)
        self.__dict__['rev_minor'] = submsg.FindU8(MSG_KEY_RESULT_ADAPTER_REV_MINOR)
        self.__dict__['duration'] = submsg.FindU16(MSG_KEY_RESULT_ADAPTER_DURATION)
        self.__dict__['name_count'] = submsg.FindU16(MSG_KEY_RESULT_ADAPTER_NAME_COUNT)
        self.__dict__['frmr_recv'] = submsg.FindU16(MSG_KEY_RESULT_ADAPTER_FRMR_RECV)
        self.__dict__['frmr_xmit'] = submsg.FindU16(MSG_KEY_RESULT_ADAPTER_FRMR_XMIT)
        self.__dict__['iframe_recv_err'] = submsg.FindU16(MSG_KEY_RESULT_ADAPTER_IFRAME_RECV_ERR)
        self.__dict__['xmit_aborts'] = submsg.FindU16(MSG_KEY_RESULT_ADAPTER_XMIT_ABORTS)
        self.__dict__['xmit_success'] = submsg.FindU32(MSG_KEY_RESULT_ADAPTER_XMIT_SUCCESS)
        self.__dict__['recv_success'] = submsg.FindU32(MSG_KEY_RESULT_ADAPTER_RECV_SUCCESS)
        self.__dict__['iframe_xmit_err'] = submsg.FindU16(MSG_KEY_RESULT_ADAPTER_IFRAME_XMIT_ERR)
        self.__dict__['recv_buff_unavail'] = submsg.FindU16(MSG_KEY_RESULT_ADAPTER_RECV_BUFF_UNAVAIL)
        self.__dict__['t1_timeouts'] = submsg.FindU16(MSG_KEY_RESULT_ADAPTER_T1_TIMEOUTS)
        self.__dict__['ti_timeouts'] = submsg.FindU16(MSG_KEY_RESULT_ADAPTER_TI_TIMEOUTS)
        self.__dict__['free_ncbs'] = submsg.FindU16(MSG_KEY_RESULT_ADAPTER_FREE_NCBS)
        self.__dict__['max_dgram_size'] = submsg.FindU16(MSG_KEY_RESULT_ADAPTER_MAX_DGRAM_SIZE)
        self.__dict__['max_sess_pkt_size'] = submsg.FindU16(MSG_KEY_RESULT_ADAPTER_MAX_SESS_PKT_SIZE)
        self.__dict__['pending_sess'] = submsg.FindU16(MSG_KEY_RESULT_ADAPTER_PENDING_SESS)
        self.__dict__['max_cfg_sess'] = submsg.FindU16(MSG_KEY_RESULT_ADAPTER_MAX_CFG_SESS)
        self.__dict__['max_cfg_ncbs'] = submsg.FindU16(MSG_KEY_RESULT_ADAPTER_MAX_CFG_NCBS)
        self.__dict__['max_ncbs'] = submsg.FindU16(MSG_KEY_RESULT_ADAPTER_MAX_NCBS)
        self.__dict__['xmit_buf_unavail'] = submsg.FindU16(MSG_KEY_RESULT_ADAPTER_XMIT_BUF_UNAVAIL)
        self.__dict__['max_sess'] = submsg.FindU16(MSG_KEY_RESULT_ADAPTER_MAX_SESS)


class ResultStatus:

    def __init__(self):
        self.__dict__['status'] = 0
        self.__dict__['errType'] = 0
        self.__dict__['rtnCode'] = 0

    def __getattr__(self, name):
        if name == 'status':
            return self.__dict__['status']
        if name == 'errType':
            return self.__dict__['errType']
        if name == 'rtnCode':
            return self.__dict__['rtnCode']
        raise AttributeError("Attribute '%s' not found" % name)

    def __setattr__(self, name, value):
        if name == 'status':
            self.__dict__['status'] = value
        elif name == 'errType':
            self.__dict__['errType'] = value
        elif name == 'rtnCode':
            self.__dict__['rtnCode'] = value
        else:
            raise AttributeError("Attribute '%s' not found" % name)

    def Marshal(self, mmsg):
        from mcl.object.Message import MarshalMessage
        submsg = MarshalMessage()
        submsg.AddU32(MSG_KEY_RESULT_STATUS_STATUS, self.__dict__['status'])
        submsg.AddU32(MSG_KEY_RESULT_STATUS_ERR_TYPE, self.__dict__['errType'])
        submsg.AddU32(MSG_KEY_RESULT_STATUS_RTN_CODE, self.__dict__['rtnCode'])
        mmsg.AddMessage(MSG_KEY_RESULT_STATUS, submsg)

    def Demarshal(self, dmsg, instance=-1):
        import mcl.object.Message
        msgData = dmsg.FindData(MSG_KEY_RESULT_STATUS, mcl.object.Message.MSG_TYPE_MSG, instance)
        submsg = mcl.object.Message.DemarshalMessage(msgData)
        self.__dict__['status'] = submsg.FindU32(MSG_KEY_RESULT_STATUS_STATUS)
        self.__dict__['errType'] = submsg.FindU32(MSG_KEY_RESULT_STATUS_ERR_TYPE)
        self.__dict__['rtnCode'] = submsg.FindU32(MSG_KEY_RESULT_STATUS_RTN_CODE)


class ResultName:

    def __init__(self):
        self.__dict__['type'] = 0
        self.__dict__['nameFlags'] = 0
        self.__dict__['networkName'] = ''

    def __getattr__(self, name):
        if name == 'type':
            return self.__dict__['type']
        if name == 'nameFlags':
            return self.__dict__['nameFlags']
        if name == 'networkName':
            return self.__dict__['networkName']
        raise AttributeError("Attribute '%s' not found" % name)

    def __setattr__(self, name, value):
        if name == 'type':
            self.__dict__['type'] = value
        elif name == 'nameFlags':
            self.__dict__['nameFlags'] = value
        elif name == 'networkName':
            self.__dict__['networkName'] = value
        else:
            raise AttributeError("Attribute '%s' not found" % name)

    def Marshal(self, mmsg):
        from mcl.object.Message import MarshalMessage
        submsg = MarshalMessage()
        submsg.AddU8(MSG_KEY_RESULT_NAME_TYPE, self.__dict__['type'])
        submsg.AddU8(MSG_KEY_RESULT_NAME_FLAGS, self.__dict__['nameFlags'])
        submsg.AddStringUtf8(MSG_KEY_RESULT_NAME_NETWORK_NAME, self.__dict__['networkName'])
        mmsg.AddMessage(MSG_KEY_RESULT_NAME, submsg)

    def Demarshal(self, dmsg, instance=-1):
        import mcl.object.Message
        msgData = dmsg.FindData(MSG_KEY_RESULT_NAME, mcl.object.Message.MSG_TYPE_MSG, instance)
        submsg = mcl.object.Message.DemarshalMessage(msgData)
        self.__dict__['type'] = submsg.FindU8(MSG_KEY_RESULT_NAME_TYPE)
        self.__dict__['nameFlags'] = submsg.FindU8(MSG_KEY_RESULT_NAME_FLAGS)
        self.__dict__['networkName'] = submsg.FindString(MSG_KEY_RESULT_NAME_NETWORK_NAME)