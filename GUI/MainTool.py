# In the name of God
# Cearte Menu main Frame File
#! /usr/bin/env python
# -*- coding: utf-8 -*-

import Database.MenuSet as MS
import wx
import wx.aui

import os
from  Config.Init import *


class MainToolAui():
    def __init__(self,parent):
        #self.myTool = wx.aui.AuiToolBar( parent, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.aui.AUI_TB_HORZ_LAYOUT )
        self.myTool = wx.ToolBar(parent, -1, wx.DefaultPosition, wx.DefaultSize, wx.TB_FLAT | wx.TB_NODIVIDER)
        self.mytb = []
        self.mytp = {}
        self.CreatToolBar()

    def CreatToolBar(self):

        for tb in ToolData().ToolBarData():
            if str(tb[1]) == '' or tb[1] == None:
                self.myTool.AddSeparator()
            else:
                self.mytb.append( self.myTool.AddTool(int(tb[0]), str(tb[1]),wx.Bitmap(ICONS_PATH+tb[2], wx.BITMAP_TYPE_ANY),
                                                  wx.NullBitmap, wx.ITEM_NORMAL, str(tb[3]), wx.EmptyString, None) )
                self.mytp[int(tb[0])] = str(tb[4])

        #print(self.mytp)
        self.myTool.Realize()

    def GetToolid(self):
        return 101


class ToolData(object):
    def __init__(self):
        self.MySql = MS.GetData(u'Menu.db', u'')
        self.ToSql = MS.SetData(u'', u'')

    def ToolBarData(self):
        self.mTBar = []
        for row in self.MySql.GetTB():
            self.mTBar.append(row)
        return self.mTBar