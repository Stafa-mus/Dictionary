# -*- coding: utf-8 -*-

###########################################################################
## Python code generated with wxFormBuilder (version 3.10.0-4761b0c)
## http://www.wxformbuilder.org/
##
## PLEASE DO *NOT* EDIT THIS FILE!
###########################################################################

import wx
import wx.xrc
import wx.richtext

###########################################################################
## Class Dictionary
###########################################################################

class Dictionary ( wx.Frame ):

	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = u"The Dictionary", pos = wx.DefaultPosition, size = wx.Size( 610,437 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )

		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )

		bSizer1 = wx.BoxSizer( wx.VERTICAL )

		self.m_panel1 = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizer2 = wx.BoxSizer( wx.VERTICAL )

		bSizer3 = wx.BoxSizer( wx.HORIZONTAL )

		self.m_textCtrlWord = wx.TextCtrl( self.m_panel1, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.TE_PROCESS_ENTER )
		bSizer3.Add( self.m_textCtrlWord, 1, wx.ALL, 5 )

		self.m_bpButtonPrevious = wx.BitmapButton( self.m_panel1, wx.ID_ANY, wx.NullBitmap, wx.DefaultPosition, wx.DefaultSize, wx.BU_AUTODRAW|0 )

		self.m_bpButtonPrevious.SetBitmap( wx.Bitmap( u"assets/icons/16px/fast-rewind.bmp", wx.BITMAP_TYPE_ANY ) )
		self.m_bpButtonPrevious.SetToolTip( u"Previous word in history" )

		bSizer3.Add( self.m_bpButtonPrevious, 0, wx.ALL, 5 )

		self.m_bpButtonNext = wx.BitmapButton( self.m_panel1, wx.ID_ANY, wx.NullBitmap, wx.DefaultPosition, wx.DefaultSize, wx.BU_AUTODRAW|0 )

		self.m_bpButtonNext.SetBitmap( wx.Bitmap( u"assets/icons/16px/fast-forward.bmp", wx.BITMAP_TYPE_ANY ) )
		self.m_bpButtonNext.SetToolTip( u"Next word in history" )

		bSizer3.Add( self.m_bpButtonNext, 0, wx.ALL, 5 )

		self.m_bpButtonPronounce = wx.BitmapButton( self.m_panel1, wx.ID_ANY, wx.NullBitmap, wx.DefaultPosition, wx.DefaultSize, wx.BU_AUTODRAW|0 )

		self.m_bpButtonPronounce.SetBitmap( wx.Bitmap( u"assets/icons/16px/volume-up.bmp", wx.BITMAP_TYPE_ANY ) )
		self.m_bpButtonPronounce.SetToolTip( u"Pronunciation" )

		bSizer3.Add( self.m_bpButtonPronounce, 0, wx.ALL, 5 )

		self.m_bpButtonBookmark = wx.BitmapButton( self.m_panel1, wx.ID_ANY, wx.NullBitmap, wx.DefaultPosition, wx.DefaultSize, wx.BU_AUTODRAW|0 )

		self.m_bpButtonBookmark.SetBitmap( wx.Bitmap( u"assets/icons/16px/bookmark-border.bmp", wx.BITMAP_TYPE_ANY ) )
		self.m_bpButtonBookmark.SetToolTip( u"Add to bookmark" )

		bSizer3.Add( self.m_bpButtonBookmark, 0, wx.ALL, 5 )


		bSizer2.Add( bSizer3, 0, wx.EXPAND, 5 )

		self.m_richTextDefinition = wx.richtext.RichTextCtrl( self.m_panel1, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.TE_AUTO_URL|wx.TE_READONLY|wx.VSCROLL|wx.HSCROLL|wx.NO_BORDER|wx.WANTS_CHARS )
		bSizer2.Add( self.m_richTextDefinition, 1, wx.EXPAND |wx.ALL, 5 )


		self.m_panel1.SetSizer( bSizer2 )
		self.m_panel1.Layout()
		bSizer2.Fit( self.m_panel1 )
		bSizer1.Add( self.m_panel1, 1, wx.EXPAND, 5 )


		self.SetSizer( bSizer1 )
		self.Layout()
		self.m_menubar1 = wx.MenuBar( 0 )
		self.m_menu1 = wx.Menu()
		self.m_menuItemPreferences = wx.MenuItem( self.m_menu1, wx.ID_ANY, u"Preferences", u"Set application preferences", wx.ITEM_NORMAL )
		self.m_menu1.Append( self.m_menuItemPreferences )

		self.m_menuItemExit = wx.MenuItem( self.m_menu1, wx.ID_ANY, u"Exit", u"Close the application", wx.ITEM_NORMAL )
		self.m_menu1.Append( self.m_menuItemExit )

		self.m_menubar1.Append( self.m_menu1, u"File" )

		self.m_menu2 = wx.Menu()
		self.m_menuItemHelp = wx.MenuItem( self.m_menu2, wx.ID_ANY, u"Help"+ u"\t" + u"F1", u"Help on how to use this application", wx.ITEM_NORMAL )
		self.m_menu2.Append( self.m_menuItemHelp )

		self.m_menuItemAbout = wx.MenuItem( self.m_menu2, wx.ID_ANY, u"About"+ u"\t" + u"F2", u"About this applicatin", wx.ITEM_NORMAL )
		self.m_menu2.Append( self.m_menuItemAbout )

		self.m_menubar1.Append( self.m_menu2, u"Help" )

		self.SetMenuBar( self.m_menubar1 )

		self.m_statusBar = self.CreateStatusBar( 2, wx.STB_SIZEGRIP, wx.ID_ANY )

		self.Centre( wx.BOTH )

		# Connect Events
		self.m_textCtrlWord.Bind( wx.EVT_TEXT, self.OnTextTyped )
		self.m_textCtrlWord.Bind( wx.EVT_TEXT_ENTER, self.OnTextEnter )
		self.m_bpButtonPrevious.Bind( wx.EVT_BUTTON, self.OnPrevious )
		self.m_bpButtonNext.Bind( wx.EVT_BUTTON, self.OnNext )
		self.m_bpButtonPronounce.Bind( wx.EVT_BUTTON, self.OnPronounce )
		self.m_bpButtonBookmark.Bind( wx.EVT_BUTTON, self.OnBookmark )
		self.Bind( wx.EVT_MENU, self.OnPreferences, id = self.m_menuItemPreferences.GetId() )
		self.Bind( wx.EVT_MENU, self.OnExit, id = self.m_menuItemExit.GetId() )
		self.Bind( wx.EVT_MENU, self.OnHelp, id = self.m_menuItemHelp.GetId() )
		self.Bind( wx.EVT_MENU, self.OnAbout, id = self.m_menuItemAbout.GetId() )

	def __del__( self ):
		pass


	# Virtual event handlers, override them in your derived class
	def OnTextTyped( self, event ):
		event.Skip()

	def OnTextEnter( self, event ):
		event.Skip()

	def OnPrevious( self, event ):
		event.Skip()

	def OnNext( self, event ):
		event.Skip()

	def OnPronounce( self, event ):
		event.Skip()

	def OnBookmark( self, event ):
		event.Skip()

	def OnPreferences( self, event ):
		event.Skip()

	def OnExit( self, event ):
		event.Skip()

	def OnHelp( self, event ):
		event.Skip()

	def OnAbout( self, event ):
		event.Skip()


###########################################################################
## Class Settings
###########################################################################

class Settings ( wx.Dialog ):

	def __init__( self, parent ):
		wx.Dialog.__init__ ( self, parent, id = wx.ID_ANY, title = u"Settings", pos = wx.DefaultPosition, size = wx.Size( 422,343 ), style = wx.DEFAULT_DIALOG_STYLE )

		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )

		bSizer4 = wx.BoxSizer( wx.VERTICAL )

		self.m_notebook1 = wx.Notebook( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_panel2 = wx.Panel( self.m_notebook1, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizer5 = wx.BoxSizer( wx.VERTICAL )

		self.m_scrolledWindow2 = wx.ScrolledWindow( self.m_panel2, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.HSCROLL|wx.VSCROLL )
		self.m_scrolledWindow2.SetScrollRate( 5, 5 )
		bSizer6 = wx.BoxSizer( wx.VERTICAL )

		self.m_checkBox1 = wx.CheckBox( self.m_scrolledWindow2, wx.ID_ANY, u"Search online if definition is not found", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer6.Add( self.m_checkBox1, 0, wx.ALL, 5 )

		self.m_checkBox2 = wx.CheckBox( self.m_scrolledWindow2, wx.ID_ANY, u"Download pronunciations automatically", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer6.Add( self.m_checkBox2, 0, wx.ALL, 5 )

		self.m_checkBox3 = wx.CheckBox( self.m_scrolledWindow2, wx.ID_ANY, u"Check for updates automatically", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer6.Add( self.m_checkBox3, 0, wx.ALL, 5 )

		self.m_checkBox4 = wx.CheckBox( self.m_scrolledWindow2, wx.ID_ANY, u"Download and install updates automatically", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer6.Add( self.m_checkBox4, 0, wx.ALL, 5 )


		self.m_scrolledWindow2.SetSizer( bSizer6 )
		self.m_scrolledWindow2.Layout()
		bSizer6.Fit( self.m_scrolledWindow2 )
		bSizer5.Add( self.m_scrolledWindow2, 1, wx.EXPAND |wx.ALL, 5 )


		self.m_panel2.SetSizer( bSizer5 )
		self.m_panel2.Layout()
		bSizer5.Fit( self.m_panel2 )
		self.m_notebook1.AddPage( self.m_panel2, u"General", False )

		bSizer4.Add( self.m_notebook1, 1, wx.EXPAND |wx.ALL, 5 )

		m_sdbSizer1 = wx.StdDialogButtonSizer()
		self.m_sdbSizer1OK = wx.Button( self, wx.ID_OK )
		m_sdbSizer1.AddButton( self.m_sdbSizer1OK )
		self.m_sdbSizer1Apply = wx.Button( self, wx.ID_APPLY )
		m_sdbSizer1.AddButton( self.m_sdbSizer1Apply )
		self.m_sdbSizer1Cancel = wx.Button( self, wx.ID_CANCEL )
		m_sdbSizer1.AddButton( self.m_sdbSizer1Cancel )
		m_sdbSizer1.Realize();

		bSizer4.Add( m_sdbSizer1, 0, wx.ALL|wx.EXPAND, 5 )


		self.SetSizer( bSizer4 )
		self.Layout()

		self.Centre( wx.BOTH )

	def __del__( self ):
		pass


