# In the name of God
# Main Program Start
#!/usr/bin/env python
# -*- coding: utf-8 -*-

import wx
import os
import wx.adv

import sys 
import glob

import GUI.window as window
from Config.Init import *

#import Utility.user as user



class mainApp(wx.App):

    def OnInit(self):
        #check directory and path in config file and program

        #check Databases of program

        #check Date,Time,propertis of file

        #Inter username and password of users
               

        #Check lock if nassesry

        #check hardware and connection
        #SIZE = wx.DisplaySize()
        #print SIZE

        #do main windows of program 

        #frame = window.MainWin()
        #frame.SetSize(SIZE)
        #frame.SetPosition((1,1))
        #frame.CenterOnScreen()
        
        #frame.Show()
        locale = wx.Locale(wx.LANGUAGE_ENGLISH)
        splash = MySplashScreen()
        splash.Show()

        return True

class MySplashScreen(wx.adv.SplashScreen):
    def __init__(self):

        #bmp = wx.Image(opj(SPALSH_PATH+"splash3.jpg")).ConvertToBitmap()
        bmp = wx.Bitmap(os.path.normpath(os.path.join(SPALSH_PATH + "splash3.png")),wx.BITMAP_TYPE_PNG)
        wx.adv.SplashScreen.__init__(self, bmp,
                                 wx.adv.SPLASH_CENTRE_ON_SCREEN | wx.adv.SPLASH_TIMEOUT,
                                 5000, None, style=wx.BORDER_SIMPLE|wx.FRAME_NO_TASKBAR|wx.STAY_ON_TOP)

        self.Bind(wx.EVT_CLOSE, self.OnClose)
        #self.fc = wx.FutureCall(2000, self.ShowMain)
        self.fc = wx.CallLater(2000, self.ShowMain)

    def OnClose(self, evt):
        # Make sure the default handler runs too so this window gets destroyed
        evt.Skip()
        self.Hide()

        # if the timer is still running then go ahead and show the main frame now
        if self.fc.IsRunning():
            self.fc.Stop()
            self.ShowMain()

    def ShowMain(self):
        SIZE = wx.DisplaySize()
        frame = window.MainWin()
        frame.SetSize(SIZE)
        frame.SetPosition((1, 1))
        # frame.CenterOnScreen()
        frame.Show()
        # frame = wxPythonDemo(None, "wxPython: (A Demonstration)")
        # frame.Show()
        if self.fc.IsRunning():
            self.Raise()
        # wx.CallAfter(frame.ShowTip)

if __name__ == '__main__':
    app = mainApp()
    app.MainLoop()
