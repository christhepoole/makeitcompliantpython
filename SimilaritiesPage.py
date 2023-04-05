import wx
import os
import re
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity

class MyFrame(wx.Frame):
    def __init__(self):
        wx.Frame.__init__(self, None, wx.ID_ANY, "File Similarity Checker", size=(500, 300))
        panel = wx.Panel(self, wx.ID_ANY)

        # Create the text boxes for the file paths
        file1_label = wx.StaticText(panel, wx.ID_ANY, "File 1:")
        self.file1_text = wx.TextCtrl(panel, wx.ID_ANY, "")
        file1_button = wx.Button(panel, wx.ID_ANY, "Choose...")
        self.Bind(wx.EVT_BUTTON, self.on_file1_button, file1_button)

        file2_label = wx.StaticText(panel, wx.ID_ANY, "File 2:")
        self.file2_text = wx.TextCtrl(panel, wx.ID_ANY, "")
        file2_button = wx.Button(panel, wx.ID_ANY, "Choose...")
        self.Bind(wx.EVT_BUTTON, self.on_file2_button, file2_button)

        # Create the buttons to run the similarity checks
        cosine_button = wx.Button(panel, wx.ID_ANY, "Cosine Similarity")
        self.Bind(wx.EVT_BUTTON, self.on_cosine_button, cosine_button)

        jaccard_button = wx.Button(panel, wx.ID_ANY, "Jaccard Similarity")
        self.Bind(wx.EVT_BUTTON, self.on_jaccard_button, jaccard_button)

        # Create the output text boxes
        self.cosine_output = wx.TextCtrl(panel, wx.ID_ANY, "", style=wx.TE_MULTILINE | wx.TE_READONLY)
        self.jaccard_output = wx.TextCtrl(panel, wx.ID_ANY, "", style=wx.TE_MULTILINE | wx.TE_READONLY)

        # Create the layout of the GUI
        file1_sizer = wx.BoxSizer(wx.HORIZONTAL)
        file1_sizer.Add(file1_label, 0, wx.ALL | wx.CENTER, 5)
        file1_sizer.Add(self.file1_text, 1, wx.EXPAND | wx.ALL, 5)
        file1_sizer.Add(file1_button, 0, wx.ALL | wx.CENTER, 5)

        file2_sizer = wx.BoxSizer(wx.HORIZONTAL)
        file2_sizer.Add(file2_label, 0, wx.ALL | wx.CENTER, 5)
        file2_sizer.Add(self.file2_text, 1, wx.EXPAND | wx.ALL, 5)
        file2_sizer.Add(file2_button, 0, wx.ALL | wx.CENTER, 5)

        button_sizer = wx.BoxSizer(wx.HORIZONTAL)
        button_sizer.Add(cosine_button, 0, wx.ALL | wx.CENTER, 5)
        button_sizer.Add(jaccard_button, 0, wx.ALL | wx.CENTER, 5)

        output_sizer = wx.BoxSizer(wx.VERTICAL)
        output_sizer.Add(wx.StaticText(panel, wx.ID_ANY, "Cosine Similarity:"), 0, wx.EXPAND | wx.ALL, 5)
        output_sizer.Add(self.cosine_output, 1, wx.EXPAND | wx.ALL, 5)
        output_sizer.Add(wx.StaticText(panel, wx.ID_ANY, "Jaccard Similarity:"), 0, wx.EXPAND | wx.ALL, 5)
        output_sizer.Add(self.jaccard_output, 1, wx.EXPAND | wx
