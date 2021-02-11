# In the name of God
# -*- coding: utf-8 -*-
# Windows and Panels main Frame File
#! /usr/bin/env python

import wx
import wx.aui as wxaui
from Config.Init import *



class BGPanel(wx.Panel):
	def __init__( self,parent,BGfile ):
		wx.Panel.__init__ ( self, parent=parent, id = wx.ID_ANY, pos = wx.DefaultPosition, size = wx.DefaultSize, style = wx.TAB_TRAVERSAL )

		#bSizer2 = wx.BoxSizer( wx.VERTICAL )

		self.BGfile = BGfile
		
		self.SetBackgroundStyle(wx.BG_STYLE_ERASE)
		self.Bind(wx.EVT_ERASE_BACKGROUND, self.OnEraseBackground)

		self.m1 = wx.Menu()

		self.itm2 = wx.MenuItem( self.m1, wx.ID_ANY, u"Show O'Clock and Calendar", wx.EmptyString, wx.ITEM_CHECK )
		self.m1.Append( self.itm2 )
		self.itm2.Check( True )

		self.itm3 = wx.MenuItem( self.m1, wx.ID_ANY, u"Pan of Input Information", wx.EmptyString, wx.ITEM_CHECK )
		self.m1.Append( self.itm3 )
		self.itm3.Check( True )

		self.itm4 = wx.MenuItem( self.m1, wx.ID_ANY, u"Pan of Do it working", wx.EmptyString, wx.ITEM_CHECK )
		self.m1.Append( self.itm4 )
		self.itm4.Check( True )


		#bSizer2.Add( self.m_bitmap4, 5, wx.ALIGN_CENTER|wx.ALL, 5 )


		#self.SetSizer( bSizer2 )
		#self.Layout()

		# Connect Events

		self.Bind( wx.EVT_RIGHT_DOWN, self.m_bitmap4OnContextMenu )
		self.Bind(wxaui.EVT_AUI_RENDER, self.OnEraseBackground)

	def __del__( self ):
		pass

	# Virtual event handlers, overide them in your derived class

	def m_bitmap4OnContextMenu( self, event ):
		#print('mouse')
		self.PopupMenu( self.m1, event.GetPosition() )
		#print self.itm1.IsChecked(),self.itm2.IsChecked()
		#print self.itm3.IsChecked(),self.itm4.IsChecked()

	def showhide(self):
		return [self.itm2.IsChecked(),self.itm3.IsChecked(),self.itm4.IsChecked()]

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
