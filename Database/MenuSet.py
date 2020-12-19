#In The name of God
#!/usr/bin/env python
# -*- codnig: utf-8 -*-

from . import wxsq as sq


class GetData:
    def __init__(self, DBF, sends):
        self.DBF = DBF
        self.sends = sends

    def ShowItem(self, ibar=1):
        return sq.wxsqltxt(self.DBF, """select mitem.id,mitem.itemid,mitem.mbarid,mitem.itemname,mitem.handler
                                        from mitem
                                        where mitem.mbarid = %d
                                        """ % ibar)

    def gItem(self, mbar=1):
        return sq.wxsqltxt(self.DBF, """select mitem.itemname,mitem.itemid
                                        from mitem
                                        where mitem.mbarid = %d
                                        """ % mbar)

    def AmenuBar(self, Access=u'FFFF'):
        return sq.wxsqltxt(self.DBF, """ SELECT *
                                         FROM menubar,access
                                         where menubar.acclvlid = access.acclvlid
                                         and access.acclevl = '%s'
                                         """ % Access)

    def AmenuItm(self, barid=1):
        return sq.wxsqltxt(self.DBF, """SELECT DISTINCT mitem.itemid,mitem.itemname,mitem.status
                     FROM mitem,menubar
                     WHERE mitem.mbarid = %d
                     ORDER BY mitem.itemid  """ % barid)

    def DirBar(self):
        return sq.wxsqltxt(self.DBF, """SELECT menubar.mbardir
                                        FROM menubar
                                        """)
    def AllBar(self):
        return sq.wxsqltxt(self.DBF,"""SELECT * FROM menubar""")

    def RevItem(self):
        return sq.wxsqltxt(self.DBF,"""select mitem.itemname,mitem.itemid 
                                       from mitem
                                       where mitem.mbarid = (select menubar.mbarid
                                            from menubar
                                            where menubar.mbardir = 'GUI.Input')
        """)

    def MyProg(self,itemid=''):
        return sq.wxsqltxt(self.DBF,"""SELECT mitem.itemid, mitem.handler
            FROM mitem
            WHERE mitem.itemid = %s  """ %itemid)

    def MnuDir(self,itemid=''):
        return  sq.wxsqltxt(self.DBF, """SELECT menubar.mbardir
              FROM mitem  JOIN menubar
              ON mitem.mbarid = menubar.mbarid
              WHERE mitem.itemid =  %s  """ %itemid)

    def DoHdnl(self):
        return sq.wxsqltxt(self.DBF,"""select mitem.handler
          from mitem
          WHERE  mitem.handler  notnull """)

    def GetTB(self):
        return sq.wxsqltxt(self.DBF,"""select itemid,tbname,icondir,status,handler from toolbar """)

    def GetAllTB(self):
        return sq.wxsqltxt(self.DBF,""" select * from toolbar """)




class SetData:
    def __init__(self, send, data):
        self.send = send
        self.data = data

    def Additem(self, send, data):
        return sq.wxsqins('Menu.db', 'mitem', send, data)

    def Additem2(self, send, data):
        return sq.wxsqins2('Menu.db', 'mitem', send, data)

    def Upditem(self, send, data):
        return sq.wxsqlup('Menu.db', 'mitem', send, data)

    def Upditem2(self, send, data):
        return sq.wxsqlup2('Menu.db', 'mitem', send, data)

    def Delitem(self, data):
        return sq.wxsqdel('Menu.db', 'mitem', data)


