import wx

import FileComparison


class UploadPanel(wx.Panel):
    def __init__(self, parent):
        wx.Panel.__init__(self, parent=parent)
        self.file_path_text_ctrl = wx.TextCtrl(self, style=wx.TE_READONLY, size=(400, -1))
        self.result_text_ctrl = wx.TextCtrl(self, -1, "", style=wx.TE_MULTILINE | wx.TE_READONLY, size=(-1, 150))
        browse_button = wx.Button(self, -1, "Browse...", size=(80, -1))
        import_button = wx.Button(self, -1, "Import", size=(80, -1))

        font = wx.Font(10, wx.DEFAULT, wx.NORMAL, wx.BOLD)
        file_sizer = wx.BoxSizer(wx.HORIZONTAL)
        file_sizer.Add(wx.StaticText(self, -1, "File path:", size=(100, -1)).SetFont(font), 0,
                       wx.ALIGN_CENTER_VERTICAL | wx.LEFT, 5)
        file_sizer.Add(self.file_path_text_ctrl, 1, wx.EXPAND)
        file_sizer.Add(browse_button, 0, wx.RIGHT, 5)

        result_sizer = wx.BoxSizer(wx.VERTICAL)
        result_sizer.Add(wx.StaticText(self, -1, "Results:", size=(-1, -1)).SetFont(font), 0,
                         wx.LEFT | wx.TOP | wx.RIGHT, 5)
        result_sizer.Add(self.result_text_ctrl, 1, wx.EXPAND | wx.LEFT | wx.RIGHT | wx.BOTTOM, 5)

        button_sizer = wx.BoxSizer(wx.HORIZONTAL)
        button_sizer.Add(import_button, 0, wx.RIGHT | wx.BOTTOM, 5)

        sizer = wx.BoxSizer(wx.VERTICAL)
        sizer.Add(file_sizer, 0, wx.EXPAND | wx.ALL, 5)
        sizer.Add(wx.StaticLine(self), 0, wx.EXPAND | wx.TOP | wx.BOTTOM, 5)
        sizer.Add(result_sizer, 0, wx.EXPAND | wx.LEFT | wx.RIGHT, 5)
        sizer.Add(button_sizer, 0, wx.ALIGN_RIGHT | wx.ALL, 5)
        self.SetSizer(sizer)

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


class SimilarityPanel(wx.Panel):
    def __init__(self, parent):
        wx.Panel.__init__(self, parent=parent)


class ConditionsPanel(wx.Panel):
    def __init__(self, parent):
        wx.Panel.__init__(self, parent=parent)
        headerFont = wx.Font(wx.FontInfo(15).Bold().Underlined())
        files = self.GetParent().getClassifiedFiles()

        file_a_box = wx.BoxSizer(wx.VERTICAL)

        # File A Permission Header
        file_a_permissions_header = wx.StaticText(self, -1, "With The " + files[0] + " You Can", style=wx.ALIGN_CENTER)
        file_a_permissions_header.SetFont(headerFont)
        file_a_permissions_header.Wrap(280)
        file_a_box.Add(file_a_permissions_header, 0)

        # File A Permission Header Line (Doesn't really work)
        #file_a_box.Add(wx.StaticLine(self), 0)

        file_b_box = wx.BoxSizer(wx.VERTICAL)

        # File B Permission Header
        file_b_permissions_header = wx.StaticText(self, -1, "With The " + files[1] + " You Can", style=wx.ALIGN_CENTER)
        file_b_permissions_header.SetFont(headerFont)
        file_b_permissions_header.Wrap(260)
        file_b_box.Add(file_b_permissions_header, 0)

        # File B Permission Header Line (Doesn't really work)
        #file_b_box.Add(wx.StaticLine(self), 0)

        file_box = wx.BoxSizer(wx.HORIZONTAL)
        file_box.Add(file_a_box, 0, flag=wx.LEFT | wx.RIGHT, border=20)
        file_box.Add(file_b_box, 0, flag=wx.LEFT | wx.RIGHT, border=20)
        self.SetSizer(file_box)
        self.Layout()


class MyFrame(wx.Frame):
    def __init__(self):
        wx.Frame.__init__(self, None, -1, 'File Import and Output', size=(600, 550))

        # Tempory way to deal with files
        self.fileA = FileComparison.file_to_string("license_templates/Apache License 2.0.txt")
        self.fileB = FileComparison.file_to_string("license_templates/MIT License.txt")

        self.panel = UploadPanel(self)
        self.similarity_panel = SimilarityPanel(self)
        self.conditions_panel = ConditionsPanel(self)
        self.similarity_panel.Hide()
        self.conditions_panel.Hide()
        self.panelSizer = wx.BoxSizer(wx.VERTICAL)
        self.panelSizer.Add(self.panel, 1, wx.EXPAND)
        self.panelSizer.Add(self.similarity_panel, 1, wx.EXPAND)
        self.panelSizer.Add(self.conditions_panel, 1, wx.EXPAND)
        self.SetSizer(self.panelSizer)


        # TODO Come up with a better way of doing switching panels. Maybe via a button instead of a menu
        menuBar = wx.MenuBar()
        view = wx.Menu()
        uploadPageMenuItem = view.Append(wx.ID_ANY, "View Upload Page", "View the Upload Page")
        similarityPageMenuItem = view.Append(wx.ID_ANY, "View Similarity Page",
                                             "View the similarity between the uploaded files")
        conditionsPageMenuItem = view.Append(wx.ID_ANY, "View Conditions Page", "View the conditions of each license")
        menuBar.Append(view, "&View")
        self.SetMenuBar(menuBar)
        self.Bind(wx.EVT_MENU, self.viewUploadPanel, uploadPageMenuItem)
        self.Bind(wx.EVT_MENU, self.viewSimilarityPanel, similarityPageMenuItem)
        self.Bind(wx.EVT_MENU, self.viewConditionsPanel, conditionsPageMenuItem)

    def viewSimilarityPanel(self, event):
        if self.panel.IsShown():
            self.panel.Hide()
        elif self.conditions_panel.IsShown():
            self.conditions_panel.Hide()
        self.similarity_panel.Show(True)
        self.Layout()

    def viewConditionsPanel(self, event):
        if self.panel.IsShown():
            self.panel.Hide()
        elif self.similarity_panel.IsShown():
            self.similarity_panel.Hide()
        self.conditions_panel.Show(True)
        self.Layout()

    def viewUploadPanel(self, event):
        if self.similarity_panel.IsShown():
            self.similarity_panel.Hide()
        elif self.conditions_panel.IsShown():
            self.conditions_panel.Hide()
        self.panel.Show(True)
        self.Layout()

    def getClassifiedFiles(self):
        classifiedFileA = FileComparison.classify(self.fileA)
        classifiedFileB = FileComparison.classify(self.fileB)
        return [classifiedFileA, classifiedFileB]


if __name__ == '__main__':
    app = wx.App()
    frame = MyFrame()
    frame.Show(True)
    app.MainLoop()
