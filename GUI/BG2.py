# In the name of God
# -*- coding: utf-8 -*-
# Windows and Panels main Frame File
#! /usr/bin/env python

import wx
import wx.aui as wxaui
from Config.Init import *

import GUI.proman as pro



class BGPanel(wx.Panel):
	def __init__( self,parent,BGfile ):
		wx.Panel.__init__ ( self, parent=parent, id = wx.ID_ANY, pos = wx.DefaultPosition, size = wx.DefaultSize, style = wx.TAB_TRAVERSAL )

		#bSizer2 = wx.BoxSizer( wx.VERTICAL )

		self.BGfile = BGfile
		
		self.SetBackgroundStyle(wx.BG_STYLE_ERASE)
		self.Bind(wx.EVT_ERASE_BACKGROUND, self.OnEraseBackground)

		#self.setmenu()


		#bSizer2.Add( self.m_bitmap4, 5, wx.ALIGN_CENTER|wx.ALL, 5 )


		#self.SetSizer( bSizer2 )
		#self.Layout()

		# Connect Events

		#self.Bind( wx.EVT_RIGHT_DOWN, self.m_bitmap4OnContextMenu )
		self.Bind( wx.EVT_CONTEXT_MENU, self.setmenu)
		self.Bind(wxaui.EVT_AUI_RENDER, self.OnEraseBackground)

	def __del__( self ):
		pass

	# Virtual event handlers, overide them in your derived class

	def m_bitmap4OnContextMenu( self, event ):
		self.PopupMenu(self.m1)

		#print (self.itm3.IsChecked(),self.itm2.IsChecked())
		#print self.itm3.IsChecked(),self.itm4.IsChecked()

	def setmenu(self,event):
		self.MnuDic = { 1: [u'Menu Change',9999] ,2:[u'Toolbar Change',9998],3:[u'Panes Change',1002],4:[u'',0],
					5:[u'Databases...',1002],6:[u'Programs...',9995],7:[u'ML Design...',1002],8:[u'',0],9:[u'Settings...',1002] }
		self.m1 = wx.Menu()

		self.itms = []
		i = 0
		for itm in self.MnuDic :
			self.Bind(wx.EVT_MENU, self.OnPopupOne, id=itm)
			if self.MnuDic[itm][0] == u'':
				self.m1.AppendSeparator()
			else:
				#self.itms.append( wx.MenuItem(self.m1, wx.ID_ANY, MnuDic[itm][0], wx.EmptyString) )
				self.m1.Append(itm, self.MnuDic[itm][0])
				#self.m1.Append(itm, self.itms[i])
				#self.Bind(wx.EVT_MENU, self.OnPopupOne, id=MnuDic[itm][1])
				i = i + 1

		self.PopupMenu(self.m1)
		self.m1.Destroy()

	def OnPopupOne(self, event):
		#print(event,event.GetId())
		pmid = event.GetId()
		a = pro.DoProgram(self.MnuDic[pmid][1],'A')
		s = a.size() if 'size' in dir(a) else ()
		win1 = wx.Frame(self, -1)
		win1.SetSize(s)
		a.main(win1)

	def OnEraseBackground(self, evt):
		# yanked from ColourDB.py
		#print(evt)
		dc = evt.GetDC()
		if not dc:
			dc = wx.ClientDC(self)
			rect = self.GetUpdateRegion().GetBox()
			#dc.SetClippingRect(rect)
			dc.SetClippingRegion(rect)
		dc.Clear()
		bmp = wx.Bitmap(PICS_PATH+self.BGfile)
		dc.DrawBitmap(bmp, 0, 0)
