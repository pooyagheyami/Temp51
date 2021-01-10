# In the name of God
#! /usr/bin/env python
# -*- coding: utf-8 -*-

import Database.MenuSet2 as MS
import importlib


class Mymenu(object):
    def __init__(self):
        self.MySql = MS.GetData(u'Menu2.db', u'')
        self.ToSql = MS.SetData(u'', u'')

    def program(self, itemid):
        self.handler = self.MySql.MyProg(itemid=itemid)
        return self.handler[0][1]

    def toogram(self, itolid):
        self.handler = self.MySql.MyTogr(itolid)
        return self.handler[0][1]

    def menudir(self, itemid):
        self.directory = self.MySql.MnuDir(itemid)
        return self.directory[0][0]

    def tooldir(self, itolid):
        self.directory = self.MySql.TolDir(itolid)
        return self.directory[0][0]

    def Dohndlr(self):
        return self.MySql.DoHdnl()

    def Revitm(self):
        return self.MySql.RevItem()


def DoProgram(item,MT):
    #print( item ) # Get item from menu
    M = Mymenu()

    if MT == 'M':
        p = M.program(item)
        d = M.menudir(item)
    elif MT == 'T':
        p = M.toogram(item)
        d = M.tooldir(item)

    I = M.Dohndlr()
    #print I
    Ii = []
    for it in I:
        Ii.append(it[0])
    #print Ii
    a = d+'.'+p
    #i = __import__(a,globals(),locals(),Ii,0)
    i = importlib.import_module(a)
    #print dir(i)
    #i.main()

    return i
