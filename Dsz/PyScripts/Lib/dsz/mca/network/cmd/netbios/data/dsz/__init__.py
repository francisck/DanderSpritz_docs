# uncompyle6 version 2.9.10
# Python bytecode 2.7 (62211)
# Decompiled from: Python 2.7.10 (default, Feb  6 2017, 23:53:20) 
# [GCC 4.2.1 Compatible Apple LLVM 8.0.0 (clang-800.0.34)]
# Embedded file name: __init__.py
import dsz
import dsz.cmd
import dsz.data
import dsz.lp

class Netbios(dsz.data.Task):

    def __init__(self, cmd=None):
        dsz.data.Task.__init__(self, cmd)

    def _LoadData(self):
        self.NetBios = list()
        try:
            for x in dsz.cmd.data.Get('NetBios', dsz.TYPE_OBJECT):
                self.NetBios.append(Netbios.NetBios(x))

        except:
            pass

    class NetBios(dsz.data.DataBean):

        def __init__(self, obj):
            self.Adapter = list()
            try:
                for x in dsz.cmd.data.ObjectGet(obj, 'Adapter', dsz.TYPE_OBJECT):
                    self.Adapter.append(Netbios.NetBios.Adapter(x))

            except:
                pass

            try:
                self.NCB = Netbios.NetBios.NCB(dsz.cmd.data.ObjectGet(obj, 'NCB', dsz.TYPE_OBJECT)[0])
            except:
                self.NCB = None

            return

        class Adapter(dsz.data.DataBean):

            def __init__(self, obj):
                try:
                    self.recv_buff_unavail = dsz.cmd.data.ObjectGet(obj, 'recv_buff_unavail', dsz.TYPE_INT)[0]
                except:
                    self.recv_buff_unavail = None

                try:
                    self.max_cfg_sess = dsz.cmd.data.ObjectGet(obj, 'max_cfg_sess', dsz.TYPE_INT)[0]
                except:
                    self.max_cfg_sess = None

                try:
                    self.t1_timeouts = dsz.cmd.data.ObjectGet(obj, 't1_timeouts', dsz.TYPE_INT)[0]
                except:
                    self.t1_timeouts = None

                try:
                    self.pending_sess = dsz.cmd.data.ObjectGet(obj, 'pending_sess', dsz.TYPE_INT)[0]
                except:
                    self.pending_sess = None

                try:
                    self.iframe_recv_err = dsz.cmd.data.ObjectGet(obj, 'iframe_recv_err', dsz.TYPE_INT)[0]
                except:
                    self.iframe_recv_err = None

                try:
                    self.xmit_aborts = dsz.cmd.data.ObjectGet(obj, 'xmit_aborts', dsz.TYPE_INT)[0]
                except:
                    self.xmit_aborts = None

                try:
                    self.max_sess = dsz.cmd.data.ObjectGet(obj, 'max_sess', dsz.TYPE_INT)[0]
                except:
                    self.max_sess = None

                try:
                    self.max_dgram_size = dsz.cmd.data.ObjectGet(obj, 'max_dgram_size', dsz.TYPE_INT)[0]
                except:
                    self.max_dgram_size = None

                try:
                    self.frmr_recv = dsz.cmd.data.ObjectGet(obj, 'frmr_recv', dsz.TYPE_INT)[0]
                except:
                    self.frmr_recv = None

                try:
                    self.xmit_buff_unavail = dsz.cmd.data.ObjectGet(obj, 'xmit_buff_unavail', dsz.TYPE_INT)[0]
                except:
                    self.xmit_buff_unavail = None

                try:
                    self.recv_success = dsz.cmd.data.ObjectGet(obj, 'recv_success', dsz.TYPE_INT)[0]
                except:
                    self.recv_success = None

                try:
                    self.frmr_xmit = dsz.cmd.data.ObjectGet(obj, 'frmr_xmit', dsz.TYPE_INT)[0]
                except:
                    self.frmr_xmit = None

                try:
                    self.xmit_success = dsz.cmd.data.ObjectGet(obj, 'xmit_success', dsz.TYPE_INT)[0]
                except:
                    self.xmit_success = None

                try:
                    self.name_count = dsz.cmd.data.ObjectGet(obj, 'name_count', dsz.TYPE_INT)[0]
                except:
                    self.name_count = None

                try:
                    self.max_cfg_ncbs = dsz.cmd.data.ObjectGet(obj, 'max_cfg_ncbs', dsz.TYPE_INT)[0]
                except:
                    self.max_cfg_ncbs = None

                try:
                    self.ti_timeouts = dsz.cmd.data.ObjectGet(obj, 'ti_timeouts', dsz.TYPE_INT)[0]
                except:
                    self.ti_timeouts = None

                try:
                    self.max_ncbs = dsz.cmd.data.ObjectGet(obj, 'max_ncbs', dsz.TYPE_INT)[0]
                except:
                    self.max_ncbs = None

                try:
                    self.duration = dsz.cmd.data.ObjectGet(obj, 'duration', dsz.TYPE_INT)[0]
                except:
                    self.duration = None

                try:
                    self.free_ncbs = dsz.cmd.data.ObjectGet(obj, 'free_ncbs', dsz.TYPE_INT)[0]
                except:
                    self.free_ncbs = None

                try:
                    self.iframe_xmit_err = dsz.cmd.data.ObjectGet(obj, 'iframe_xmit_err', dsz.TYPE_INT)[0]
                except:
                    self.iframe_xmit_err = None

                try:
                    self.max_sess_pkt_size = dsz.cmd.data.ObjectGet(obj, 'max_sess_pkt_size', dsz.TYPE_INT)[0]
                except:
                    self.max_sess_pkt_size = None

                try:
                    self.adapter_type = dsz.cmd.data.ObjectGet(obj, 'adapter_type', dsz.TYPE_STRING)[0]
                except:
                    self.adapter_type = None

                try:
                    self.release = dsz.cmd.data.ObjectGet(obj, 'release', dsz.TYPE_STRING)[0]
                except:
                    self.release = None

                try:
                    self.adapter_addr = dsz.cmd.data.ObjectGet(obj, 'adapter_addr', dsz.TYPE_STRING)[0]
                except:
                    self.adapter_addr = None

                self.names = list()
                try:
                    for x in dsz.cmd.data.ObjectGet(obj, 'names', dsz.TYPE_OBJECT):
                        self.names.append(Netbios.NetBios.Adapter.names(x))

                except:
                    pass

                return

            class names(dsz.data.DataBean):

                def __init__(self, obj):
                    try:
                        self.type = dsz.cmd.data.ObjectGet(obj, 'type', dsz.TYPE_STRING)[0]
                    except:
                        self.type = None

                    try:
                        self.netname = dsz.cmd.data.ObjectGet(obj, 'netname', dsz.TYPE_STRING)[0]
                    except:
                        self.netname = None

                    try:
                        self.name = dsz.cmd.data.ObjectGet(obj, 'name', dsz.TYPE_STRING)[0]
                    except:
                        self.name = None

                    return

        class NCB(dsz.data.DataBean):

            def __init__(self, obj):
                try:
                    self.ncb_rto = dsz.cmd.data.ObjectGet(obj, 'ncb_rto', dsz.TYPE_INT)[0]
                except:
                    self.ncb_rto = None

                try:
                    self.ncb_num = dsz.cmd.data.ObjectGet(obj, 'ncb_num', dsz.TYPE_INT)[0]
                except:
                    self.ncb_num = None

                try:
                    self.ncb_retcode = dsz.cmd.data.ObjectGet(obj, 'ncb_retcode', dsz.TYPE_INT)[0]
                except:
                    self.ncb_retcode = None

                try:
                    self.ncb_lana_num = dsz.cmd.data.ObjectGet(obj, 'ncb_lana_num', dsz.TYPE_INT)[0]
                except:
                    self.ncb_lana_num = None

                try:
                    self.ncb_sto = dsz.cmd.data.ObjectGet(obj, 'ncb_sto', dsz.TYPE_INT)[0]
                except:
                    self.ncb_sto = None

                try:
                    self.ncb_command = dsz.cmd.data.ObjectGet(obj, 'ncb_command', dsz.TYPE_INT)[0]
                except:
                    self.ncb_command = None

                try:
                    self.ncb_cmd_cplt = dsz.cmd.data.ObjectGet(obj, 'ncb_cmd_cplt', dsz.TYPE_INT)[0]
                except:
                    self.ncb_cmd_cplt = None

                try:
                    self.ncb_lsn = dsz.cmd.data.ObjectGet(obj, 'ncb_lsn', dsz.TYPE_INT)[0]
                except:
                    self.ncb_lsn = None

                try:
                    self.ncbname = dsz.cmd.data.ObjectGet(obj, 'ncbname', dsz.TYPE_STRING)[0]
                except:
                    self.ncbname = None

                try:
                    self.callname = dsz.cmd.data.ObjectGet(obj, 'callname', dsz.TYPE_STRING)[0]
                except:
                    self.callname = None

                return


dsz.data.RegisterCommand('Netbios', Netbios)
NETBIOS = Netbios
netbios = Netbios