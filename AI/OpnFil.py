# -*- coding: utf-8 -*-


import wx
import wx.stc as stc

import keyword

if wx.Platform == '__WXMSW__':
    faces = {'times': 'Times New Roman',
             'mono': 'Courier New',
             'helv': 'Arial',
             'other': 'Comic Sans MS',
             'size': 10,
             'size2': 8,
             }
elif wx.Platform == '__WXMAC__':
    faces = {'times': 'Times New Roman',
             'mono': 'Monaco',
             'helv': 'Arial',
             'other': 'Comic Sans MS',
             'size': 12,
             'size2': 10,
             }
else:
    faces = {'times': 'Times',
             'mono': 'Courier',
             'helv': 'Helvetica',
             'other': 'new century schoolbook',
             'size': 12,
             'size2': 10,
             }


class PythonSTC(stc.StyledTextCtrl):
    fold_symbols = 2

    def __init__(self, parent, PyFile):
        stc.StyledTextCtrl.__init__(self, parent)

        self.CmdKeyAssign(ord('B'), stc.STC_SCMOD_CTRL, stc.STC_CMD_ZOOMIN)
        self.CmdKeyAssign(ord('N'), stc.STC_SCMOD_CTRL, stc.STC_CMD_ZOOMOUT)

        self.SetLexer(stc.STC_LEX_PYTHON)
        self.SetKeyWords(0, " ".join(keyword.kwlist))

        self.SetProperty("fold", "1")
        self.SetProperty("tab.timmy.whinge.level", "1")
        self.SetMargins(0, 0)

        self.SetViewWhiteSpace(False)
        # self.SetBufferedDraw(False)
        # self.SetViewEOL(True)
        # self.SetEOLMode(stc.STC_EOL_CRLF)
        # self.SetUseAntiAliasing(True)

        # Global default styles for all languages
        self.StyleSetSpec(stc.STC_STYLE_DEFAULT, "face:%(helv)s,size:%(size)d" % faces)
        self.StyleClearAll()  # Reset all to be like the default

        # Global default styles for all languages
        self.StyleSetSpec(stc.STC_STYLE_DEFAULT, "face:%(helv)s,size:%(size)d" % faces)
        self.StyleSetSpec(stc.STC_STYLE_LINENUMBER, "back:#C0C0C0,face:%(helv)s,size:%(size2)d" % faces)
        self.StyleSetSpec(stc.STC_STYLE_CONTROLCHAR, "face:%(other)s" % faces)
        self.StyleSetSpec(stc.STC_STYLE_BRACELIGHT, "fore:#FFFFFF,back:#0000FF,bold")
        self.StyleSetSpec(stc.STC_STYLE_BRACEBAD, "fore:#000000,back:#FF0000,bold")

        # Python styles
        # Default
        self.StyleSetSpec(stc.STC_P_DEFAULT, "fore:#000000,face:%(helv)s,size:%(size)d" % faces)
        # Comments
        self.StyleSetSpec(stc.STC_P_COMMENTLINE, "fore:#007F00,face:%(other)s,size:%(size)d" % faces)
        # Number
        self.StyleSetSpec(stc.STC_P_NUMBER, "fore:#007F7F,size:%(size)d" % faces)
        # String
        self.StyleSetSpec(stc.STC_P_STRING, "fore:#7F007F,face:%(helv)s,size:%(size)d" % faces)
        # Single quoted string
        self.StyleSetSpec(stc.STC_P_CHARACTER, "fore:#7F007F,face:%(helv)s,size:%(size)d" % faces)
        # Keyword
        self.StyleSetSpec(stc.STC_P_WORD, "fore:#00007F,bold,size:%(size)d" % faces)
        # Triple quotes
        self.StyleSetSpec(stc.STC_P_TRIPLE, "fore:#7F0000,size:%(size)d" % faces)
        # Triple double quotes
        self.StyleSetSpec(stc.STC_P_TRIPLEDOUBLE, "fore:#7F0000,size:%(size)d" % faces)
        # Class name definition
        self.StyleSetSpec(stc.STC_P_CLASSNAME, "fore:#0000FF,bold,underline,size:%(size)d" % faces)
        # Function or method name definition
        self.StyleSetSpec(stc.STC_P_DEFNAME, "fore:#007F7F,bold,size:%(size)d" % faces)
        # Operators
        self.StyleSetSpec(stc.STC_P_OPERATOR, "bold,size:%(size)d" % faces)
        # Identifiers
        self.StyleSetSpec(stc.STC_P_IDENTIFIER, "fore:#000000,face:%(helv)s,size:%(size)d" % faces)
        # Comment-blocks
        self.StyleSetSpec(stc.STC_P_COMMENTBLOCK, "fore:#7F7F7F,size:%(size)d" % faces)
        # End of line where string is not closed
        self.StyleSetSpec(stc.STC_P_STRINGEOL, "fore:#000000,face:%(mono)s,back:#E0C0E0,eol,size:%(size)d" % faces)

        self.SetCaretForeground("BLUE")

        # register some images for use in the AutoComplete box.
        # self.RegisterImage(1, images.Smiles.GetBitmap())
        # self.RegisterImage(2,
        #    wx.ArtProvider.GetBitmap(wx.ART_NEW, size=(16,16)))
        # self.RegisterImage(3,
        #    wx.ArtProvider.GetBitmap(wx.ART_COPY, size=(16,16)))

        with open(PyFile) as fobj:
            text = fobj.read()

        self.SetText(text)


'''
class PyPanel(wx.Panel):

	def __init__(self, parent, pyFile, style = wx.TAB_TRAVERSAL, name = wx.EmptyString):
		wx.Panel.__init__(self, parent, style = style, name = name )

		sizer0 = wx.BoxSizer(wx.VERTICAL)

		self.py_view = PythonSTC(self,pyFile)

		sizer1 = wx.BoxSizer(wx.VERTICAL)
		sizer1.Add(self.py_view, 1, wx.EXPAND, 5)

		sizer0.Add(sizer1, 1, wx.EXPAND, 5)

		sizer2 = wx.BoxSizer(wx.HORIZONTAL)

		self.Btn1 = wx.Button(self, wx.ID_ANY, u"Ok", wx.DefaultPosition, wx.DefaultSize, 0)
		sizer2.Add(self.Btn1, 0, wx.EXPAND, 5)

		self.Btn2 = wx.Button(self, wx.ID_ANY, u"Ok", wx.DefaultPosition, wx.DefaultSize, 0)
		sizer2.Add(self.Btn2, 0, wx.EXPAND, 5)

		sizer0.Add(sizer2, 0, wx.EXPAND, 5)

		self.SetSizer(sizer0)
		self.Layout()
'''


###########################################################################
## Class MyPanel1
###########################################################################

class PyPanel(wx.Panel):

    def __init__(self, parent, pyFile, id=wx.ID_ANY, pos=wx.DefaultPosition, size=wx.Size(680, 465),
                 style=wx.TAB_TRAVERSAL, name=wx.EmptyString):
        wx.Panel.__init__(self, parent, id=id, pos=pos, size=size, style=style, name=name)

        Vz1 = wx.BoxSizer(wx.VERTICAL)

        Hz1 = wx.BoxSizer(wx.HORIZONTAL)

        self.py_view = PythonSTC(self, pyFile)

        Hz1.Add(self.py_view, 1, wx.EXPAND | wx.ALL, 5)

        Vz2 = wx.BoxSizer(wx.VERTICAL)

        self.btn3 = wx.Button(self, wx.ID_ANY, u"SelectAll", wx.DefaultPosition, wx.DefaultSize, 0)
        Vz2.Add(self.btn3, 0, wx.ALL, 5)

        self.btn4 = wx.Button(self, wx.ID_ANY, u"Copy", wx.DefaultPosition, wx.DefaultSize, 0)
        Vz2.Add(self.btn4, 0, wx.ALL, 5)

        self.btn5 = wx.Button(self, wx.ID_ANY, u"Paste", wx.DefaultPosition, wx.DefaultSize, 0)
        Vz2.Add(self.btn5, 0, wx.ALL, 5)

        Vz2.Add((0, 0), 1, wx.EXPAND, 5)

        self.btn1 = wx.Button(self, wx.ID_ANY, u"save", wx.DefaultPosition, wx.DefaultSize, 0)
        Vz2.Add(self.btn1, 0, wx.ALL, 5)

        self.btn2 = wx.Button(self, wx.ID_ANY, u"close", wx.DefaultPosition, wx.DefaultSize, 0)
        Vz2.Add(self.btn2, 0, wx.ALL, 5)

        Hz1.Add(Vz2, 0, wx.EXPAND, 5)

        Vz1.Add(Hz1, 1, wx.EXPAND, 5)

        self.SetSizer(Vz1)
        self.Layout()

        # Connect Events
        self.btn3.Bind(wx.EVT_BUTTON, self.slctal)
        self.btn4.Bind(wx.EVT_BUTTON, self.cpyslct)
        self.btn5.Bind(wx.EVT_BUTTON, self.pstslct)
        self.btn1.Bind(wx.EVT_BUTTON, self.svefil)
        self.btn2.Bind(wx.EVT_BUTTON, self.clos)

    def __del__(self):
        pass

    # Virtual event handlers, overide them in your derived class
    def slctal(self, event):
        event.Skip()

    def cpyslct(self, event):
        event.Skip()

    def pstslct(self, event):
        event.Skip()

    def svefil(self, event):
        event.Skip()

    def clos(self, event):
        q = self.GetParent()
        q.Close()
