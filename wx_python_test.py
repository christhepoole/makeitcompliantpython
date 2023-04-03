import wx


class StandaloneApp(wx.Frame):
    def __init__(self, parent):
        wx.Frame.__init__(self, parent, title="Compliance System for Software Licenses", size=(550, 600))

        self.Show(True)


app = wx.App(False)
frame = StandaloneApp(None)
app.MainLoop()
