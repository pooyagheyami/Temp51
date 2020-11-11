# In the name of God
# -*- coding: utf-8 -*-
# Windows and Panels main Frame File
#! /usr/bin/env python

import wx
import wx.html
from Config.Init import *



class MyHtmlPanel(wx.Panel):
	def __init__( self,parent,id,pos,siz,style,bgfile ):
		wx.Panel.__init__ ( self, parent, id = wx.ID_ANY, pos = wx.DefaultPosition, size = wx.DefaultSize, style = wx.TAB_TRAVERSAL )

		bSizer2 = wx.BoxSizer( wx.VERTICAL )
		#self.SetLayoutDirection(2)
		'''
		self.BImage = wx.Image( PICS_PATH+bgfile, wx.BITMAP_TYPE_ANY )
		if bgfile != 'None':
		    W = self.BImage.GetWidth()
            H = self.BImage.GetHeight()
            self.BImage = self.BImage.Scale(1440,900)
            mi2 = self.BImage.Resize((1024,800),(0,0))
        '''
		mi = wx.Bitmap( PICS_PATH+bgfile, wx.BITMAP_TYPE_ANY )
		mi.SetSize((1440,900))

		self.m1 = wx.Menu()

		self.itm2 = wx.MenuItem( self.m1, wx.ID_ANY, u"Show O'Clock and Calendar", wx.EmptyString, wx.ITEM_CHECK )
		self.m1.AppendItem( self.itm2 )
		self.itm2.Check( True )

		self.itm3 = wx.MenuItem( self.m1, wx.ID_ANY, u"Pan of Input Information", wx.EmptyString, wx.ITEM_CHECK )
		self.m1.AppendItem( self.itm3 )
		self.itm3.Check( True )

		self.itm4 = wx.MenuItem( self.m1, wx.ID_ANY, u"Pan of Do it working", wx.EmptyString, wx.ITEM_CHECK )
		self.m1.AppendItem( self.itm4 )
		self.itm4.Check( True )


		#self.m_bitmap4 = wx.StaticBitmap( self, wx.ID_ANY, wx.Bitmap( bgfile , wx.BITMAP_TYPE_ANY ), wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_bitmap4 = wx.StaticBitmap( self, wx.ID_ANY, mi, wx.DefaultPosition, wx.DefaultSize, 0 )

		bSizer2.Add( self.m_bitmap4, 5, wx.ALIGN_CENTER|wx.ALL, 5 )


		self.SetSizer( bSizer2 )
		self.Layout()

		# Connect Events
		self.m_bitmap4.Bind( wx.EVT_RIGHT_DOWN, self.m_bitmap4OnContextMenu )

	def __del__( self ):
		pass

	# Virtual event handlers, overide them in your derived class

	def m_bitmap4OnContextMenu( self, event ):
		self.m_bitmap4.PopupMenu( self.m1, event.GetPosition() )
		#print self.itm1.IsChecked(),self.itm2.IsChecked()
		#print self.itm3.IsChecked(),self.itm4.IsChecked()

	def showhide(self):
		return [self.itm2.IsChecked(),self.itm3.IsChecked(),self.itm4.IsChecked()]
