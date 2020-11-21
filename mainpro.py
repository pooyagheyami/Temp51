# In the name of God
# Main Program Start
#!/usr/bin/env python
# -*- codnig: utf-8 -*-

import wx
import os
import wx.adv

try:
    from agw import advancedsplash as AS
except ImportError: # if it's not there locally, try the wxPython lib.
    import wx.lib.agw.advancedsplash as AS

import sys 
import glob

import GUI.window as window
from  Config.Init import *

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
        splash = MySplashScreen()
        splash.Show()

        return True



#class MySplashScreen(wx.Panel):
#    def __init__(self,parent):
#        wx.Panel.__init__(self,parent)

class MySplashScreen(wx.adv.SplashScreen):
    def __init__(self):

        #bmp = wx.Image(opj(SPALSH_PATH+"splash3.jpg")).ConvertToBitmap()
        bmp = wx.Bitmap(os.path.normpath(os.path.join(SPALSH_PATH + "splash3.png")),wx.BITMAP_TYPE_PNG)
        wx.adv.SplashScreen.__init__(self, bmp,
                                 wx.adv.SPLASH_CENTRE_ON_SCREEN | wx.adv.SPLASH_TIMEOUT,
                                 5000, None, style=wx.BORDER_SIMPLE|wx.FRAME_NO_TASKBAR|wx.STAY_ON_TOP)


        #pn = os.path.normpath(os.path.join(SPALSH_PATH + "splash3.png"))
        #bitmap = wx.Bitmap(pn, wx.BITMAP_TYPE_PNG)
        #shadow = wx.WHITE

        #self.frame = AS.AdvancedSplash(self, bitmap=bitmap, timeout=5000,
        #                               agwStyle=AS.AS_TIMEOUT |
        #                               AS.AS_CENTER_ON_PARENT |
        #                               AS.AS_SHADOW_BITMAP
        #                               ,shadowcolour=shadow )
        self.Bind(wx.EVT_CLOSE, self.OnClose)
        #self.fc = wx.FutureCall(2000, self.ShowMain)
        self.fc = wx.CallLater(2000, self.ShowMain)

    def OnClose(self, evt):
        # Make sure the default handler runs too so this window gets
        # destroyed
        evt.Skip()
        self.Hide()

        # if the timer is still running then go ahead and show the
        # main frame now
        if self.fc.IsRunning():
            self.fc.Stop()
            self.ShowMain()

    def ShowMain(self):
        SIZE = wx.DisplaySize()
        # print SIZE

        # do main windows of program

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
