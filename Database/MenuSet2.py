#In The name of God
#!/usr/bin/env python
# -*- codnig: utf-8 -*-

from . import wxsq as sq


class GetData:
    def __init__(self, DBF, sends):
        self.DBF = DBF
        self.sends = sends

    def ShowItem(self, ibar=1):
        return sq.wxsqltxt(self.DBF, """select mitem.extid, mitem.itemid,mitem.mbarid,mitem.itemname,handler.prgname
                                        from mitem
                                        left join handler on handler.handlerid = mitem.handlerid
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
                                         and access.acclvl = '%s'
                                         """ % Access)

    def AmenuItm(self, barid=101):
        return sq.wxsqltxt(self.DBF, """SELECT DISTINCT mitem.itemid,mitem.itemname,extended.status,extended.shortcut,extended.icon,mitem.itemtyp
                     FROM mitem
                     left join extended on mitem.extid = extended.extid
                     WHERE mitem.mbarid = %d
                       """ % barid)  #ORDER BY mitem.itemid

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
        return sq.wxsqltxt(self.DBF,"""SELECT distinct mitem.handlerid, handler.prgname
            FROM mitem join handler on mitem.handlerid = handler.handlerid
            WHERE mitem.itemid = %s  """ %itemid)

    def MnuDir(self,itemid=''):
        return  sq.wxsqltxt(self.DBF, """SELECT menubar.mbardir
              FROM mitem  JOIN menubar
              ON mitem.mbarid = menubar.mbarid
              WHERE mitem.itemid =  %s  """ %itemid)

    def SubDir(self,itemsub=''):
        return sq.wxsqltxt(self.DBF, """SELECT handler.prgdir
              FROM mitem  JOIN handler
              ON mitem.handlerid = handler.handlerid
              WHERE mitem.itemid = %s  """ %itemsub)

    def DoHdnl(self):
        return sq.wxsqltxt(self.DBF,"""select handler.prgname
          from handler join mitem on mitem.handlerid = handler.handlerid
          WHERE  mitem.handlerid  notnull """)

    def GetTB(self):
        return sq.wxsqltxt(self.DBF,"""select toolbar.toolid,toolbar.toolname,toolbar.toolicon,toolbar.shrttxt,handler.prgname 
                                       from toolbar left join handler
                                       on toolbar.handlerid = handler.handlerid """)

    def GetAllTB(self):
        return sq.wxsqltxt(self.DBF,""" select * from toolbar """)

    def MyTogr(self,itolid=''):
        return sq.wxsqltxt(self.DBF,"""SELECT distinct toolbar.handlerid, handler.prgname
            FROM toolbar join handler on toolbar.handlerid = handler.handlerid
            WHERE toolbar.toolid = %s  """ %itolid)

    def TolDir(self,itolid=''):
        return sq.wxsqltxt(self.DBF, """ select distinct menubar.mbardir , mitem.handlerid
            from menubar, toolbar  inner join mitem on mitem.handlerid = toolbar.handlerid
            where menubar.mbarid = mitem.mbarid
            and toolbar.toolid =  %s  """ % itolid)
    def Acclvl(self,accid=''):
        return sq.wxsqltxt(self.DBF, """ select * from access where access.acclvlid = '%s' """ % accid)
    def gBarItm(self,mbar=''):
        return  sq.wxsqltxt(self.DBF,""" select distinct mitem.mbarid , mitem.itemid , mitem.extid 
                                     from mitem,extended 
                                     where mitem.mbarid = %s""" % mbar)




class SetData:
    def __init__(self, field,send, data):
        self.field = field
        self.send = send
        self.data = data

    def Additem(self, send, data):
        return sq.wxsqins('Menu2.db', self.field, send, data)

    def Additem2(self, send, data):
        return sq.wxsqins2('Menu2.db', self.field, send, data)

    def Upditem(self, send, data):
        return sq.wxsqlup('Menu2.db', self.field, send, data)

    def Upditem2(self, send, data):
        return sq.wxsqlup2('Menu2.db', self.field, send, data)

    def Delitem(self, data):
        return sq.wxsqdel('Menu2.db', self.field, data)


