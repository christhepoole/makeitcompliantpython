import os, wx
import FileComparison   

file_list = []

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
            text_file = {"name": os.path.splitext(os.path.basename(path))[0], "value": file.read()}
            file_list.append(text_file)
        file_list_names = ""
        for file in file_list:
            file_list_names += file["name"] + " "
        self.uploaded_files.SetValue(file_list_names)


class SimilarityPanel(wx.Panel):
    def __init__(self, parent):
        wx.Panel.__init__(self, parent=parent)
        self.files_to_compare = wx.TextCtrl(self, size=(400, -1), style=wx.TE_READONLY)
        self.comparison_results = wx.TextCtrl(self, size=(400, -1), style=wx.TE_READONLY)

        self.files_to_compare.SetValue("Uploaded files: ")
        for file in file_list:
            self.files_to_compare.AppendText(file["name"] + " ")

        cosine_sim_btn = wx.Button(self, -1, "Cosine Sim")
        jaccard_sim_btn = wx.Button(self, -1, "Jaccard Sim")
        cosine_sim_btn.Bind(wx.EVT_BUTTON, self.cosine_similarity)
        jaccard_sim_btn.Bind(wx.EVT_BUTTON, self.jaccard_similarity)

        btn_sizer = wx.BoxSizer(wx.HORIZONTAL)
        btn_sizer.Add(cosine_sim_btn, 0, 0, 0)
        btn_sizer.Add(jaccard_sim_btn, 0, 0, 0)

        sizer = wx.BoxSizer(wx.VERTICAL)
        sizer.Add(self.files_to_compare, 0, 0, 0)
        sizer.Add(btn_sizer, 0, 0, 0)
        sizer.Add(self.comparison_results, 0, 0, 0)
        self.SetSizer(sizer)
    
    def cosine_similarity(self, event):
        compare_value = str(100*(FileComparison.cosine_similarity(file_list[0]['value'], file_list[1]['value'])))
        self.comparison_results.SetValue("Cosine Similarity: " + compare_value + " %")
    
    def jaccard_similarity(self, event):
        compare_value = str(100*(FileComparison.jaccard_similarity(file_list[0]['value'], file_list[1]['value'])))
        self.comparison_results.SetValue("Jaccard Similarity: " + compare_value + " %")



class ConditionsPanel(wx.Panel):
    def __init__(self, parent):
        wx.Panel.__init__(self, parent=parent)
        headerFont = wx.Font(wx.FontInfo(15).Bold().Underlined())
        font = wx.Font(wx.FontInfo(10))
        files = self.GetParent().getClassifiedFiles()
        permissions = FileComparison.get_permissions()
        d_conditions = FileComparison.get_conditions_for_distribution()
        m_conditions = FileComparison.get_conditions_for_modification()
        limitations = FileComparison.get_limitations()
        if files is not False:
            file_a_box = wx.BoxSizer(wx.VERTICAL)

            # File A Permission Header
            file_a_permissions_header = wx.StaticText(self, -1, "With The " + files[0] + " You Can", style=wx.ALIGN_CENTER)
            file_a_permissions_header.SetFont(headerFont)
            file_a_permissions_header.Wrap(260)
            file_a_box.Add(file_a_permissions_header, 0)

            # File A Permission Header Line (Doesn't really work)
            #file_a_box.Add(wx.StaticLine(self), 0)

            file_a_permissions_box = wx.BoxSizer(wx.VERTICAL)
            for permission in permissions[0]:
                file_a_permission = wx.StaticText(self, -1, "-" + FileComparison.define(permission))
                file_a_permission.SetFont(font)
                file_a_permission.Wrap(260)
                file_a_permissions_box.Add(file_a_permission)

            file_a_box.Add(file_a_permissions_box, 0, flag=wx.TOP | wx.BOTTOM, border=20)

            file_a_d_conditions_box = wx.BoxSizer(wx.VERTICAL)
            if d_conditions[0] is not False:
                file_a_d_conditions_header = wx.StaticText(self, -1, "Conditions For Distribution", style=wx.ALIGN_CENTER)
                file_a_d_conditions_header.SetFont(headerFont)
                file_a_d_conditions_header.Wrap(260)
                file_a_box.Add(file_a_d_conditions_header)
                for condition in d_conditions[0]:
                    file_a_condition = wx.StaticText(self, -1, "-" + FileComparison.define(condition))
                    file_a_condition.SetFont(font)
                    file_a_condition.Wrap(260)
                    file_a_d_conditions_box.Add(file_a_condition)
            file_a_box.Add(file_a_d_conditions_box, 0, flag=wx.TOP | wx.BOTTOM, border=20)

            file_a_m_conditions_box = wx.BoxSizer(wx.VERTICAL)
            if m_conditions[0] is not False:
                file_a_m_conditions_header = wx.StaticText(self, -1, "Conditions For Modification", style=wx.ALIGN_CENTER)
                file_a_m_conditions_header.SetFont(headerFont)
                file_a_m_conditions_header.Wrap(260)
                file_a_box.Add(file_a_m_conditions_header)
                for condition in m_conditions[0]:
                    file_a_condition = wx.StaticText(self, -1, "-" + FileComparison.define(condition))
                    file_a_condition.SetFont(font)
                    file_a_condition.Wrap(260)
                    file_a_m_conditions_box.Add(file_a_condition)
            file_a_box.Add(file_a_m_conditions_box, 0, flag=wx.TOP | wx.BOTTOM, border=20)

            file_a_limitations_box = wx.BoxSizer(wx.VERTICAL)
            if limitations[0] is not False:
                file_a_limitations_header = wx.StaticText(self, -1, "Limitations", style=wx.ALIGN_CENTER)
                file_a_limitations_header.SetFont(headerFont)
                file_a_limitations_header.Wrap(260)
                file_a_box.Add(file_a_limitations_header)
                for limitation in limitations[0]:
                    file_a_limitation = wx.StaticText(self, -1, "-" + FileComparison.define(limitation))
                    file_a_limitation.SetFont(font)
                    file_a_limitation.Wrap(260)
                    file_a_limitations_box.Add(file_a_limitation)
            file_a_box.Add(file_a_limitations_box, 0, flag=wx.TOP | wx.BOTTOM, border=20)

            file_b_box = wx.BoxSizer(wx.VERTICAL)

            # File B Permission Header
            file_b_permissions_header = wx.StaticText(self, -1, "With The " + files[1] + " You Can", style=wx.ALIGN_CENTER)
            file_b_permissions_header.SetFont(headerFont)
            file_b_permissions_header.Wrap(260)
            file_b_box.Add(file_b_permissions_header, 0)

            # File B Permission Header Line (Doesn't really work)
            #file_b_box.Add(wx.StaticLine(self), 0)

            file_b_permissions_box = wx.BoxSizer(wx.VERTICAL)
            for permission in permissions[1]:
                file_b_permission = wx.StaticText(self, -1, "-" + FileComparison.define(permission))
                file_b_permission.SetFont(font)
                file_b_permission.Wrap(260)
                file_b_permissions_box.Add(file_b_permission)

            file_b_box.Add(file_b_permissions_box, 0, flag=wx.TOP | wx.BOTTOM, border=20)

            file_b_d_conditions_box = wx.BoxSizer(wx.VERTICAL)
            if d_conditions[1] is not False:
                file_b_d_conditions_header = wx.StaticText(self, -1, "Conditions For Distribution", style=wx.ALIGN_CENTER)
                file_b_d_conditions_header.SetFont(headerFont)
                file_b_d_conditions_header.Wrap(260)
                file_b_box.Add(file_b_d_conditions_header)
                for condition in d_conditions[1]:
                    file_b_condition = wx.StaticText(self, -1, "-" + FileComparison.define(condition))
                    file_b_condition.SetFont(font)
                    file_b_condition.Wrap(260)
                    file_b_d_conditions_box.Add(file_b_condition)
            file_b_box.Add(file_b_d_conditions_box, 0, flag=wx.TOP | wx.BOTTOM, border=20)

            file_b_m_conditions_box = wx.BoxSizer(wx.VERTICAL)
            if m_conditions[1] is not False:
                file_b_m_conditions_header = wx.StaticText(self, -1, "Conditions For Modification", style=wx.ALIGN_CENTER)
                file_b_m_conditions_header.SetFont(headerFont)
                file_b_m_conditions_header.Wrap(260)
                file_b_box.Add(file_b_m_conditions_header)
                for condition in m_conditions[1]:
                    file_b_condition = wx.StaticText(self, -1, "-" + FileComparison.define(condition))
                    file_b_condition.SetFont(font)
                    file_b_condition.Wrap(260)
                    file_b_m_conditions_box.Add(file_b_condition)
            file_b_box.Add(file_b_m_conditions_box, 0, flag=wx.TOP | wx.BOTTOM, border=20)

            file_b_limitations_box = wx.BoxSizer(wx.VERTICAL)
            if limitations[1] is not False:
                file_b_limitations_header = wx.StaticText(self, -1, "Limitations", style=wx.ALIGN_CENTER)
                file_b_limitations_header.SetFont(headerFont)
                file_b_limitations_header.Wrap(260)
                file_b_box.Add(file_b_limitations_header)
                for limitation in limitations[1]:
                    file_b_limitation = wx.StaticText(self, -1, "-" + FileComparison.define(limitation))
                    file_b_limitation.SetFont(font)
                    file_b_limitation.Wrap(260)
                    file_b_limitations_box.Add(file_b_limitation)
            file_b_box.Add(file_b_limitations_box, 0, flag=wx.TOP | wx.BOTTOM, border=20)

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
        self.conditions_panel = None
        self.similarity_panel.Hide()
        self.panelSizer = wx.BoxSizer(wx.VERTICAL)
        self.panelSizer.Add(self.panel, 1, wx.EXPAND)
        self.panelSizer.Add(self.similarity_panel, 1, wx.EXPAND)
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
        self.similarity_panel = SimilarityPanel(self)
        self.panelSizer.Add(self.similarity_panel, 1, wx.EXPAND)
        if self.panel.IsShown():
            self.panel.Hide()
        elif self.conditions_panel.IsShown():
            self.conditions_panel.Hide()
        self.similarity_panel.Show(True)
        self.Layout()

    def viewConditionsPanel(self, event):
        self.conditions_panel = ConditionsPanel(self)
        self.panelSizer.Add(self.conditions_panel, 1, wx.EXPAND)
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
        if len(file_list) == 0:
            return False
        return FileComparison.classify_two_files(file_list[0]["value"], file_list[1]["value"])


if __name__ == '__main__':
    app = wx.App()
    frame = MyFrame()
    frame.Show(True)
    app.MainLoop()
