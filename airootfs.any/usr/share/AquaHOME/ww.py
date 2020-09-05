import wx
import subprocess

class MyApp(wx.Frame):

    def __init__(self, *args, **kw):
        super(MyApp, self).__init__(*args, **kw)

        self.init_ui()

    def init_ui(self):
        self.SetTitle('Aqua HOME')
        self.SetSize((1000, 700))
        self.Show()

        panel_ui = wx.Panel(self, -1, pos=(0, 0), size=(1000, 700))

        image = wx.Image('/usr/share/AquaHOME/aqua.png')
        bitmap = image.ConvertToBitmap()
        btn = wx.Button(panel_ui, -1, 'インストール', pos=(65, 350))
        btn = wx.Button(panel_ui, -1, 'インストール', pos=(65, 330))
        btn = wx.Button(panel_ui, -1, 'インストール', pos=(65, 310))
        ver = wx.Button(panel_ui, -1, '  バージョン ', pos=(750, 350))
        ver = wx.Button(panel_ui, -1, '  バージョン ', pos=(750, 330))
        ver = wx.Button(panel_ui, -1, '  バージョン ', pos=(750, 310))
        auto = wx.Button(panel_ui, -1, '自動起動を無効化', pos=(520, 310))
        auto = wx.Button(panel_ui, -1, '自動起動を無効化', pos=(520, 350))
        auto = wx.Button(panel_ui, -1, '自動起動を無効化', pos=(520, 330))
        con = wx.Button(panel_ui, -1, 'コントロールパネル', pos=(290, 310))
        con = wx.Button(panel_ui, -1, 'コントロールパネル', pos=(290, 350))
        con = wx.Button(panel_ui, -1, 'コントロールパネル', pos=(290, 330))
        self.Bind(wx.EVT_BUTTON, self.closebutton, btn)
        self.Bind(wx.EVT_BUTTON, self.ver, ver)
        self.Bind(wx.EVT_BUTTON, self.auto, auto)
        wx.StaticBitmap(panel_ui, -1, bitmap, pos=(5, 0), size=image.GetSize())

    def closebutton(self,event):
        subprocess.run(['pkexec','/usr/bin/calamares'])

    def ver(self,event):
        subprocess.run(['python3','/usr/share/AquaHOME/py.py'])

    def auto(self,event):
        subprocess.run(['gksu','del'])

    def con(self,event):
        subprocess.run(['con'])


app = wx.App()
MyApp(None)
app.MainLoop()