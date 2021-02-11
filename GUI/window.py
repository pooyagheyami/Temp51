# -*- coding: utf-8 -*-
# In the name of God
# Main Program Start
#!/usr/bin/env python
# -*- coding: utf-8 -*-


import wx
import wx.aui
import wx.html


import GUI.MainMenu2 as MM
import GUI.MainTool as MT

import GUI.AuiPanel.Rev as RP
import GUI.AuiPanel.Stat as SP
import GUI.AuiPanel.PAui as PA
import importlib

import GUI.BG2 as BG

#import Config.basedata as bs
#import Utility.massage as ms
import Utility.Tclacal3 as C1
#import Utility.user as user
from Config.Init import * 
import wx.dataview

import GUI.proman as pro
  
class MainWin(wx.Frame):
    def __init__(self):
        wx.Frame.__init__(self,None,title=u'main',size=(800,600))

        #Check config for first start prgram ===============
        
        #C = bs.BaseCheck()
        #print C
        #C = 0
        #D = bs.Getprogini()
        #print D
        
        #BGF = D[4] 
        
        

        #Check config for show or hide aui panels=========
        #rps = int(D[0])
        #sps = int(D[1])
        #bps = int(D[2])
        #tps = int(D[3])
        rps = 1
        sps = 1
        bps = 1
        tps = 1
        BGF = "V10.jpg"


        #Menu of Program============== 
        menu = MM.MainMenu()
        statusBar = self.CreateStatusBar()
        imenu=menu.createMenuBar()

        self.SetMenuBar(imenu)
        h= menu.GetItemId()
        h1 = menu.mid
        self.Bind(wx.EVT_MENU_RANGE,self.OnMenu,id =h1, id2=h.GetId())

        #Enable or Disable Menu==========================
        #imenu.EnableTop(3, False)

        #Show aui panels==============




        #Aui Panels of Program==================
        self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )
        self.m_mgr = wx.aui.AuiManager()
        self.m_mgr.SetManagedWindow( self )
        self.m_mgr.SetFlags(wx.aui.AUI_MGR_DEFAULT)

        # Create Tool Bars=======================
        #tool = MT.MainTool(self, -1, wx.DefaultPosition, wx.DefaultSize,
         #                     wx.TB_FLAT | wx.TB_NODIVIDER | wx.TB_TEXT)
        #tool = MT.MainToolAui(self)

        #self.m_mgr.AddPane(tool[0],wx.aui.AuiPaneInfo().Name(tool).Caption("Tool bar").
        #                   ToolbarPane().Top().Row(1).LeftDockable(False).RightDockable(False))
        #self.m_mgr.AddPane(tool.myTool,wx.aui.AuiPaneInfo().Top().PinButton(True).Dock().Resizable().FloatingSize(wx.Size(122, 260)).Layer(1))
        self.ToolPnl()

        #panel revnue======================
        self.Repnl(rps)
        #Panel report=======================
        self.Stpnl(sps)
        #All Panel Aui=======================
        self.APnls()

        #set background in frame ==================
        
        self.BGrnd(bps,BGF)

          
                

        
        self.m_mgr.Update()
        self.Centre( wx.BOTH )

        #if user.Checkpass() != 'OK':
        #    print 'quit'
        #self.Bind(wx.EVT_RIGHT_DOWN,self.mouseclick)
        #Show other win in main windows==============
        '''
        if C == 1:
            wino = wx.Frame(self,-1,style=wx.FRAME_FLOAT_ON_PARENT|wx.DEFAULT_FRAME_STYLE)
            
            txt = bs.Startpro()
            Startp = ms.MyPanel1(wino,txt)

            wino.SetSize((600,400))
            wino.SetPosition((100,100))
            wino.Show()
        
        '''
        self.Clock(tps)
        self.Update()

    def OnMenu(self, event):
        self.mid = event.GetId()
        #print( self.mid )
        a = pro.DoProgram(self.mid,'M')
        #print dir(a)
        s = a.size() if 'size' in dir(a) else ()
        
        win1 = wx.Frame(self, -1)
        win1.SetSize(s)
        a.main(win1)

    def OnTool(self, event):
        self.tid = event.GetId()
        #print( self.tid )
        a = pro.DoProgram(self.tid,'T')
        # print dir(a)
        s = a.size() if 'size' in dir(a) else ()

        win1 = wx.Frame(self, -1)
        win1.SetSize(s)
        a.main(win1)

    def OnShow(self,event):
        #print event
        self.Stap.refresh()
        self.Stap.showitem() 
        #self.Stap.Layout()
        #self.m_mgr.Update()
	    #self.Centre( wx.BOTH )

    def ToolPnl(self):
        self.tool = []
        MTBL = MT.ToolData()
        MLT = MTBL.ToolBarList()
        i = 0
        for T in MLT:
            #print(MLT[T])
            MTB = MT.MyToolbar(self)
            MyTL = MTB.data
            print(MyTL)
            self.tool.append( MTB.CreatTool(MLT[T]) )
            self.tool[i].SetToolBitmapSize(wx.Size(24, 24))
            self.tool[i].Realize()
            self.m_mgr.AddPane(self.tool[i], wx.aui.AuiPaneInfo().Name("tb"+str(i)).Caption("Toolbar").
                           ToolbarPane().Top().LeftDockable(False).RightDockable(False))
            self.Bind(wx.EVT_TOOL_RANGE, self.OnTool, id=self.tool[i].mytb[0].GetId(), id2=self.tool[i].mytb[-1].GetId())
            i += 1

    def APnls(self):
        self.Pnls = []
        ML = PA.MyLstPnl()
        for P in ML.GetAuiPnl():
            #print(P)
            if P != '__init__.py':
                ii = importlib.import_module('GUI.AuiPanel.'+P[:-3])
                mp = ii.MyPanel(self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL)
                self.Pnls.append(mp)
                self.m_mgr.AddPane(mp,wx.aui.AuiPaneInfo() .Right() .PinButton(True) .Dock() .Resizable() .FloatingSize(wx.Size(400,300)).Layer(2) )


    def Repnl(self,RPS):
        self.Rpanel = RP.MyPanel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
        self.m_mgr.AddPane( self.Rpanel, wx.aui.AuiPaneInfo() .Left() .PinButton( True ).Dock().Resizable().FloatingSize( wx.Size( 200,400 ) ).Layer( 1 ) )
        self.m_mgr.Bind(wx.EVT_BUTTON,self.OnMenu)
        if RPS == 1 :
            self.m_mgr.GetPane(self.Rpanel).Show()
        elif RPS == 0:
            self.m_mgr.GetPane(self.Rpanel).Hide()
            
    def Stpnl(self,SPS):
        lbel = [u'Description',u'Data',u'Input',u'Account',u'Code',u'Date']
        
        self.Stap = SP.MyPanel( self, wx.ID_ANY, wx.DefaultPosition, wx.Size( -1,100 ), wx.TAB_TRAVERSAL, lbel )
        self.m_mgr.AddPane( self.Stap, wx.aui.AuiPaneInfo() .Bottom() .PinButton( True ).Dock().Resizable().FloatingSize( wx.Size( 400,200 ) ).Layer( 2 ) )
        
        self.m_mgr.Bind(wx.EVT_TEXT,self.OnShow)
        #self.m_mgr.Bind(wx.EVT_WINDOW_DESTROY,self.OnShow) 
        
        if SPS == 1 :
            self.m_mgr.GetPane(self.Stap).Show()
        elif SPS == 0:
            self.m_mgr.GetPane(self.Stap).Hide()


    def Clock(self,TPS):
        #self.owin = wx.Frame(self,-1,style=wx.FRAME_FLOAT_ON_PARENT|wx.DEFAULT_FRAME_STYLE)
        self.owin = C1.MyFrame1(self)
        #clockpanel = C1.ClockPanel(self.owin)
        self.owin.SetSize((250,250))
        self.owin.SetPosition((150,50))
        if TPS == 1:
            self.owin.Show()
        elif TPS == 0:
            self.owin.Hide()

    def BGrnd(self,BPS,BGF):
        #self.bmpwin = BG.MyHtmlPanel(self,wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL , BGF)    
        #self.htmlwin = BG.MyHtmlPanel(self,wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.html.HW_SCROLLBAR_AUTO )
        self.bmpwin = BG.BGPanel(self,BGF)
        self.m_mgr.AddPane( self.bmpwin, wx.aui.AuiPaneInfo() .Right() .Center() .CloseButton( False ).Dock().Resizable().FloatingSize( wx.Size( 800,600 )) )
        #print self.bmpwin.GetSize()
        if BPS == 1 :
            self.m_mgr.GetPane(self.bmpwin).Show()
        elif BPS == 0:
            self.m_mgr.GetPane(self.bmpwin).Hide()
        #self.m_mgr.GetPane(self.htmlwin).Show()
        self.m_mgr.Bind(wx.EVT_CONTEXT_MENU,self.printit)
        #self.bmpwin.Bind(wx.EVT_CONTEXT_MENU,self.printit)
        #self.m_mgr.Bind(wx.EVT_MOUSE_EVENTS,self.printit)
        #self.bmpwin.Bind(wx.EVT_MOUSE_EVENTS,self.printit)

    def mouseclick(self,event):
        print(event)

    def printit(self,event):
        #print self.bmpwin.showhide()
                    
        if self.bmpwin.showhide()[0]:
            tps = 1
            try :
                self.owin.Show()
                tps = 1
            except:
                self.Clock(tps)
                

        elif not self.bmpwin.showhide()[0]:
            tps = 0
            try :
                self.owin.Hide()
                tps = 0
            except:
                self.Clock(tps)
            
        if self.bmpwin.showhide()[1]:
            rps = 1
            self.m_mgr.GetPane(self.Rpanel).Show()
        elif not self.bmpwin.showhide()[1]:
            rps = 0
            self.m_mgr.GetPane(self.Rpanel).Hide()
            
        if self.bmpwin.showhide()[2]:
            sps = 1
            self.m_mgr.GetPane(self.Stap).Show()
        elif not self.bmpwin.showhide()[2]:
            sps = 0
            self.m_mgr.GetPane(self.Stap).Hide()
        self.m_mgr.Update()