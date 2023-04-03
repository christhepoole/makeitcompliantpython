import wx

class MyFrame(wx.Frame):
    def __init__(self):
        wx.Frame.__init__(self, None, -1, 'File Import and Output', size=(500, 300))
        panel = wx.Panel(self, -1)
        self.file_path_text_ctrl = wx.TextCtrl(panel, -1, "", style=wx.TE_READONLY, size=(400, -1))
        self.result_text_ctrl = wx.TextCtrl(panel, -1, "", style=wx.TE_MULTILINE|wx.TE_READONLY, size=(-1, 150))
        browse_button = wx.Button(panel, -1, "Browse...", size=(80, -1))
        import_button = wx.Button(panel, -1, "Import", size=(80, -1))
        
        font = wx.Font(10, wx.DEFAULT, wx.NORMAL, wx.BOLD)
        file_sizer = wx.BoxSizer(wx.HORIZONTAL)
        file_sizer.Add(wx.StaticText(panel, -1, "File path:", size=(100, -1)).SetFont(font), 0, wx.ALIGN_CENTER_VERTICAL|wx.LEFT, 5)
        file_sizer.Add(self.file_path_text_ctrl, 1, wx.EXPAND)
        file_sizer.Add(browse_button, 0, wx.ALIGN_RIGHT|wx.RIGHT, 5)
        
        result_sizer = wx.BoxSizer(wx.VERTICAL)
        result_sizer.Add(wx.StaticText(panel, -1, "Results:", size=(-1, -1)).SetFont(font), 0, wx.LEFT|wx.TOP|wx.RIGHT, 5)
        result_sizer.Add(self.result_text_ctrl, 1, wx.EXPAND|wx.LEFT|wx.RIGHT|wx.BOTTOM, 5)
        
        button_sizer = wx.BoxSizer(wx.HORIZONTAL)
        button_sizer.Add(import_button, 0, wx.ALIGN_RIGHT|wx.RIGHT|wx.BOTTOM, 5)

        sizer = wx.BoxSizer(wx.VERTICAL)
        sizer.Add(file_sizer, 0, wx.EXPAND|wx.ALL, 5)
        sizer.Add(wx.StaticLine(panel), 0, wx.EXPAND|wx.TOP|wx.BOTTOM, 5)
        sizer.Add(result_sizer, 0, wx.EXPAND|wx.LEFT|wx.RIGHT, 5)
        sizer.Add(button_sizer, 0, wx.ALIGN_RIGHT|wx.ALL, 5)
        panel.SetSizer(sizer)

        self.Bind(wx.EVT_BUTTON, self.on_browse, browse_button)
        self.Bind(wx.EVT_BUTTON, self.on_import, import_button)
        
    def on_browse(self, event):
        dlg = wx.FileDialog(self, "Choose a file", style=wx.FD_OPEN)
        if dlg.ShowModal() == wx.ID_OK:
            path = dlg.GetPath()
            self.file_path_text_ctrl.SetValue(path)
        dlg.Destroy()

    def on_import(self, event):
        path = self.file_path_text_ctrl.GetValue()
        with open(path, 'r') as file:
            # Do some processing on the file
            result = file.read()
        self.result_text_ctrl.SetValue(result)

if __name__ == '__main__':
    app = wx.App()
    frame = MyFrame()
    frame.Show(True)
    app.MainLoop()
