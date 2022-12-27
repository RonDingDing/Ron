import wx


class Example(wx.Frame):
    def __init__(self, *args, **kw):
        super(Example, self).__init__(*args, **kw)

        self.InitUI()

    def InitUI(self):

        pnl = wx.Panel(self)
        exitButton = wx.Button(pnl, wx.ID_ANY, "Exit", (10, 10))

        self.Bind(wx.EVT_BUTTON, self.OnExit, id=exitButton.GetId())

        self.SetTitle("Automatic id")
        self.Centre()
        self.Show(True)

    def OnExit(self, event):

        self.Close()


def main():

    ex = wx.App()
    Example(None)
    ex.MainLoop()


if __name__ == "__main__":
    main()
