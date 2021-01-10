# In the name of God
# Cearte Menu main Frame File
# ! /usr/bin/env python
# -*- coding: utf-8 -*-

import Database.MenuSet2 as MS
import wx
import os
from Config.Init import *


class MainMenu():
    def __init__(self):
        self.createMenuBar()
        #M = MenuData()
        #self.m = M.menuBar()
        self.mid = 1001

    def createMenuBar(self):
        self.menuBar = wx.MenuBar()
        #self.mhand = []
        self.m = MenuData()
        for eachMenuData in self.m.menuBar():
            menuLabel = eachMenuData[1]
            menuItem = self.m.menuItem(eachMenuData[0])

            self.menuBar.Append(self.createMenu(menuItem), menuLabel)
            #if eachMenuData[3] == '31cd':
            #    print(self.menuBar)


        # print self.menuBar
        return self.menuBar

    def createMenu(self, menuData):
        self.menu = wx.Menu()
        #print(menuData)
        for eachId, eachLabel, eachStatus, shrtcut, echicon in menuData:

            if not eachLabel:
                self.menu.AppendSeparator()
                continue
            if shrtcut != None:
                itmlebl = eachLabel+u'\t'+shrtcut
            else:
                itmlebl = eachLabel
            self.menuItem = self.menu.Append(eachId, itmlebl, eachStatus)
            if echicon != None:
                self.menuItem.SetBitmap(wx.Bitmap(ICON16_PATH+echicon, wx.BITMAP_TYPE_ANY))

        # print self.menu
        return self.menu

    def createHandler(self):
        # print self.menu.GetEventHandler()
        return self.menu.GetEventHandler

    def Onmenu(self, event):
        self.mid = event.GetId()
        # print self.GetItemId()


    def GetItemId(self):

        return self.menuItem


class MenuData(object):
    def __init__(self):
        self.MySql = MS.GetData(u'Menu2.db', u'')
        self.ToSql = MS.SetData(u'', u'')

    def menuBar(self):
        self.mbar = []
        for row in self.MySql.AmenuBar():
            self.mbar.append(row)
        return self.mbar

    def menuItem(self, i):
        self.bitm = self.MySql.AmenuItm(i)
        self.mitem = []
        for itm in self.bitm:
            #print(itm)
            self.mitem.append(itm)
        # print self.mitem
        return self.mitem

    def menuDir(self):
        self.Bdir = self.MySql.DirBar()
        self.mdir = []
        for row in self.Bdir:
            self.mdir.append(row)
        # print self.mdir
        return self.mdir
