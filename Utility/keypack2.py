# -*- coding: utf-8 -*- 

###########################################################################
## Python code generated with wxFormBuilder (version Jun 17 2015)
## http://www.wxformbuilder.org/
##
## PLEASE DO "NOT" EDIT THIS FILE!
###########################################################################

import wx
import wx.xrc
import Tmkey1
import Tmapkey

###########################################################################
## Class MyPanel1
###########################################################################

class MyPanel1 ( wx.Panel ):
	
	def __init__( self, parent, id = wx.ID_ANY, pos = wx.DefaultPosition, size = wx.Size( 730,170 ), style = wx.TAB_TRAVERSAL, name = wx.EmptyString ):
		wx.Panel.__init__ ( self, parent, id = id, pos = pos, size = size, style = style, name = name )

                self.SetLayoutDirection(1)
		self.txt = ''
		bSizer23 = wx.BoxSizer( wx.VERTICAL )

		bSizer24 = wx.BoxSizer( wx.HORIZONTAL )

		self.m_textCtrl1 = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer24.Add( self.m_textCtrl1, 1, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.m_bpButton1 = wx.BitmapButton( self, wx.ID_ANY, wx.NullBitmap, wx.DefaultPosition, wx.DefaultSize, wx.BU_AUTODRAW|0 )

		self.m_bpButton1.SetBitmap( wx.ArtProvider.GetBitmap( wx.ART_GO_DOWN, wx.ART_BUTTON ) )
		bSizer24.Add( self.m_bpButton1, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )


		bSizer23.Add( bSizer24, 1, wx.EXPAND|wx.ALIGN_CENTER_HORIZONTAL, 5 )

		bSizer25 = wx.BoxSizer( wx.HORIZONTAL )

		self.mapkey = wx.BitmapButton( self, wx.ID_ANY, wx.NullBitmap, wx.DefaultPosition, wx.DefaultSize, wx.BU_AUTODRAW|0 )

		self.mapkey.SetBitmap( wx.ArtProvider.GetBitmap( wx.ART_FILE_OPEN, wx.ART_BUTTON ) )
		bSizer25.Add( self.mapkey, 0, wx.ALL, 5 )

		self.m_button197 = wx.Button( self, wx.ID_ANY, u"cancel", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer25.Add( self.m_button197, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.m_button196 = wx.Button( self, wx.ID_ANY, u"ok", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer25.Add( self.m_button196, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )


		bSizer23.Add( bSizer25, 0, wx.ALIGN_RIGHT, 5 )
		
		self.Pcal1 = wx.PopupTransientWindow(self.GetTopLevelParent(),wx.SIMPLE_BORDER)
                self.pnl = Tmkey1.TmPanel1(self.Pcal1)

                
		
		self.SetSizer( bSizer23 )
		self.Layout()
		
		# Connect Events
		self.m_bpButton1.Bind( wx.EVT_BUTTON, self.keybrd )
		self.m_button197.Bind( wx.EVT_BUTTON, self.cancl )
		self.m_button196.Bind( wx.EVT_BUTTON, self.doit )
		self.mapkey.Bind( wx.EVT_BUTTON, self.domapkey )


		self.pnl.Bind(wx.EVT_BUTTON,self.Onbind)
	
	def __del__( self ):
		pass
	
	
	# Virtual event handlers, overide them in your derived class
	def keybrd( self, event ):
                self.Pcal1.SetSize((640,210))
                btn = event.GetEventObject()
                pos = btn.ClientToScreen( (0,0) )
                sz =  btn.GetSize()
                self.Pcal1.Position(pos, (0, sz[1]))
                if not self.Pcal1.IsShown():
                        #self.Pcal1.Popup()
                        self.Pcal1.Show()
                        #print 'Popup is'
                else:
                        print 'Show 2'
	
	def cancl( self, event ):
		q = self.GetParent()
                q.Close()
	
	def doit( self, event ):
		print self.m_textCtrl1.GetValue()
		q = self.GetParent()
                q.Close()

	def Onbind(self, event):
                #print event
                
                #print event.GetEventObject().GetLabel()
                r =  event.GetEventObject().GetLabel()
                if r == u"Enter":
                    self.txt = self.txt + ''
                    self.Pcal1.Show(False)
                    #print self.Pcal1.IsShownOnScreen()
                    
                elif r == u'Space':
                    self.txt = self.txt + ' '
                elif r == u'TAB':
                    self.txt = self.txt + '       '
                elif r == u"<-":
                    self.txt = self.txt[:-1]    
                else:
                    self.txt = self.txt + r
                #self.txt = self.txt + t
                self.m_textCtrl1.SetValue(self.txt)

        def domapkey( self, event ):
		iwin = wx.Dialog(self,-1)
		pnl = Tmapkey.MpPanel1(iwin)
		iwin.SetSize((535,185))
		iwin.ShowModal()


		self.Refresh()
		self.Layout() 
		iwin.Destroy()
	
	

