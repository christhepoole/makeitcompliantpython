import os, wx
import FileComparison   

file_list = []

class Text_File:
    def __init__(self, name, value):
        self.name = name
        self.value = value

class UploadPanel(wx.Panel):
    def __init__(self, parent):
        wx.Panel.__init__(self, parent=parent)
        self.file_path = wx.TextCtrl(self, size=(400, -1), style=wx.TE_READONLY)
        self.uploaded_files = wx.TextCtrl(self, style=wx.TE_READONLY)
        browse_button = wx.Button(self, -1, "Browse...")
        import_button = wx.Button(self, -1, "Import")

        browse_button.Bind(wx.EVT_BUTTON, self.on_browse)
        import_button.Bind(wx.EVT_BUTTON, self.on_import)

        sizer = wx.BoxSizer(wx.VERTICAL)
        sizer.Add(self.file_path, 0, 0, 0)
        sizer.Add(browse_button, 0, 0, 0)
        sizer.Add(import_button, 0, 0, 0)
        sizer.Add(self.uploaded_files, 0, wx.EXPAND, 0)

        self.SetSizer(sizer)        

    def on_browse(self, event):
        dlg = wx.FileDialog(self, "Choose a file", style=wx.FD_OPEN)
        if dlg.ShowModal() == wx.ID_OK:
            path = dlg.GetPath()
            self.file_path.SetValue(path)
        dlg.Destroy()

    def on_import(self, event):
        path = self.file_path.GetValue()
        with open(path) as file:
            text_file = Text_File(os.path.splitext(os.path.basename(path))[0], file.readlines())
            file_list.append(text_file)
        file_list_names = ""
        for file in file_list:
            file_list_names += file.name + " "
        self.uploaded_files.SetValue(file_list_names)


class SimilarityPanel(wx.Panel):
    def __init__(self, parent):
        wx.Panel.__init__(self, parent=parent)
        self.files_to_compare = wx.TextCtrl(self, style=wx.TE_READONLY)
        self.comparison_results = wx.TextCtrl(self, style=wx.TE_READONLY)

        self.files_to_compare.SetValue("Uploaded files: ")
        for file in file_list:
            self.files_to_compare.AppendText(file.name + " ")

        sizer = wx.BoxSizer(wx.VERTICAL)
        sizer.Add(self.files_to_compare, 0, 0, 0)
        self.SetSizer(sizer)
    
    def cosine_similarity():
        compare_value = str(100*(FileComparison.cosine_similarity(file_list[0]['value'], file_list[1]['value'])))
        return compare_value



class ConditionsPanel(wx.Panel):
    def __init__(self, parent):
        wx.Panel.__init__(self, parent=parent)


class MyFrame(wx.Frame):
    def __init__(self):
        wx.Frame.__init__(self, None, -1, 'File Import and Output', size=(500, 300))
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

        #TODO Come up with a better way of doing switching panels. Maybe via a button instead of a menu
        menuBar = wx.MenuBar()
        view = wx.Menu()
        uploadPageMenuItem = view.Append(wx.ID_ANY, "View Upload Page", "View the Upload Page")
        similarityPageMenuItem = view.Append(wx.ID_ANY, "View Similarity Page", "View the similarity between the uploaded files")
        conditionsPageMenuItem = view.Append(wx.ID_ANY, "View Conditions Page", "View the conditions of each license")
        menuBar.Append(view, "&View")
        self.SetMenuBar(menuBar)
        self.Bind(wx.EVT_MENU, self.viewUploadPanel, uploadPageMenuItem)
        self.Bind(wx.EVT_MENU, self.viewSimilarityPanel, similarityPageMenuItem)
        self.Bind(wx.EVT_MENU, self.viewConditionsPanel, conditionsPageMenuItem)


    def viewSimilarityPanel(self, event):
        self.similarity_panel = SimilarityPanel(self)
        self.panelSizer.Add(self.similarity_panel, 1, wx.EXPAND)
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


if __name__ == '__main__':
    app = wx.App()
    frame = MyFrame()
    frame.Show(True)
    app.MainLoop()
