# In the name of God
# -*- coding: utf-8 -*-
# Windows and Panels main Frame File
#! /usr/bin/env python

import wx
import wx.dataview
from GUI.proman import Mymenu
import os


class MyLstPnl(object):
    LPn = []
    def __init__(self):
        dirfil = os.listdir('./GUI/AuiPanel/')
        for f in dirfil:
            if f[-3:] == '.py':
                self.LPn.append(f)
        self.LPn.remove( 'PAui.py')
        #print(self.LPn)

    def GetAuiPnl(self):
        return self.LPn

