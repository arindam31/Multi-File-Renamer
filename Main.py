#Rename files, suffix , prefix or extension

import wx
import os.path
import os
from Rename import Renamer


def GetTheFiles(path):
    ff = [f for f in os.listdir(path)
            if os.path.isfile(os.path.join(path, f))]
    #ff = os.listdir(f)
    return ff


def rename_preview(org_list, mod_text, prefix, suffix, f_ext):
    mod_list = []
    if org_list:
        for i in org_list:
            t = os.path.splitext(i)
            if prefix and suffix:
                new_name = mod_text + t[0] + mod_text + t[-1]
            elif prefix:
                new_name = mod_text + t[0] + t[-1]
            elif suffix:
                new_name = t[0] + mod_text + t[-1]
            elif f_ext:
                new_name = t[0] + "." + mod_text
            mod_list.append(new_name)
    return mod_list


class TheRenamer(wx.Frame):
    def __init__(self, parent, title):
        super(TheRenamer, self).__init__(parent, title=title,
            size=(650, 650))
        self.InitUI()
        self.Centre()
#*.*.*.*.*.*.*.*.*.*.*.*.*.*.*.*.*.*.*.*.*.*.*.*.*.*.*.*.*.*.*.*.*.*.*.*.*.*.*
#----------------------------------------------------------------------------
        favicon = wx.Icon('desktop.ico', wx.BITMAP_TYPE_ICO)
        wx.Frame.SetIcon(self, favicon)
        self.Show()

    def InitUI(self):
        panel = wx.Panel(self)

        font = wx.SystemSettings_GetFont(wx.SYS_SYSTEM_FONT)
        font.SetPointSize(9)

        font1 = wx.SystemSettings_GetFont(wx.SYS_SYSTEM_FONT)
        font1.SetPointSize(10)

        vbox = wx.BoxSizer(wx.VERTICAL)

#*.*.*.*.*.*.*.*.*.*.*.*.*.*.*.*.*.*.*.*.*.*.*.*.*.*.*.*.*.*.*.*.*.*.*.*.*.*.*.
#-----------------------------------------------------------------------------
#Second Horizontal Box First Box
        
        hbox21 = wx.BoxSizer(wx.HORIZONTAL)
        st21 = wx.StaticText(panel, label='Original')
        st21.SetFont(font)
        hbox21.Add(st21)
        vbox.Add(hbox21, flag=wx.LEFT | wx.TOP, border=10)

        vbox.Add((-1, 10))

        
 #File Repository1
        
        self.Files_List1 = wx.ListCtrl(panel, -1, style=wx.LC_REPORT|wx.BORDER_SUNKEN|wx.LC_SINGLE_SEL)
        self.Files_List1.InsertColumn(0, 'File Name')
        self.Files_List1.SetColumnWidth(0, 500)
        
        bt_choose_dir = wx.Button(panel, -1, label='Choose Folder')
        self.bt_Clear = wx.Button(panel, -1, label='Clear')
        
        hbox31 = wx.BoxSizer(wx.HORIZONTAL)
        vbox11 = wx.BoxSizer(wx.VERTICAL)
        
        vbox11.Add(bt_choose_dir, flag=wx.RIGHT | wx.LEFT, border=5)
        vbox11.Add(self.bt_Clear, flag=wx.RIGHT | wx.LEFT | wx.TOP, border=5)
        
        hbox31.Add(self.Files_List1, proportion=1, flag=wx.EXPAND)
        hbox31.Add(vbox11, flag=wx.RIGHT | wx.LEFT, border=10)
        
        vbox.Add(hbox31, proportion=1, flag=wx.LEFT | wx.RIGHT | wx.EXPAND,
            border=10)
        self.Files_List1.SetFont(font)
        vbox.Add((-1, 25))

#*.*.*.*.*.*.*.*.*.*.*.*.*.*.*.*.*.*.*.*.*.*.*.*.*.*.*.*.*.*.*.*.*.*.*.*.*.*.*.
#-----------------------------------------------------------------------------

#First Horizontal Box
       
        hbox1 = wx.BoxSizer(wx.HORIZONTAL)

  #Static Text for 'Term'
        st1 = wx.StaticText(panel, label='Text')
        st1.SetFont(font)
        hbox1.Add(st1, flag=wx.RIGHT|wx.TOP, border=8)

  #Replacement text Box
        
        self.Replacement_Text = wx.TextCtrl(panel,-1,"Enter string to be added",size=wx.Size(-1,30))
        hbox1.Add(self.Replacement_Text, proportion=1)        
        self.Replacement_Text.SetFont(font1)

  #Show mod results Button
        
        btn_Mod_Results = wx.Button(panel,-1,label='PREVIEW')
        self.Bind(wx.EVT_BUTTON, self.loadResult_Modified, btn_Mod_Results)
        hbox1.Add(btn_Mod_Results, flag=wx.RIGHT|wx.LEFT|wx.TOP, border=5)
        vbox.Add(hbox1, flag=wx.EXPAND|wx.LEFT|wx.RIGHT|wx.TOP, border=10)
        vbox.Add((-1, 10))

#*.*.*.*.*.*.*.*.*.*.*.*.*.*.*.*.*.*.*.*.*.*.*.*.*.*.*.*.*.*.*.*.*.*.*.*.*.*.*.*.
#--------------------------------------------------------------------------------
        
#*.*.*.*.*.*.*.*.*.*.*.*.*.*.*.*.*.*.*.*.*.*.*.*.*.*.*.*.*.*.*.*.*.*.*.*.*.*.*.*.
#--------------------------------------------------------------------------------
        

#*.*.*.*.*.*.*.*.*.*.*.*.*.*.*.*.*.*.*.*.*.*.*.*.*.*.*.*.*.*.*.*.*.*.*.*.*.*.*
#----------------------------------------------------------------------------
#Second Horizontal Box Second Box
        hbox22 = wx.BoxSizer(wx.HORIZONTAL)
        st22 = wx.StaticText(panel, label='Preview')
        st22.SetFont(font)
        hbox22.Add(st22)
        vbox.Add(hbox22, flag=wx.LEFT | wx.TOP, border=10)

        vbox.Add((-1, 10))

#Third Horizontal Box
        
 #File Repository2
        self.Files_List2 = wx.ListCtrl(
                panel,
                -1,
                style=wx.LC_REPORT | wx.BORDER_SUNKEN | wx.LC_SINGLE_SEL
                )
        self.Files_List2.InsertColumn(0, 'File Name')
        self.Files_List2.SetColumnWidth(0, 500)
         
        hbox32 = wx.BoxSizer(wx.HORIZONTAL)
        vbox12 = wx.BoxSizer(wx.VERTICAL)
        
        hbox32.Add(self.Files_List2, proportion=1, flag=wx.EXPAND)
        hbox32.Add(vbox12, flag=wx.RIGHT | wx.LEFT, border=10)
        
        vbox.Add(hbox32, proportion=1, flag=wx.LEFT | wx.RIGHT | wx.EXPAND,
            border=10)
        self.Files_List2.SetFont(font)
        vbox.Add((-1, 25))

#*.*.*.*.*.*.*.*.*.*.*.*.*.*.*.*.*.*.*.*.*.*.*.*.*.*.*.*.*.*.*.*.*.*.*.*.*.*.*.
#----------------------------------------------------------------------------
#Fourth Horizontal Box

        hbox4 = wx.BoxSizer(wx.HORIZONTAL)
        self.cb1 = wx.CheckBox(panel, label='Prefix')
        self.cb2 = wx.CheckBox(panel, label='Suffix')
        self.cb3 = wx.CheckBox(panel, label='File extension')
        self.cb1.SetFont(font)
        self.cb2.SetFont(font)
        self.cb3.SetFont(font)
        hbox4.Add(self.cb1)
        hbox4.Add(self.cb2)
        hbox4.Add(self.cb3)
        vbox.Add(hbox4, flag=wx.LEFT, border=10)

        vbox.Add((-1, 25))

#*.*.*.*.*.*.*.*.*.*.*.*.*.*.*.*.*.*.*.*.*.*.*.*.*.*.*.*.*.*.*.*.*.*.*.*.*.*.*.
#-----------------------------------------------------------------------------
#Fifth Horizontal Box
        hbox5 = wx.BoxSizer(wx.HORIZONTAL)
        self.bt_Final = wx.Button(panel, label='SUBMIT', size=(100, 30))
        self.bt_Reset = wx.Button(panel, label='RESET', size=(70, 30))
        self.bt_Result = wx.Button(panel, label='OPEN RESULT FOLDER', size=(160, 30))
        hbox5.Add(self.bt_Final, flag=wx.LEFT, border=5)
        hbox5.Add(self.bt_Reset, flag=wx.LEFT, border=5)
        hbox5.Add(self.bt_Result, flag=wx.LEFT, border=5)
        vbox.Add(hbox5, flag=wx.ALIGN_RIGHT | wx.RIGHT, border=10)

        vbox.Add((-1, 25))

        #Seventh Horizontal Box

        hbox7 = wx.BoxSizer(wx.HORIZONTAL)
        self.statusbar = self.CreateStatusBar()
        self.statusbar.SetStatusText('Ready')
        hbox7.Add(self.statusbar, proportion=1, flag=wx.EXPAND)
        vbox.Add(hbox7, flag=wx.TOP | wx.EXPAND, border=5)

        panel.SetSizer(vbox)

#Menu section
        menubar = wx.MenuBar()
        pehla = wx.Menu()
        doosra = wx.Menu()
        teesra = wx.Menu()
        info = wx.Menu()

#Menu Items
        
        item1_1 = pehla.Append(wx.ID_OPEN,
                "&Open\tAlt-A",
                "This is to choose folder"
                )  #Sub-Items of First menu pull down list

        item1_2 = pehla.Append(wx.ID_EXIT,
                "&Exit\tAlt-E",
                "This will exit app"
                )
        
        item3_2 = teesra.Append(wx.ID_ABOUT, "A&bout\tAlt-B", "About Section")

        
        menu_1 = menubar.Append(pehla, '&File')#Naming of Menu items
        menu_3 = menubar.Append(teesra, '&Info')
        self.SetMenuBar(menubar)

#Events
        self.Bind(wx.EVT_MENU, self.OnFileExit, item1_2)
        self.Bind(wx.EVT_MENU, self.OnFileOpen, item1_1)
        self.Bind(wx.EVT_BUTTON, self.OnReset, self.bt_Reset)
        self.Bind(wx.EVT_BUTTON, self.Process, self.bt_Final)
        self.Bind(wx.EVT_BUTTON, self.OpenResult, self.bt_Result)
        self.Bind(wx.EVT_BUTTON, self.OnFileOpen, bt_choose_dir)
        self.Bind(wx.EVT_BUTTON, self.OnClear, self.bt_Clear)
        self.Bind(wx.EVT_MENU, self.OnAbout, item3_2)

        
#Set Launch state of buttons        

        self.bt_Clear.Disable()
        self.bt_Final.Disable()
        self.bt_Result.Disable()
        self.bt_Reset.Disable()
#^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^Function Definations^^^^^^^^^^^^^^
#::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

        #My Variables
        self.files_in_folder = []

    def OnFileOpen(self, event):
        """ File|Open event - Open dialog box. """
        self.dirname = ''
        dlg = wx.DirDialog(self, "Choose a folder", self.dirname)
        if (dlg.ShowModal() == wx.ID_OK):
            self._selectedDir = dlg.GetPath()
            self.files_in_folder = GetTheFiles(self._selectedDir)
            self.bt_Clear.Enable()
            self.loadResult_Normal()

#^-^-^-^-^-^-^-^-^-^-^-^-^-^-^-^-^-^-^-^-^-^-^-^-^-^-^-^-^-^-^-^-
    def OnFileExit(self, event):
        """ File|Exit event """
        self.Close()

    def OpenResult(self, event):
        import platform
        target_dir = os.path.join(self._selectedDir, 'modified')
        if platform.system == 'Windows':
            from os import startfile
            if os.path.isdir(target_dir):
                startfile(os.path.join(target_dir))
            else:
                wx.MessageBox('Folder does not exist...',
                        wx.OK | wx.ICON_INFORMATION
                        )
        else:
            os.system('xdg-open "%s"' % target_dir)

    def Process(self, event):
        Renamer(
                self._selectedDir,
                self.mod_text,
                self.prefix,
                self.suffix,
                self.file_ext
                )

        self.bt_Result.Enable()
        wx.MessageBox('DONE...Please check the folder "Modified"',
                    'Info',
                    wx.OK | wx.ICON_INFORMATION
                    )

    def loadResult_Modified(self, event):
        self.mod_text = self.Replacement_Text.GetValue()
        self.prefix = self.cb1.GetValue()
        self.suffix = self.cb2.GetValue()
        self.file_ext = self.cb3.GetValue()

        if not any((self.prefix, self.suffix, self.file_ext)):
            wx.MessageBox('Please select atleast one flag from Prefix ,Suffix or File Extension',
                    'Info',
                    wx.OK | wx.ICON_INFORMATION
                    )
            return

        if self.files_in_folder:
            if self.mod_text:
                self.bt_Final.Enable()
                self.mod_list = rename_preview(
                        self.files_in_folder,
                        self.mod_text,
                        self.prefix,
                        self.suffix,
                        self.file_ext
                        )
            else:
                wx.MessageBox('No text provided', 'Info', wx.OK | wx.ICON_INFORMATION)
                return
        else:
            wx.MessageBox('No files to process', 'Info', wx.OK | wx.ICON_INFORMATION)
            return
        # clear the Result listctrl
        self.Files_List2.DeleteAllItems()
        self.index = 0  # First declaration
        # load each data row
        
        for i in range(len(self.mod_list)):

            self.Files_List2.InsertStringItem(self.index, self.mod_list[i])
            # max rows value and starting point , here resource management by dynamic allocation
            self.index += 1
        self.statusbar.SetStatusText(str(len(self.mod_list)) + " files will be renamed") #Display results on staus bar

    def loadResult_Normal(self):
        self.bt_Reset.Enable()
        if self.files_in_folder:
            pass
        else:
            wx.MessageBox(
                    'This folder is empty',
                    'Info',
                    wx.OK | wx.ICON_INFORMATION
                    )
            return
        
        # clear the Result listctrl
        self.Files_List1.DeleteAllItems()
        self.index = 0  # First declaration
        # load each data row
        for i in range(len(self.files_in_folder)):

            self.Files_List1.InsertStringItem(
                    self.index,
                    self.files_in_folder[i]
                    )  #max rows value and starting point ,
            #here resource management by dynamic allocation
            self.index += 1
        self.statusbar.SetStatusText(
                str(len(self.files_in_folder)) + " files found") #Display results on status bar

    def OnReset(self, event):
        #This will clear all display sections.
        self.Files_List1.DeleteAllItems()
        self.Files_List2.DeleteAllItems()
        self.Replacement_Text.Clear()
        self.cb1.SetValue(False)
        self.cb2.SetValue(False)
        self.cb3.SetValue(False)
        #We are clearing all list so all previous data is flashed.
        #Clear status bar and deactivate Export button
        self.bt_Clear.Disable()
        self.bt_Result.Disable()
        self.bt_Reset.Disable()
        self.statusbar.SetStatusText("Ready")
        
    def OnClear(self, event):
        self.Files_List1.DeleteAllItems()
        self.bt_Clear.Disable()
        self.bt_Final.Disable()

    def OnAbout(self, event):

        description = """\t Rename all files in a folder at once. Can add text to start
        or end of a file
        ."""

        licence = "For internal purpose only."
        info = wx.AboutDialogInfo()

        #info.SetIcon(wx.Icon('icons/hunter.png', wx.BITMAP_TYPE_PNG))
        info.SetName('Multi File Renamer')
        info.SetVersion('1.0.0')
        info.SetDescription(description)
        info.SetCopyright('(C) 2013 Arindam Roychowdhury')
       # info.SetWebSite('arindam31@yahoo.co.in')
        info.SetLicence(licence)
        info.AddDeveloper('Arindam Roychowdhury')
        
        wx.AboutBox(info)
#^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
#::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::


if __name__ == '__main__':
    app = wx.App()
    TheRenamer(None, title='Multi File Renamer')
    app.MainLoop()
