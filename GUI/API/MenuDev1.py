# -*- coding: utf-8 -*-

###########################################################################
## Python code generated with wxFormBuilder (version Oct 26 2018)
## http://www.wxformbuilder.org/
##
## PLEASE DO *NOT* EDIT THIS FILE!
###########################################################################

import wx
import wx.xrc
import wx.dataview
import wx.stc as stc

import Database.MenuSet2 as MS
import GUI.API.MitemFrm as MF

###########################################################################
## Class MyPanel1
###########################################################################

class MyPanel1 ( wx.Panel ):

    def __init__( self, parent, id = wx.ID_ANY, pos = wx.DefaultPosition, size = wx.Size( 646,300 ), style = wx.TAB_TRAVERSAL, name = wx.EmptyString ):
        wx.Panel.__init__ ( self, parent, id = id, pos = pos, size = size, style = style, name = name )

        Vsz1 = wx.BoxSizer( wx.VERTICAL )

        self.Spw1 = wx.SplitterWindow( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.SP_3DSASH|wx.SP_NO_XP_THEME )
        self.Spw1.Bind( wx.EVT_IDLE, self.Spw1OnIdle )

        self.pnl1 = wx.Panel( self.Spw1, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
        Vsz2 = wx.BoxSizer( wx.VERTICAL )

        self.TLCtrl1 = wx.dataview.TreeListCtrl( self.pnl1, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize,wx.dataview.TL_CHECKBOX|wx.dataview.TL_DEFAULT_STYLE|wx.dataview.TL_MULTIPLE )
        self.TLCtrl1.AppendColumn( u"ID", wx.COL_WIDTH_DEFAULT, wx.ALIGN_LEFT, wx.COL_RESIZABLE )
        self.TLCtrl1.AppendColumn( u"Name", wx.COL_WIDTH_DEFAULT, wx.ALIGN_LEFT, wx.COL_RESIZABLE )
        self.TLCtrl1.AppendColumn( u"dir", wx.COL_WIDTH_DEFAULT, wx.ALIGN_LEFT, wx.COL_RESIZABLE )
        self.TLCtrl1.AppendColumn( u"access", wx.COL_WIDTH_DEFAULT, wx.ALIGN_LEFT, wx.COL_RESIZABLE )

        Vsz2.Add( self.TLCtrl1, 1, wx.EXPAND |wx.ALL, 5 )

        self.MyMenu = MS.GetData(u'Menu2.db', u'')
        broot = self.TLCtrl1.GetRootItem()
        roots = self.MyMenu.AllBar()

        for r in roots:
            grp_roots = self.TLCtrl1.AppendItem(broot,'Bar Menu')
            self.TLCtrl1.SetItemText(grp_roots,0,str(r[0]))
            self.TLCtrl1.SetItemText(grp_roots, 1, r[1])
            self.TLCtrl1.SetItemText(grp_roots, 2, r[2])
            self.TLCtrl1.SetItemText(grp_roots, 3, r[3])
            items = self.MyMenu.ShowItem(r[0])
            #items = self.MyMenu.AmenuItm(r[0])
            print(items)
            for i in items:
                chditm = self.TLCtrl1.AppendItem(grp_roots,'Items Menu')
                self.TLCtrl1.SetItemText(chditm,0,str(i[1]))
                if i[3] == None or i[3] == '':
                    self.TLCtrl1.SetItemText(chditm, 1, '---')
                    self.TLCtrl1.SetItemText(chditm, 2, '---')
                else:
                    self.TLCtrl1.SetItemText(chditm, 1, str(i[3]))
                    self.TLCtrl1.SetItemText(chditm, 2, str(i[4]))
                #self.TLCtrl1.SetItemText(chditm, 3, str(i[4]))



        self.pnl1.SetSizer( Vsz2 )
        self.pnl1.Layout()
        Vsz2.Fit( self.pnl1 )
        self.pnl2 = wx.Panel( self.Spw1, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
        Vsz3 = wx.BoxSizer( wx.VERTICAL )

        self.btn1 = wx.Button( self.pnl2, wx.ID_ANY, u"Add", wx.DefaultPosition, wx.DefaultSize, 0 )
        Vsz3.Add( self.btn1, 0, wx.ALL, 5 )

        self.btn2 = wx.Button( self.pnl2, wx.ID_ANY, u"Edit", wx.DefaultPosition, wx.DefaultSize, 0 )
        Vsz3.Add( self.btn2, 0, wx.ALL, 5 )

        self.btn3 = wx.Button( self.pnl2, wx.ID_ANY, u"Delete", wx.DefaultPosition, wx.DefaultSize, 0 )
        Vsz3.Add( self.btn3, 0, wx.ALL, 5 )


        Vsz3.Add( ( 0, 0), 1, wx.EXPAND, 5 )

        self.btn4 = wx.Button( self.pnl2, wx.ID_ANY, u"Apply", wx.DefaultPosition, wx.DefaultSize, 0 )
        Vsz3.Add( self.btn4, 0, wx.ALL, 5 )


        self.pnl2.SetSizer( Vsz3 )
        self.pnl2.Layout()
        Vsz3.Fit( self.pnl2 )
        self.Spw1.SplitVertically( self.pnl1, self.pnl2, 532 )
        Vsz1.Add( self.Spw1, 1, wx.EXPAND, 5 )
        self.txt = stc.StyledTextCtrl()

        self.SetSizer( Vsz1 )
        self.Layout()

        # Connect Events
        self.TLCtrl1.Bind( wx.dataview.EVT_TREELIST_ITEM_CHECKED, self.DoshowItm )
        self.TLCtrl1.Bind( wx.dataview.EVT_TREELIST_ITEM_CONTEXT_MENU, self.Thismenu )
        self.btn1.Bind( wx.EVT_BUTTON, self.Additm )
        self.btn2.Bind( wx.EVT_BUTTON, self.edititm )
        self.btn3.Bind( wx.EVT_BUTTON, self.delitm )
        self.btn4.Bind( wx.EVT_BUTTON, self.aplyit )

    def __del__( self ):
        pass


    # Virtual event handlers, overide them in your derived class
    def DoshowItm( self, event ):
        print(event)
        event.Skip()

    def Thismenu( self, event ):
        print(event)
        event.Skip()

    def Additm( self, event ):
        self.Frm = wx.Frame(self, style=wx.CAPTION | wx.CLOSE_BOX | wx.FRAME_FLOAT_ON_PARENT | wx.TAB_TRAVERSAL)
        self.Pnl = MF.MyPanel1(self.Frm)
        self.Frm.SetSize((700,360))
        self.Frm.Show()
        #event.Skip()

    def edititm( self, event ):
        event.Skip()

    def delitm( self, event ):
        event.Skip()

    def aplyit( self, event ):
        event.Skip()

    def Spw1OnIdle( self, event ):
        self.Spw1.SetSashPosition( 532 )
        self.Spw1.Unbind( wx.EVT_IDLE )



