import wx
from TheDictionaryDictionary import TheDictionaryDictionary

app = wx.App()
wx.InitAllImageHandlers()

frame = TheDictionaryDictionary(None)
frame.Show()
app.MainLoop()