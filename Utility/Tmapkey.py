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
import wx.dataview as dv
#import tamil
import os

###########################################################################
## Class MyPanel3
###########################################################################

class MpPanel1 ( wx.Panel ):

	def __init__( self, parent, id = wx.ID_ANY, pos = wx.DefaultPosition, size = wx.Size( 627,214 ), style = wx.TAB_TRAVERSAL, name = wx.EmptyString ):
		wx.Panel.__init__ ( self, parent, id = id, pos = pos, size = size, style = style, name = name )

                self.itext = ''
                self.MyMap = getmap.GetMapKey()

                self.MyMap.Loadmap(u"./Map1")
                self.init()

		bSizer1 = wx.BoxSizer( wx.VERTICAL )

		bSizer2 = wx.BoxSizer( wx.HORIZONTAL )

		self.kbtn1 = []
		i = 0
		#self.row1 = self.MyMap.row1
		#self.srow1 = self.MyMap.srow1

		for ky in self.row1:
                    self.kbtn1.append( wx.TextCtrl( self, 100+i, ky, wx.DefaultPosition, wx.Size( 35,-1 ), 0 ) )
                    self.kbtn1[i].SetMaxLength(1)
                    bSizer2.Add( self.kbtn1[i], 0, wx.EXPAND, 5 )
                    #self.kbtn1[i].Bind(  wx.EVT_SET_FOCUS, self.r )
                    self.kbtn1[i].Bind( wx.EVT_TEXT, self.chng )
                    i += 1

                
                self.bbck = wx.Button( self, wx.ID_ANY, u"Back", wx.DefaultPosition, wx.Size( 55,-1 ), 0 )
		bSizer2.Add( self.bbck, 1, wx.EXPAND, 5 )

		bSizer1.Add( bSizer2, 1, wx.EXPAND, 5 )

		bSizer3 = wx.BoxSizer( wx.HORIZONTAL )

		self.bnxt = wx.Button( self, wx.ID_ANY, u"Next", wx.DefaultPosition, wx.Size( 45,-1 ), wx.BU_EXACTFIT )
		bSizer3.Add( self.bnxt, 0, wx.EXPAND, 5 )

                self.kbtn2 = []
                i = 0
                #self.row2 = self.MyMap.row2
                #self.srow2 = self.MyMap.srow2
		for ky in self.row2:
                    self.kbtn2.append(wx.TextCtrl( self, 200+i, ky, wx.DefaultPosition, wx.Size( 35,-1 ), 0 ))
                    self.kbtn2[i].SetMaxLength(1)
                    bSizer3.Add( self.kbtn2[i], 1, wx.EXPAND, 5 )
                    #self.kbtn2[i].Bind(  wx.EVT_SET_FOCUS, self.r )
                    self.kbtn2[i].Bind( wx.EVT_TEXT, self.chng )
                    i += 1

                

		self.blod = wx.Button( self, wx.ID_ANY, u"Load", wx.DefaultPosition, wx.Size( 55,-1 ), 0 )
		bSizer3.Add( self.blod, 0, wx.EXPAND, 5 )


		bSizer1.Add( bSizer3, 1, wx.EXPAND, 5 )

		bSizer4 = wx.BoxSizer( wx.HORIZONTAL )

		self.bcps = wx.Button( self, wx.ID_ANY, u"Caps Lock", wx.DefaultPosition, wx.Size( 60,-1 ), wx.BU_EXACTFIT )
		bSizer4.Add( self.bcps, 0, wx.EXPAND, 5 )

		self.kbtn3 = []
                i = 0
                #self.row3 = self.MyMap.row3
                #self.srow3 = self.MyMap.srow3
		for ky in self.row3:
                    self.kbtn3.append(wx.TextCtrl( self, 300+i, ky, wx.DefaultPosition, wx.Size( 35,-1 ), 0 ))
                    self.kbtn3[i].SetMaxLength(1)
                    bSizer4.Add( self.kbtn3[i], 1, wx.EXPAND, 5 )
                    #self.kbtn3[i].Bind(  wx.EVT_SET_FOCUS, self.r )
                    self.kbtn3[i].Bind( wx.EVT_TEXT, self.chng )
                    i += 1

                
		

		self.bsav = wx.Button( self, wx.ID_ANY, u"Save", wx.DefaultPosition, wx.Size( 85,-1 ), 0 )
		bSizer4.Add( self.bsav, 0, wx.EXPAND, 5 )


		bSizer1.Add( bSizer4, 1, wx.EXPAND, 5 )

		bSizer5 = wx.BoxSizer( wx.HORIZONTAL )

		

		self.bshft1 = wx.ToggleButton( self, wx.ID_ANY, u"Shift", wx.DefaultPosition, wx.Size( 80,-1 ), 0 )
		bSizer5.Add( self.bshft1, 1, wx.EXPAND, 5 )

		self.kbtn4 = []
                i = 0
                #self.row4 = self.MyMap.row4
                #self.srow4 = self.MyMap.srow4
		for ky in self.row4:
                    self.kbtn4.append(wx.TextCtrl( self, 400+i, ky, wx.DefaultPosition, wx.Size( 35,-1 ), 0 ))
                    self.kbtn4[i].SetMaxLength(1)
                    bSizer5.Add( self.kbtn4[i], 1, wx.EXPAND, 5 )
                    #self.kbtn4[i].Bind(  wx.EVT_SET_FOCUS, self.r )
                    self.kbtn4[i].Bind( wx.EVT_TEXT, self.chng )
                    i += 1

                

		self.bshft2 = wx.ToggleButton( self, wx.ID_ANY, u"Shift", wx.DefaultPosition, wx.Size( 95,-1 ), 0 )
		bSizer5.Add( self.bshft2, 1, wx.EXPAND, 5 )


		bSizer1.Add( bSizer5, 1, wx.EXPAND, 5 )

		bSizer6 = wx.BoxSizer( wx.HORIZONTAL )

		self.bctrl1 = wx.Button( self, wx.ID_ANY, u"Ctrl", wx.DefaultPosition, wx.Size( 60,-1 ), wx.BU_EXACTFIT )
		bSizer6.Add( self.bctrl1, 1, wx.EXPAND, 5 )

		self.balt1 = wx.Button( self, wx.ID_ANY, u"Alt", wx.DefaultPosition, wx.DefaultSize, wx.BU_EXACTFIT )
		bSizer6.Add( self.balt1, 1, wx.EXPAND, 5 )

		self.bSpec = wx.Button( self, wx.ID_ANY, u"Back", wx.DefaultPosition, wx.Size( 275,-1 ), 0 )
		bSizer6.Add( self.bSpec, 1, wx.EXPAND, 5 )

		self.balt2 = wx.Button( self, wx.ID_ANY, u"Alt", wx.DefaultPosition, wx.DefaultSize, wx.BU_EXACTFIT )
		bSizer6.Add( self.balt2, 1, wx.EXPAND, 5 )

		self.bcomd = wx.Button( self, 900, u"Win", wx.DefaultPosition, wx.DefaultSize, wx.BU_EXACTFIT )
		bSizer6.Add( self.bcomd, 1, wx.EXPAND, 5 )

		self.bctrl2 = wx.Button( self, wx.ID_ANY, u"Ctrl", wx.DefaultPosition, wx.Size( 60,-1 ), 0 )
		bSizer6.Add( self.bctrl2, 1, wx.EXPAND, 5 )


		bSizer1.Add( bSizer6, 1, wx.EXPAND, 5 )


		self.SetSizer( bSizer1 )
		self.Layout()

		#self.mychr = u''
		
		# Connect Events
		self.bbck.Bind( wx.EVT_BUTTON, self.bak )
		
		self.bnxt.Bind( wx.EVT_BUTTON, self.nxt )
		self.blod.Bind( wx.EVT_BUTTON, self.lod )
		self.bcps.Bind( wx.EVT_BUTTON, self.casp )
		self.bsav.Bind( wx.EVT_BUTTON, self.sav )
		self.bshft1.Bind( wx.EVT_TOGGLEBUTTON, self.shft )
		self.bshft2.Bind( wx.EVT_TOGGLEBUTTON, self.shft )
		self.bctrl1.Bind( wx.EVT_BUTTON, self.ctl )
		#self.balt1.Bind( wx.EVT_BUTTON, self.alt )
		self.bSpec.Bind( wx.EVT_BUTTON, self.spc )
		#self.balt2.Bind( wx.EVT_BUTTON, self.alt )
		self.bcomd.Bind( wx.EVT_BUTTON, self.exp )
		self.bctrl2.Bind( wx.EVT_BUTTON, self.ctl )

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
                
	def tonxt( self, event ):
		print event

	def chng( self, event ):
		mid = event.GetEventObject().GetId()
		#print mid
		if mid//100 == 1 :
                        if  (self.bshft1.GetValue() or self.bshft2.GetValue()):
                                self.srow1[mid%100] = event.GetEventObject().GetValue()
                        else:
                                self.row1[mid%100] = event.GetEventObject().GetValue()
                if mid//100 == 2 :
                        if (self.bshft1.GetValue() or self.bshft2.GetValue()):
                                self.srow2[mid%100] = event.GetEventObject().GetValue()
                        else:
                                self.row2[mid%100] = event.GetEventObject().GetValue()
                                
                if mid//100 == 3 :
                        if (self.bshft1.GetValue() or self.bshft2.GetValue()):
                                self.srow3[mid%100] = event.GetEventObject().GetValue()
                        else:
                                self.row3[mid%100] = event.GetEventObject().GetValue()
                                
                if mid//100 == 4 :
                        if (self.bshft1.GetValue() or self.bshft2.GetValue()):
                                self.srow4[mid%100] = event.GetEventObject().GetValue()
                        else:
                                self.row4[mid%100] = event.GetEventObject().GetValue()        
                        
                        

	def bak( self, event ):
		pass
	def nxt( self, event ):
		event.Skip()

	def lod( self, event ):
		iwin = wx.Dialog(self,-1)
		pnl = MyPanel2(iwin)
		iwin.SetSize((200,300))
		iwin.ShowModal()

		f = pnl.Iselct()
		#print os.getcwd()+u'/'+f
		self.MyMap = getmap.GetMapKey()
		self.MyMap.Loadmap(os.getcwd()+u'/'+f)
		self.init()

		self.Refresh()
		self.Layout()
		iwin.Destroy()

	def casp( self, event ):
		event.Skip()

	def sav( self, event ):
		iwin = wx.Dialog(self,-1)
		pnl = MyPanel3(iwin)
		iwin.SetSize((280,350))
		iwin.ShowModal()

		if pnl.Doit :
                        myfile = pnl.Getfilename()
                        Mydata = self.GetKeyData()
                        self.MyMap.Savemap(myfile,Mydata)

		self.Refresh()
		self.Layout()
		iwin.Destroy()
		

	def GetKeyData( self ):
                Data = []
                for c in self.row1:
                        Data.append(c+u'\n')
                for c in self.row2:
                        Data.append(c+u'\n')
                for c in self.row3:
                        Data.append(c+u'\n')
                for c in self.row4:
                        Data.append(c+u'\n')
                for c in self.srow1:
                        Data.append(c+u'\n')
                for c in self.srow2:
                        Data.append(c+u'\n')
                for c in self.srow3:
                        Data.append(c+u'\n')
                for c in self.srow4:
                        Data.append(c+u'\n')
                return Data        

	def shft( self, event ):
                
		if self.bshft1.GetValue() or self.bshft2.GetValue():
                        self.Updatekey(True)
                else:
                        self.Updatekey(False)


	def ctl( self, event ):
		event.Skip()

	def alt( self, event ):
                
		iwin = wx.Dialog(self,-1)
		pnl = MyPanel4(iwin)
		iwin.SetSize((200,300))
		iwin.ShowModal()

		self.mychr = pnl.retdata()
		#print self.mychr
				

		self.Refresh()
		self.Layout()
		iwin.Destroy()

	def r( self , event ):
                event.GetEventObject().SetValue(self.mychr)
                #print event.GetEventObject().GetValue()
                #print event.GetEventObject().GetId()

	def spc( self, event ):
		q = self.GetParent()
                q.Close()


	def exp( self, event ):
		event.Skip()


	
	def onkey( self, event ):
		return event.GetEventObject().GetLabel()
	
                    
        def Updatekey(self,shift):
                if shift :
                        i = 0
                        for lbl in self.srow1:
                                self.kbtn1[i].SetValue(lbl)
                                i += 1
                        i = 0        
                        for lbl in self.srow2:
                                self.kbtn2[i].SetValue(lbl)
                                i += 1
                        i = 0        
                        for lbl in self.srow3:
                                self.kbtn3[i].SetValue(lbl)
                                i += 1
                        i = 0        
                        for lbl in self.srow4:
                                self.kbtn4[i].SetValue(lbl)
                                i += 1
                else:
                        i = 0
                        for lbl in self.row1:
                                self.kbtn1[i].SetValue(lbl)
                                i += 1
                        i = 0        
                        for lbl in self.row2:
                                self.kbtn2[i].SetValue(lbl)
                                i += 1
                        i = 0        
                        for lbl in self.row3:
                                self.kbtn3[i].SetValue(lbl)
                                i += 1
                        i = 0        
                        for lbl in self.row4:
                                self.kbtn4[i].SetValue(lbl)
                                i += 1
	
                self.Refresh()
		self.Layout()






###########################################################################
## Class MyPanel2
###########################################################################

class MyPanel2 ( wx.Panel ):

	def __init__( self, parent, id = wx.ID_ANY, pos = wx.DefaultPosition, size = wx.Size( 209,300 ), style = wx.TAB_TRAVERSAL, name = wx.EmptyString ):
		wx.Panel.__init__ ( self, parent, id = id, pos = pos, size = size, style = style, name = name )

		Hsz1 = wx.BoxSizer( wx.VERTICAL )

		self.DVLC1 = dv.DataViewListCtrl( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.Col1 = self.DVLC1.AppendTextColumn( u"Name", dv.DATAVIEW_CELL_INERT, -1, wx.ALIGN_LEFT, dv.DATAVIEW_COL_RESIZABLE )
		self.Col2 = self.DVLC1.AppendTextColumn( u"Size",width = 10)
		Hsz1.Add( self.DVLC1, 1, wx.ALL|wx.EXPAND, 5 )

		for f in os.listdir(os.getcwd()):
                        if '.' not in f:
                                if os.path.getsize(os.getcwd()+'/'+f) < 1000 :
                                        D = (f,str(os.path.getsize(os.getcwd()+'/'+f)))
                                        self.DVLC1.AppendItem(D)


		self.SetSizer( Hsz1 )
		self.Layout()

		self.myselct = u''

		# Connect Events
		#self.DVLC1.Bind( dv.EVT_DATAVIEW_ITEM_ACTIVATED, self.doselct, id = wx.ID_ANY )
		self.DVLC1.Bind( dv.EVT_DATAVIEW_SELECTION_CHANGED, self.doselct, id = wx.ID_ANY )

	def __del__( self ):
		pass


	# Virtual event handlers, overide them in your derived class
	def doselct( self, event ):
		r  = self.DVLC1.GetSelectedRow()
		self.myselct =  unicode(self.DVLC1.GetValue(r,0))
		

	def Iselct ( self ):
                return self.myselct





###########################################################################
## Class MyPanel3
###########################################################################

class MyPanel3 ( wx.Panel ):

	def __init__( self, parent, id = wx.ID_ANY, pos = wx.DefaultPosition, size = wx.Size( 279,353 ), style = wx.TAB_TRAVERSAL, name = wx.EmptyString ):
		wx.Panel.__init__ ( self, parent, id = id, pos = pos, size = size, style = style, name = name )

		Bsz1 = wx.BoxSizer( wx.VERTICAL )

		self.txt1 = wx.StaticText( self, wx.ID_ANY, u"Name of Map that create it", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.txt1.Wrap( -1 )

		Bsz1.Add( self.txt1, 0, wx.ALL, 5 )

		self.file1 = wx.FilePickerCtrl( self, wx.ID_ANY, wx.EmptyString, u"Save a file", u"*.*", wx.DefaultPosition, wx.DefaultSize, wx.FLP_OVERWRITE_PROMPT|wx.FLP_SAVE|wx.FLP_USE_TEXTCTRL )
		Bsz1.Add( self.file1, 0, wx.ALL|wx.EXPAND, 5 )

		MaplistChoices = []
		self.Maplist = wx.CheckListBox( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, MaplistChoices, 0 )
		Bsz1.Add( self.Maplist, 1, wx.ALL|wx.EXPAND, 5 )

		Bsz2 = wx.BoxSizer( wx.HORIZONTAL )

		self.m_button1 = wx.Button( self, wx.ID_ANY, u"Cancel", wx.DefaultPosition, wx.DefaultSize, 0 )
		Bsz2.Add( self.m_button1, 0, wx.ALL, 5 )

		self.m_button2 = wx.Button( self, wx.ID_ANY, u"Save", wx.DefaultPosition, wx.DefaultSize, 0 )
		Bsz2.Add( self.m_button2, 0, wx.ALL, 5 )


		Bsz1.Add( Bsz2, 0, wx.ALIGN_RIGHT, 5 )


		self.SetSizer( Bsz1 )
		self.Layout()

		# Connect Events
		self.file1.Bind( wx.EVT_FILEPICKER_CHANGED, self.myfile )
		self.m_button1.Bind( wx.EVT_BUTTON, self.cancl )
		self.m_button2.Bind( wx.EVT_BUTTON, self.savit )

	def __del__( self ):
		pass


	# Virtual event handlers, overide them in your derived class
	def myfile( self, event ):
		self.thisfile = self.file1.GetTextCtrlValue()

	def cancl( self, event ):
                self.Doit = False
		q = self.GetParent()
		q.Close()

	def savit( self, event ):
                self.Doit = True
		q = self.GetParent()
		q.Close()

	def Getfilename( self ):
                if self.thisfile == u'':
                        wx.MessageBox(u"Please enter file name")
                else:
                        return self.thisfile 

        def Getmapdata( self) :
                
                pass


###########################################################################
## Class MyPanel4
###########################################################################

class MyPanel4 ( wx.Panel ):

	def __init__( self, parent, id = wx.ID_ANY, pos = wx.DefaultPosition, size = wx.Size( 211,300 ), style = wx.TAB_TRAVERSAL, name = wx.EmptyString ):
		wx.Panel.__init__ ( self, parent, id = id, pos = pos, size = size, style = style, name = name )

		Vsz1 = wx.BoxSizer( wx.VERTICAL )

		self.DVC1 = dv.DataViewListCtrl( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.Col1 = self.DVC1.AppendTextColumn( u"Code", dv.DATAVIEW_CELL_INERT, -1, wx.ALIGN_LEFT, dv.DATAVIEW_COL_RESIZABLE )
		self.Col2 = self.DVC1.AppendTextColumn( u"Char", dv.DATAVIEW_CELL_INERT, -1, wx.ALIGN_LEFT, dv.DATAVIEW_COL_RESIZABLE )
		Vsz1.Add( self.DVC1, 1, wx.ALL|wx.EXPAND, 5 )

		for d in tamil.utf8.tamil_letters:
                        if len(d) <= 1:
                                C = (unicode(d),d)
                                self.DVC1.AppendItem(C)
                        
                #for c in  self.DVC1.Columns:

                #        c.Sortable = True

                #        c.Reorderable = True

		self.SetSizer( Vsz1 )
		self.Layout()

		# Connect Events
		self.DVC1.Bind( dv.EVT_DATAVIEW_ITEM_ACTIVATED, self.dochos, id = wx.ID_ANY )

	def __del__( self ):
		pass


	# Virtual event handlers, overide them in your derived class
	def dochos( self, event ):
		a = self.DVC1.GetSelectedRow()
		#print a
		self.retdata()
		q = self.GetParent()
		q.Close()

	def retdata(self):
                a = self.DVC1.GetSelectedRow()
                
                if a == -1:
                        return u''
                else:
                        return unicode(self.DVC1.GetValue(a,1))


