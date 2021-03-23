#In the name of GOD
#please put your code under here
# -*- coding: utf-8 -*-

###########################################################################
## Python code generated with wxFormBuilder (version Oct 26 2018)
## http://www.wxformbuilder.org/
##
## PLEASE DO *NOT* EDIT THIS FILE!
###########################################################################

import wx
import wx.xrc
import wx.propgrid as pg

###########################################################################
## Class MyPanel1
###########################################################################

class MyPanel1 ( wx.Panel ):

	def __init__( self, parent, id = wx.ID_ANY, pos = wx.DefaultPosition, size = wx.Size( 500,395 ), style = wx.TAB_TRAVERSAL, name = wx.EmptyString ):
		wx.Panel.__init__ ( self, parent, id = id, pos = pos, size = size, style = style, name = name )

		bSizer1 = wx.BoxSizer( wx.VERTICAL )

		self.m_propertyGridManager1 = pg.PropertyGridManager(self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.propgrid.PG_DESCRIPTION|wx.propgrid.PG_SPLITTER_AUTO_CENTER|wx.propgrid.PG_TOOLBAR|wx.propgrid.PG_TOOLTIPS|wx.TAB_TRAVERSAL)
		self.m_propertyGridManager1.SetExtraStyle( wx.propgrid.PG_EX_AUTO_UNSPECIFIED_VALUES|wx.propgrid.PG_EX_MODE_BUTTONS|wx.propgrid.PG_EX_NO_FLAT_TOOLBAR|wx.propgrid.PG_EX_NO_TOOLBAR_DIVIDER )

		self.m_propertyGridPage1 = self.m_propertyGridManager1.AddPage( u"Page", wx.ArtProvider.GetBitmap( wx.ART_REPORT_VIEW, wx.ART_BUTTON ) );
		self.Item1 = self.m_propertyGridPage1.Append( pg.PropertyCategory( u"Directory of Work", u"Directory of Work" ) )
		self.Item2 = self.m_propertyGridPage1.Append( pg.DirProperty( u"Database and Sql files", u"Database and Sql files" ) )
		self.Item3 = self.m_propertyGridPage1.Append( pg.DirProperty( u"Utility and Plugin", u"Utility and Plugin" ) )
		self.Item4 = self.m_propertyGridPage1.Append( pg.DirProperty( u"Server and Local Network", u"Server and Local Network" ) )
		self.m_propertyGridPage1.SetPropertyHelpString( Item4, u"Directory of Local Network that Database and Main File here and other client get Data from it" )
		self.Item5 = self.m_propertyGridPage1.Append( pg.DirProperty( u"Other and Temp", u"Other and Temp" ) )
		self.Item6 = self.m_propertyGridPage1.Append( pg.PropertyCategory( u"General parameter", u"General parameter" ) )
		self.Item7 = self.m_propertyGridPage1.Append( pg.DateProperty( u"Date of Today ", u"Date of Today " ) )
		self.Item8 = self.m_propertyGridPage1.Append( pg.EnumProperty( u"Language", u"Language" ) )
		self.Item9 = self.m_propertyGridPage1.Append( pg.BoolProperty( u"Show Clock", u"Show Clock" ) )
		self.Item10 = self.m_propertyGridPage1.Append( pg.FontProperty( u"Font", u"Font" ) )
		self.Item11 = self.m_propertyGridPage1.Append( pg.FlagsProperty( u"Size", u"Size" ) )
		self.Item12 = self.m_propertyGridPage1.Append( pg.StringProperty( u"position", u"position" ) )

		self.m_propertyGridPage2 = self.m_propertyGridManager1.AddPage( u"Page", wx.ArtProvider.GetBitmap( wx.ART_LIST_VIEW, wx.ART_TOOLBAR ) );
		self.Item13 = self.m_propertyGridPage2.Append( pg.PropertyCategory( u"Other Status", u"Other Status" ) )
		self.Item14 = self.m_propertyGridPage2.Append( pg.StringProperty( u"Toolbar", u"Toolbar" ) )
		self.Item15 = self.m_propertyGridPage2.Append( pg.StringProperty( u"Pan Input", u"Pan Input" ) )
		self.Item16 = self.m_propertyGridPage2.Append( pg.StringProperty( u"Pan Status", u"Pan Status" ) )
		self.Item17 = self.m_propertyGridPage2.Append( pg.ImageFileProperty( u"Background", u"Background" ) )
		self.Item18 = self.m_propertyGridPage2.Append( pg.CursorProperty( u"Cursor", u"Cursor" ) )
		self.Item19 = self.m_propertyGridPage2.Append( pg.LongStringProperty( u"Help", u"Help" ) )
		bSizer1.Add( self.m_propertyGridManager1, 1, wx.ALL|wx.EXPAND, 5 )


		self.SetSizer( bSizer1 )
		self.Layout()

	def __del__( self ):
		pass


