# -*- coding: utf-8 -*-

###########################################################################
## Python code generated with wxFormBuilder (version Oct 26 2018)
## http://www.wxformbuilder.org/
##
## PLEASE DO *NOT* EDIT THIS FILE!
###########################################################################

import wx
import wx.xrc

from Config.Init import *

###########################################################################
## Class MyPanel1
###########################################################################

class MyPanel1 ( wx.Panel ):

	def __init__( self, parent, id = wx.ID_ANY, pos = wx.DefaultPosition, size = wx.Size( 700,360 ), style = wx.TAB_TRAVERSAL, name = wx.EmptyString ):
		wx.Panel.__init__ ( self, parent, id = id, pos = pos, size = size, style = style, name = name )

		Vz1 = wx.BoxSizer( wx.VERTICAL )

		self.SP1 = wx.SplitterWindow( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.SP_3D )
		self.SP1.Bind( wx.EVT_IDLE, self.SP1OnIdle )

		self.P1 = wx.Panel( self.SP1, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.BORDER_RAISED|wx.TAB_TRAVERSAL )
		Vzp1 = wx.BoxSizer( wx.VERTICAL )

		Hzp1 = wx.WrapSizer( wx.HORIZONTAL, 0 )

		self.txt1 = wx.StaticText( self.P1, wx.ID_ANY, u"ID", wx.DefaultPosition, wx.Size( 70,-1 ), 0 )
		self.txt1.Wrap( -1 )

		Hzp1.Add( self.txt1, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.fld1 = wx.TextCtrl( self.P1, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		Hzp1.Add( self.fld1, 1, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL|wx.ALIGN_CENTER_VERTICAL, 5 )


		Vzp1.Add( Hzp1, 0, wx.EXPAND, 5 )

		Hzp2 = wx.WrapSizer( wx.HORIZONTAL, 0 )

		self.txt2 = wx.StaticText( self.P1, wx.ID_ANY, u"Label", wx.DefaultPosition, wx.Size( 70,-1 ), 0 )
		self.txt2.Wrap( -1 )

		Hzp2.Add( self.txt2, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.fld2 = wx.TextCtrl( self.P1, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		Hzp2.Add( self.fld2, 1, wx.ALL, 5 )


		Vzp1.Add( Hzp2, 0, wx.EXPAND, 5 )

		Hzp3 = wx.WrapSizer( wx.HORIZONTAL, 0 )

		self.txt3 = wx.StaticText( self.P1, wx.ID_ANY, u"Icon", wx.DefaultPosition, wx.Size( 70,-1 ), 0 )
		self.txt3.Wrap( -1 )

		Hzp3.Add( self.txt3, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.fld3 = wx.TextCtrl( self.P1, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		Hzp3.Add( self.fld3, 1, wx.ALL, 5 )

		self.btnIcn = wx.Button( self.P1, wx.ID_ANY, u"...", wx.DefaultPosition, wx.DefaultSize, wx.BU_EXACTFIT )
		Hzp3.Add( self.btnIcn, 0, wx.ALL, 5 )


		Vzp1.Add( Hzp3, 0, wx.EXPAND, 5 )

		Hzp31 = wx.WrapSizer( wx.HORIZONTAL, 0 )

		self.icon = wx.StaticBitmap( self.P1, wx.ID_ANY, wx.Bitmap( ICONS_PATH+u"image.png", wx.BITMAP_TYPE_ANY ), wx.DefaultPosition, wx.DefaultSize, 0 )
		Hzp31.Add( self.icon, 1, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL|wx.ALIGN_CENTER_VERTICAL, 5 )


		Vzp1.Add( Hzp31, 0, wx.ALIGN_CENTER_HORIZONTAL, 5 )

		Hzp4 = wx.WrapSizer( wx.HORIZONTAL, 0 )

		self.txt4 = wx.StaticText( self.P1, wx.ID_ANY, u"Shorcut", wx.DefaultPosition, wx.Size( 70,-1 ), 0 )
		self.txt4.Wrap( -1 )

		Hzp4.Add( self.txt4, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.fld4 = wx.TextCtrl( self.P1, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		Hzp4.Add( self.fld4, 1, wx.ALL, 5 )


		Vzp1.Add( Hzp4, 0, wx.EXPAND, 5 )

		Hzp5 = wx.WrapSizer( wx.HORIZONTAL, 0 )

		self.txt5 = wx.StaticText( self.P1, wx.ID_ANY, u"Help String", wx.DefaultPosition, wx.Size( 70,-1 ), 0 )
		self.txt5.Wrap( -1 )

		Hzp5.Add( self.txt5, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.fld5 = wx.TextCtrl( self.P1, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		Hzp5.Add( self.fld5, 1, wx.ALL, 5 )


		Vzp1.Add( Hzp5, 0, wx.EXPAND, 5 )

		Hzp6 = wx.WrapSizer( wx.HORIZONTAL, 0 )

		self.txt6 = wx.StaticText( self.P1, wx.ID_ANY, u"Status", wx.DefaultPosition, wx.Size( 70,-1 ), 0 )
		self.txt6.Wrap( -1 )

		Hzp6.Add( self.txt6, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.fld6 = wx.TextCtrl( self.P1, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		Hzp6.Add( self.fld6, 1, wx.ALL, 5 )


		Vzp1.Add( Hzp6, 0, wx.EXPAND, 5 )

		Hzp7 = wx.WrapSizer( wx.HORIZONTAL, wx.WRAPSIZER_DEFAULT_FLAGS )

		self.txt7 = wx.StaticText( self.P1, wx.ID_ANY, u"Type:", wx.DefaultPosition, wx.Size( 50,-1 ), 0 )
		self.txt7.Wrap( -1 )

		Hzp7.Add( self.txt7, 0, wx.ALL, 5 )

		self.rBtn1 = wx.RadioButton( self.P1, wx.ID_ANY, u"Normal", wx.DefaultPosition, wx.DefaultSize, 0 )
		Hzp7.Add( self.rBtn1, 0, wx.ALL, 5 )

		self.rBtn2 = wx.RadioButton( self.P1, wx.ID_ANY, u"Check", wx.DefaultPosition, wx.DefaultSize, 0 )
		Hzp7.Add( self.rBtn2, 0, wx.ALL, 5 )

		self.rBtn3 = wx.RadioButton( self.P1, wx.ID_ANY, u"Radio", wx.DefaultPosition, wx.DefaultSize, 0 )
		Hzp7.Add( self.rBtn3, 0, wx.ALL, 5 )

		self.rBtn4 = wx.RadioButton( self.P1, wx.ID_ANY, u"SubMenu", wx.DefaultPosition, wx.DefaultSize, 0 )
		Hzp7.Add( self.rBtn4, 0, wx.ALL, 5 )


		Vzp1.Add( Hzp7, 0, wx.EXPAND, 5 )

		Hzp71 = wx.WrapSizer( wx.HORIZONTAL, 0 )

		self.cBox1 = wx.CheckBox( self.P1, wx.ID_ANY, u"Disable", wx.DefaultPosition, wx.DefaultSize, 0 )
		Hzp71.Add( self.cBox1, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL|wx.ALIGN_CENTER_HORIZONTAL, 5 )

		self.cBox2 = wx.CheckBox( self.P1, wx.ID_ANY, u"Hidden", wx.DefaultPosition, wx.DefaultSize, 0 )
		Hzp71.Add( self.cBox2, 0, wx.ALL, 5 )


		Vzp1.Add( Hzp71, 0, wx.ALIGN_CENTER_HORIZONTAL, 5 )


		self.P1.SetSizer( Vzp1 )
		self.P1.Layout()
		Vzp1.Fit( self.P1 )
		self.P2 = wx.Panel( self.SP1, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.BORDER_RAISED|wx.TAB_TRAVERSAL )
		Vzp2 = wx.BoxSizer( wx.VERTICAL )

		Hzp8 = wx.WrapSizer( wx.HORIZONTAL, 0 )

		self.txt8 = wx.StaticText( self.P2, wx.ID_ANY, u"Program to DO", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.txt8.Wrap( -1 )

		Hzp8.Add( self.txt8, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.file1 = wx.FilePickerCtrl( self.P2, wx.ID_ANY, wx.EmptyString, u"Select a file", u"*.py", wx.DefaultPosition, wx.DefaultSize, wx.FLP_DEFAULT_STYLE|wx.FLP_SMALL )
		Hzp8.Add( self.file1, 1, wx.ALL, 5 )


		Vzp2.Add( Hzp8, 0, wx.EXPAND, 5 )

		Hzp9 = wx.WrapSizer( wx.HORIZONTAL, 0 )

		self.Doprgitm = wx.TextCtrl( self.P2, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		Hzp9.Add( self.Doprgitm, 1, wx.ALL, 5 )


		Vzp2.Add( Hzp9, 0, wx.EXPAND, 5 )

		Hzp10 = wx.WrapSizer( wx.HORIZONTAL, 0 )

		self.btn1 = wx.Button( self.P2, wx.ID_ANY, u"Preview", wx.DefaultPosition, wx.DefaultSize, 0 )
		Hzp10.Add( self.btn1, 0, wx.ALL, 5 )

		self.btn2 = wx.Button( self.P2, wx.ID_ANY, u"Open File", wx.DefaultPosition, wx.DefaultSize, 0 )
		Hzp10.Add( self.btn2, 0, wx.ALL, 5 )

		self.btn3 = wx.Button( self.P2, wx.ID_ANY, u"New...", wx.DefaultPosition, wx.DefaultSize, 0 )
		Hzp10.Add( self.btn3, 0, wx.ALL, 5 )


		Vzp2.Add( Hzp10, 0, wx.EXPAND, 5 )

		Hzp11 = wx.WrapSizer( wx.HORIZONTAL, 0 )

		self.btn4 = wx.Button( self.P2, wx.ID_ANY, u"Analiz...", wx.DefaultPosition, wx.DefaultSize, 0 )
		Hzp11.Add( self.btn4, 0, wx.ALL, 5 )

		self.btn5 = wx.Button( self.P2, wx.ID_ANY, u"Parse...", wx.DefaultPosition, wx.DefaultSize, 0 )
		Hzp11.Add( self.btn5, 0, wx.ALL, 5 )

		self.btn6 = wx.Button( self.P2, wx.ID_ANY, u"Generate1", wx.DefaultPosition, wx.DefaultSize, 0 )
		Hzp11.Add( self.btn6, 0, wx.ALL, 5 )


		Vzp2.Add( Hzp11, 0, wx.EXPAND, 5 )

		Hzpl = wx.WrapSizer( wx.HORIZONTAL, 0 )

		self.line1 = wx.StaticLine( self.P2, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_HORIZONTAL )
		Hzpl.Add( self.line1, 1, wx.EXPAND |wx.ALL, 5 )


		Vzp2.Add( Hzpl, 0, wx.EXPAND, 5 )

		Hzp12 = wx.WrapSizer( wx.HORIZONTAL, 0 )

		self.txt9 = wx.StaticText( self.P2, wx.ID_ANY, u"Select Database", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.txt9.Wrap( -1 )

		Hzp12.Add( self.txt9, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.dir1 = wx.DirPickerCtrl( self.P2, wx.ID_ANY, wx.EmptyString, u"Select a folder", wx.DefaultPosition, wx.DefaultSize, wx.DIRP_DEFAULT_STYLE|wx.DIRP_SMALL )
		Hzp12.Add( self.dir1, 1, wx.ALL, 5 )


		Vzp2.Add( Hzp12, 0, wx.EXPAND, 5 )

		Hzp13 = wx.WrapSizer( wx.HORIZONTAL, 0 )

		self.txt10 = wx.StaticText( self.P2, wx.ID_ANY, u"Tabels and Fields", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.txt10.Wrap( -1 )

		Hzp13.Add( self.txt10, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		Lbox1Choices = []
		self.Lbox1 = wx.ListBox( self.P2, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, Lbox1Choices, 0 )
		Hzp13.Add( self.Lbox1, 1, wx.ALL, 5 )


		Vzp2.Add( Hzp13, 0, wx.EXPAND, 5 )

		Hzp14 = wx.WrapSizer( wx.HORIZONTAL, wx.WRAPSIZER_DEFAULT_FLAGS )

		self.btn7 = wx.Button( self.P2, wx.ID_ANY, u"Analiz...", wx.DefaultPosition, wx.DefaultSize, 0 )
		Hzp14.Add( self.btn7, 0, wx.ALL, 5 )

		self.btn8 = wx.Button( self.P2, wx.ID_ANY, u"Parse...", wx.DefaultPosition, wx.DefaultSize, 0 )
		Hzp14.Add( self.btn8, 0, wx.ALL, 5 )

		self.btn9 = wx.Button( self.P2, wx.ID_ANY, u"Generate2", wx.DefaultPosition, wx.DefaultSize, 0 )
		Hzp14.Add( self.btn9, 0, wx.ALL, 5 )


		Vzp2.Add( Hzp14, 1, wx.EXPAND, 5 )


		self.P2.SetSizer( Vzp2 )
		self.P2.Layout()
		Vzp2.Fit( self.P2 )
		self.SP1.SplitVertically( self.P1, self.P2, 349 )
		Vz1.Add( self.SP1, 1, wx.EXPAND, 5 )

		Hz1 = wx.BoxSizer( wx.HORIZONTAL )

		self.btnA = wx.Button( self, wx.ID_ANY, u"Apply", wx.DefaultPosition, wx.DefaultSize, 0 )
		Hz1.Add( self.btnA, 0, wx.ALL, 5 )

		self.btnS = wx.Button( self, wx.ID_ANY, u"Save ", wx.DefaultPosition, wx.DefaultSize, 0 )
		Hz1.Add( self.btnS, 0, wx.ALL, 5 )

		self.btnR = wx.Button( self, wx.ID_ANY, u"Report", wx.DefaultPosition, wx.DefaultSize, 0 )
		Hz1.Add( self.btnR, 0, wx.ALL, 5 )


		Vz1.Add( Hz1, 0, wx.ALIGN_CENTER_HORIZONTAL, 5 )


		self.SetSizer( Vz1 )
		self.Layout()

		# Connect Events
		self.btnIcn.Bind( wx.EVT_BUTTON, self.opnicn )
		self.rBtn1.Bind( wx.EVT_RADIOBUTTON, self.typitm )
		self.rBtn2.Bind( wx.EVT_RADIOBUTTON, self.typitm )
		self.rBtn3.Bind( wx.EVT_RADIOBUTTON, self.typitm )
		self.rBtn4.Bind( wx.EVT_RADIOBUTTON, self.typitm )
		self.cBox1.Bind( wx.EVT_CHECKBOX, self.disitm )
		self.cBox2.Bind( wx.EVT_CHECKBOX, self.hiditm )
		self.file1.Bind( wx.EVT_FILEPICKER_CHANGED, self.chngfil )
		self.btn1.Bind( wx.EVT_BUTTON, self.prvw )
		self.btn2.Bind( wx.EVT_BUTTON, self.opnfil )
		self.btn3.Bind( wx.EVT_BUTTON, self.newfil )
		self.btn4.Bind( wx.EVT_BUTTON, self.anliz1 )
		self.btn5.Bind( wx.EVT_BUTTON, self.pars1 )
		self.btn6.Bind( wx.EVT_BUTTON, self.gnrt1 )
		self.dir1.Bind( wx.EVT_DIRPICKER_CHANGED, self.dbfil )
		self.Lbox1.Bind( wx.EVT_LISTBOX, self.tblfld )
		self.btn7.Bind( wx.EVT_BUTTON, self.anliz2 )
		self.btn8.Bind( wx.EVT_BUTTON, self.pars2 )
		self.btn9.Bind( wx.EVT_BUTTON, self.gnrt2 )
		self.btnA.Bind( wx.EVT_BUTTON, self.Aply )
		self.btnS.Bind( wx.EVT_BUTTON, self.Save )
		self.btnR.Bind( wx.EVT_BUTTON, self.Rprt )

	def __del__( self ):
		pass


	# Virtual event handlers, overide them in your derived class
	def opnicn( self, event ):
		event.Skip()

	def typitm( self, event ):
		event.Skip()




	def disitm( self, event ):
		event.Skip()

	def hiditm( self, event ):
		event.Skip()

	def chngfil( self, event ):
		event.Skip()

	def prvw( self, event ):
		event.Skip()

	def opnfil( self, event ):
		event.Skip()

	def newfil( self, event ):
		event.Skip()

	def anliz1( self, event ):
		event.Skip()

	def pars1( self, event ):
		event.Skip()

	def gnrt1( self, event ):
		event.Skip()

	def dbfil( self, event ):
		event.Skip()

	def tblfld( self, event ):
		event.Skip()

	def anliz2( self, event ):
		event.Skip()

	def pars2( self, event ):
		event.Skip()

	def gnrt2( self, event ):
		event.Skip()

	def Aply( self, event ):
		event.Skip()

	def Save( self, event ):
		event.Skip()

	def Rprt( self, event ):
		event.Skip()

	def SP1OnIdle( self, event ):
		self.SP1.SetSashPosition( 349 )
		self.SP1.Unbind( wx.EVT_IDLE )


