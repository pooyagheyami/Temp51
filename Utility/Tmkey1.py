# -*- coding: utf-8 -*-

###########################################################################
## Python code generated with wxFormBuilder (version Oct 26 2018)
## http://www.wxformbuilder.org/
##
## PLEASE DO *NOT* EDIT THIS FILE!
###########################################################################

import wx
import wx.xrc
import getmap
import os
from Config.Init import *

###########################################################################
## Class MyPanel3
###########################################################################

class TmPanel1 ( wx.Panel ):

	def __init__( self, parent, id = wx.ID_ANY, pos = wx.DefaultPosition, size = wx.Size( 640,200 ), style = wx.TAB_TRAVERSAL, name = wx.EmptyString ):
		wx.Panel.__init__ ( self, parent, id = id, pos = pos, size = size, style = style, name = name )

                self.itext = ''
                self.MyMap = getmap.GetMapKey()

                self.MyMap.Loadmap(UTILITY_PATH+u"Map1")

		bSizer1 = wx.BoxSizer( wx.VERTICAL )

		bSizer2 = wx.BoxSizer( wx.HORIZONTAL )

		self.kbtn1 = []
		i = 0
		self.row1 = self.MyMap.row1
		self.srow1 = self.MyMap.srow1

		for ky in self.row1:
                    self.kbtn1.append( wx.Button( self, wx.ID_ANY, ky, wx.DefaultPosition, wx.DefaultSize, wx.BU_EXACTFIT ) )
                    bSizer2.Add( self.kbtn1[i], 1, wx.EXPAND, 5 )
                    i += 1

                


		bSizer1.Add( bSizer2, 1, wx.EXPAND, 5 )

		bSizer3 = wx.BoxSizer( wx.HORIZONTAL )

		self.m_button48 = wx.Button( self, wx.ID_ANY, u"TAB", wx.DefaultPosition, wx.Size( 45,-1 ), wx.BU_EXACTFIT )
		bSizer3.Add( self.m_button48, 1, wx.EXPAND, 5 )

                self.kbtn2 = []
                i = 0
                self.row2 = self.MyMap.row2
                self.srow2 = self.MyMap.srow2
		for ky in self.row2:
                    self.kbtn2.append(wx.Button( self, wx.ID_ANY, ky, wx.DefaultPosition, wx.DefaultSize, wx.BU_EXACTFIT ))
                    bSizer3.Add( self.kbtn2[i], 1, wx.EXPAND, 5 )
                    i += 1

                

		self.m_button61 = wx.Button( self, wx.ID_ANY, u"|", wx.DefaultPosition, wx.Size( 55,-1 ), 0 )
		bSizer3.Add( self.m_button61, 1, wx.EXPAND, 5 )


		bSizer1.Add( bSizer3, 1, wx.EXPAND, 5 )

		bSizer4 = wx.BoxSizer( wx.HORIZONTAL )

		self.bcps = wx.Button( self, wx.ID_ANY, u"Caps Lock", wx.DefaultPosition, wx.Size( 60,-1 ), wx.BU_EXACTFIT )
		bSizer4.Add( self.bcps, 1, wx.EXPAND, 5 )

		self.kbtn3 = []
                i = 0
                self.row3 = self.MyMap.row3
                self.srow3 = self.MyMap.srow3
		for ky in self.row3:
                    self.kbtn3.append(wx.Button( self, wx.ID_ANY, ky, wx.DefaultPosition, wx.DefaultSize, wx.BU_EXACTFIT ))
                    bSizer4.Add( self.kbtn3[i], 1, wx.EXPAND, 5 )
                    i += 1

                
		

		self.m_button62 = wx.Button( self, wx.ID_ANY, u"Enter", wx.DefaultPosition, wx.Size( 85,-1 ), 0 )
		bSizer4.Add( self.m_button62, 1, wx.EXPAND, 5 )


		bSizer1.Add( bSizer4, 1, wx.EXPAND, 5 )

		bSizer5 = wx.BoxSizer( wx.HORIZONTAL )

		

		self.bshft1 = wx.ToggleButton( self, wx.ID_ANY, u"Shift", wx.DefaultPosition, wx.Size( 80,-1 ), 0 )
		bSizer5.Add( self.bshft1, 1, wx.EXPAND, 5 )

		self.kbtn4 = []
                i = 0
                self.row4 = self.MyMap.row4
                self.srow4 = self.MyMap.srow4
		for ky in self.row4:
                    self.kbtn4.append(wx.Button( self, wx.ID_ANY, ky, wx.DefaultPosition, wx.DefaultSize, wx.BU_EXACTFIT ))
                    bSizer5.Add( self.kbtn4[i], 1, wx.EXPAND, 5 )
                    i += 1

                

		self.bshft2 = wx.ToggleButton( self, wx.ID_ANY, u"Shift", wx.DefaultPosition, wx.Size( 95,-1 ), 0 )
		bSizer5.Add( self.bshft2, 1, wx.EXPAND, 5 )


		bSizer1.Add( bSizer5, 1, wx.EXPAND, 5 )

		bSizer6 = wx.BoxSizer( wx.HORIZONTAL )

		self.bctrl1 = wx.Button( self, wx.ID_ANY, u"Ctrl", wx.DefaultPosition, wx.Size( 60,-1 ), wx.BU_EXACTFIT )
		bSizer6.Add( self.bctrl1, 1, wx.EXPAND, 5 )

		self.m_toggleBtn1 = wx.ToggleButton( self, wx.ID_ANY, u"command", wx.DefaultPosition, wx.Size( 60,-1 ), 0 )
		bSizer6.Add( self.m_toggleBtn1, 1, wx.EXPAND, 5 )

		self.balt1 = wx.Button( self, wx.ID_ANY, u"Alt", wx.DefaultPosition, wx.DefaultSize, wx.BU_EXACTFIT )
		bSizer6.Add( self.balt1, 1, wx.EXPAND, 5 )

		self.m_button29 = wx.Button( self, wx.ID_ANY, u"Space", wx.DefaultPosition, wx.Size( 275,-1 ), 0 )
		bSizer6.Add( self.m_button29, 1, wx.EXPAND, 5 )

		self.balt2 = wx.Button( self, wx.ID_ANY, u"Alt", wx.DefaultPosition, wx.DefaultSize, wx.BU_EXACTFIT )
		bSizer6.Add( self.balt2, 1, wx.EXPAND, 5 )

		#self.bcomd = wx.Button( self, wx.ID_ANY, u"Win", wx.DefaultPosition, wx.DefaultSize, wx.BU_EXACTFIT )
		#bSizer6.Add( self.bcomd, 1, wx.EXPAND, 5 )
		m_choice1Choices = self.loadname()
		self.m_choice1 = wx.Choice( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, m_choice1Choices, 0 )
		self.m_choice1.SetSelection( 0 )
		bSizer6.Add( self.m_choice1, 1, wx.EXPAND, 5 )

		self.bctrl2 = wx.Button( self, wx.ID_ANY, u"Ctrl", wx.DefaultPosition, wx.Size( 60,-1 ), 0 )
		bSizer6.Add( self.bctrl2, 1, wx.EXPAND, 5 )


		bSizer1.Add( bSizer6, 1, wx.EXPAND, 5 )


		self.SetSizer( bSizer1 )
		self.Layout()

		# Connect Events
		#self.btab.Bind( wx.EVT_BUTTON, self.ontab )
		#self.bbck.Bind( wx.EVT_BUTTON, self.onbak )
		self.bcps.Bind( wx.EVT_BUTTON, self.oncaps )
		#self.bentr.Bind( wx.EVT_BUTTON, self.onenter )
		self.bshft1.Bind( wx.EVT_TOGGLEBUTTON, self.onshftl )
		self.bshft2.Bind( wx.EVT_TOGGLEBUTTON, self.onshftl  )
		self.bctrl1.Bind( wx.EVT_BUTTON, self.lctrl )
		self.balt1.Bind( wx.EVT_BUTTON, self.lalt )
		#self.bspce.Bind( wx.EVT_BUTTON, self.onspce )
		self.balt2.Bind( wx.EVT_BUTTON, self.ralt )
		#self.bcomd.Bind( wx.EVT_BUTTON, self.oncom )
		self.m_choice1.Bind( wx.EVT_CHOICE, self.lodit )
		self.bctrl2.Bind( wx.EVT_BUTTON, self.rctrl )
		#self.Bind(wx.EVT_KEY_DOWN, self.keydwn)
		#self.Bind(wx.EVT_KEY_UP, self.keyup )
		#self.kbtn2[1].Bind(wx.EVT_CHAR_HOOK, self.keydwn)
		#self.kbtn2[1].Bind(wx.EVT_CHAR_HOOK, self.keydwn)
		self.Bind(wx.EVT_CHAR_HOOK , self.keyhook)

	def __del__( self ):
		pass


	# Virtual event handlers, overide them in your derived class
	def init( self ):
                self.row1 = self.MyMap.row1
		self.srow1 = self.MyMap.srow1
		self.row2 = self.MyMap.row2
                self.srow2 = self.MyMap.srow2
                self.row3 = self.MyMap.row3
                self.srow3 = self.MyMap.srow3
                self.row4 = self.MyMap.row4
                self.srow4 = self.MyMap.srow4
        def loadname( self ):
                lstf = []
                for f in os.listdir(os.getcwd()):
                        if '.' not in f:
                                if os.path.getsize(os.getcwd()+'/'+f) < 1000 :
                                        
                                        lstf.append(str(f))
                print lstf                        
                return lstf            

        def lodit( self, event ):
		f = self.m_choice1.GetStringSelection()
		self.MyMap = getmap.GetMapKey()
		self.MyMap.Loadmap(os.getcwd()+u'/'+f)
		self.init()
                     
	def ontab( self, event ):
		print event
	
	def onbak( self, event ):
		print event
	
	def oncaps( self, event ):
		print event
	
	def onenter( self, event ):
		print event

	def keydwn( self , event ):
                print event
                event.Skip()
        def keyup( self , event ):
                print event
                event.Skip()
	def keyhook( self, event ):
                keycod =  event.GetKeyCode()
                controlDown = event.CmdDown()
                altDown = event.AltDown()
                shiftDown = event.ShiftDown()
                                
                self.show_in_keyboard(keycod)
                
                if keycod == wx.WXK_BACK:
                        self.GTXT = self.GTXT[:-1]
                        
                elif keycod == wx.WXK_TAB:
                        self.GTXT = self.GTXT + '    '
                        
                elif keycod == wx.WXK_RETURN:
                        self.GTXT=self.GTXT+'\n'
                        
                elif keycod == wx.WXK_SPACE:
                        self.GTXT = self.GTXT + ' '
                        
                elif keycod == wx.WXK_SHIFT:
                        self.shift = 1
               
                event.Skip()
	def onshftl( self, event ):
		print self.bshft2.GetValue()
		if self.bshft1.GetValue() or self.bshft2.GetValue():
                        self.Updatekey(True)
                else:
                        self.Updatekey(False)
	
	def onshftr( self, event ):
		print event
	
	def lctrl( self, event ):
		print event
	
	def lalt( self, event ):
		print event
	
	def onspce( self, event ):
		print event
	
	def ralt( self, event ):
		print event
	
	def oncom( self, event ):
		print event
	
	def rctrl( self, event ):
		print event
	def onkey( self, event ):
		return event.GetEventObject().GetLabel()

	def Updatekey(self,shift):
                if shift :
                        i = 0
                        for lbl in self.srow1:
                                self.kbtn1[i].SetLabel(lbl)
                                i += 1
                        i = 0
                        for lbl in self.srow2:
                                self.kbtn2[i].SetLabel(lbl)
                                i += 1
                        i = 0
                        
                        for lbl in self.srow3:
                                self.kbtn3[i].SetLabel(lbl)
                                i += 1
                        i = 0
                        
                        for lbl in self.srow4:
                                self.kbtn4[i].SetLabel(lbl)
                                i += 1
                else:
                        i = 0
                        
                        for lbl in self.row1:
                                self.kbtn1[i].SetLabel(lbl)
                                i += 1
                        i = 0        
                        for lbl in self.row2:
                                self.kbtn2[i].SetLabel(lbl)
                                i += 1
                        i = 0        
                        for lbl in self.row3:
                                self.kbtn3[i].SetLabel(lbl)
                                i += 1
                        i = 0        
                        for lbl in self.row4:
                                self.kbtn4[i].SetLabel(lbl)
                                i += 1
	
                #self.Refresh()
		#self.Layout()
   


