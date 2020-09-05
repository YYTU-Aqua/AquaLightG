#797,575
import wx


class MyApp(wx.Frame):

    def __init__(self, *args, **kw):
        super(MyApp, self).__init__(*args, **kw)

        self.init_ui()

    def init_ui(self):
        self.SetTitle('バージョン')
        self.SetSize((797, 575))
        self.Show()

        panel_ui = wx.Panel(self, -1, pos=(0, 0), size=(797, 575))

        image = wx.Image('/usr/share/AquaHOME/ver.png')
        bitmap = image.ConvertToBitmap()

        wx.StaticBitmap(panel_ui, -1, bitmap, pos=(0, 0), size=image.GetSize())


app = wx.App()
MyApp(None)
app.MainLoop()