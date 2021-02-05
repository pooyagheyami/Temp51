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

        VL = wx.BoxSizer(wx.VERTICAL)

        self.Line = wx.StaticLine(self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_HORIZONTAL)
        VL.Add(self.Line, 0, wx.EXPAND | wx.ALL, 5)

        Vsz1.Add(VL, 0, wx.EXPAND, 5)

        Hz1 = wx.BoxSizer(wx.HORIZONTAL)

        self.btna = wx.Button(self, wx.ID_ANY, u"New Bar", wx.DefaultPosition, wx.DefaultSize, 0)
        Hz1.Add(self.btna, 0, wx.ALL, 5)

        self.btnb = wx.Button(self, wx.ID_ANY, u"Change Bar", wx.DefaultPosition, wx.DefaultSize, 0)
        Hz1.Add(self.btnb, 0, wx.ALL, 5)

        self.btnc = wx.Button(self, wx.ID_ANY, u"Delete Bar", wx.DefaultPosition, wx.DefaultSize, 0)
        Hz1.Add(self.btnc, 0, wx.ALL, 5)

        Vsz1.Add(Hz1, 0, wx.EXPAND, 5)

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
        self.btna.Bind(wx.EVT_BUTTON, self.Nbar)
        self.btnb.Bind(wx.EVT_BUTTON, self.Cbar)
        self.btnc.Bind(wx.EVT_BUTTON, self.Dbar)

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

    def Nbar(self, event):
        self.Frm = wx.Dialog(self)
        self.Pnl = MyPanel3(self.Frm)
        self.Frm.SetSize((500, 180))
        self.Frm.ShowModal()
        self.Frm.Destroy()

    def Cbar(self, event):
        self.Frm = wx.Dialog(self)
        self.Pnl = MyPanel3(self.Frm)
        self.Frm.SetSize((500, 180))
        self.Frm.ShowModal()
        self.Frm.Destroy()

    def Dbar(self, event):
        self.Frm = wx.Dialog(self)
        self.Pnl = MyPanel3(self.Frm)
        self.Frm.SetSize((500, 180))
        self.Frm.ShowModal()
        self.Frm.Destroy()

    def Spw1OnIdle( self, event ):
        self.Spw1.SetSashPosition( 532 )
        self.Spw1.Unbind( wx.EVT_IDLE )



###########################################################################
## Class MyPanel3
###########################################################################

class MyPanel3 ( wx.Panel ):

    def __init__( self, parent, id = wx.ID_ANY, pos = wx.DefaultPosition, size = wx.Size( 500,180 ), style = wx.TAB_TRAVERSAL, name = wx.EmptyString ):
        wx.Panel.__init__ ( self, parent, id = id, pos = pos, size = size, style = style, name = name )

        bSizer8 = wx.BoxSizer( wx.VERTICAL )

        bSizer9 = wx.BoxSizer( wx.HORIZONTAL )

        self.m_staticText11 = wx.StaticText( self, wx.ID_ANY, u"Bar name", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText11.Wrap( -1 )

        bSizer9.Add( self.m_staticText11, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

        self.m_textCtrl8 = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
        bSizer9.Add( self.m_textCtrl8, 1, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )


        bSizer8.Add( bSizer9, 1, wx.EXPAND, 5 )

        bSizer10 = wx.BoxSizer( wx.HORIZONTAL )

        self.m_staticText12 = wx.StaticText( self, wx.ID_ANY, u"Directory", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText12.Wrap( -1 )

        bSizer10.Add( self.m_staticText12, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

        self.m_dirPicker2 = wx.DirPickerCtrl( self, wx.ID_ANY, wx.EmptyString, u"Select a folder", wx.DefaultPosition, wx.DefaultSize, wx.DIRP_DEFAULT_STYLE|wx.DIRP_SMALL )
        bSizer10.Add( self.m_dirPicker2, 1, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )


        bSizer8.Add( bSizer10, 1, wx.EXPAND, 5 )

        bSizer11 = wx.BoxSizer( wx.HORIZONTAL )

        self.m_checkBox3 = wx.CheckBox( self, wx.ID_ANY, u"Disable", wx.DefaultPosition, wx.DefaultSize, 0 )
        bSizer11.Add( self.m_checkBox3, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

        self.m_checkBox4 = wx.CheckBox( self, wx.ID_ANY, u"Hiden", wx.DefaultPosition, wx.DefaultSize, 0 )
        bSizer11.Add( self.m_checkBox4, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )


        bSizer8.Add( bSizer11, 0, wx.ALIGN_CENTER_HORIZONTAL, 5 )

        bSizer12 = wx.BoxSizer( wx.HORIZONTAL )


        bSizer12.Add( ( 0, 0), 1, wx.EXPAND, 5 )

        self.m_button21 = wx.Button( self, wx.ID_ANY, u"Cancle", wx.DefaultPosition, wx.DefaultSize, 0 )
        bSizer12.Add( self.m_button21, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

        self.m_button19 = wx.Button( self, wx.ID_ANY, u"Change", wx.DefaultPosition, wx.DefaultSize, 0 )
        bSizer12.Add( self.m_button19, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

        self.m_button20 = wx.Button( self, wx.ID_ANY, u"Add", wx.DefaultPosition, wx.DefaultSize, 0 )
        bSizer12.Add( self.m_button20, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )


        bSizer8.Add( bSizer12, 1, wx.EXPAND, 5 )


        self.SetSizer( bSizer8 )
        self.Layout()

        # Connect Events
        self.m_dirPicker2.Bind( wx.EVT_DIRPICKER_CHANGED, self.bardir )
        self.m_checkBox3.Bind( wx.EVT_CHECKBOX, self.disbar )
        self.m_checkBox4.Bind( wx.EVT_CHECKBOX, self.hidbar )
        self.m_button21.Bind( wx.EVT_BUTTON, self.cancl )
        self.m_button19.Bind( wx.EVT_BUTTON, self.chngbar )
        self.m_button20.Bind( wx.EVT_BUTTON, self.addbar )

    def __del__( self ):
        pass


    # Virtual event handlers, overide them in your derived class
    def bardir( self, event ):
        event.Skip()

    def disbar( self, event ):
        event.Skip()

    def hidbar( self, event ):
        event.Skip()

    def cancl( self, event ):
        q = self.GetParent()
        q.Close()
        #event.Skip()

    def chngbar( self, event ):
        event.Skip()

    def addbar( self, event ):
        event.Skip()
