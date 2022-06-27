import tkinter as tk
from config import _HEIGHT, _WIDHTH
from pages import *
import tkinter.messagebox as msg


class MenuBar(tk.Frame):
    def __init__(self):
        tk.Frame.__init__(self)
        self.config(bg='grey')

        self.widgets()
        self.layout()

    def widgets(self):
        self.homeBTN = tk.Button(self, text="home", command=None)
        self.settingsBTN = tk.Button(self, text = "settings", command = None)
        self.powerBTN = tk.Button(self, text = "power", command = lambda : self.poweroff())
        self.networkBTN = tk.Button(self, text = "network", command = None)


    def layout(self):
        self.columnconfigure(0, weight=1)
        for i in range(10):
            self.rowconfigure(i, weight = 1)


        self.homeBTN.grid(row=0, column=0, sticky="news")
        self.settingsBTN.grid(row=1, column=0, sticky="news")
        self.networkBTN.grid(row=2, column=0, sticky="news")
        self.powerBTN.grid(row=9, column=0, sticky="news")

    def poweroff(self):
        pass


class PageContainer(tk.Frame):
    def __init__(self):
        tk.Frame.__init__(self)
        self.config(bg='grey')
        self.name = None
        self.rowconfigure(0, weight=1)
        self.columnconfigure(0, weight=1)

        self.homepage = Homepage(self)
        self.settings = Settings(self)
        self.network = Network(self)


class View(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)
        self.geometry(_WIDHTH+"x"+_HEIGHT+"-0+0")
        self.overrideredirect(1)

        self.initWidgets()
        self.layout()

        self.pageContainer.homepage.show()

    def initWidgets(self):
        self.menuBar = MenuBar()
        self.pageContainer = PageContainer()

        self.menuBar.homeBTN.config(command=lambda:self.pageContainer.homepage.show())
        self.menuBar.settingsBTN.config(command=lambda:self.pageContainer.settings.show())
        self.menuBar.powerBTN.config(command = lambda :self.poweroff())
        self.menuBar.networkBTN.config(command = lambda : self.pageContainer.network.show())


    def layout(self):

        self.columnconfigure(0, weight=1)
        self.columnconfigure(1, weight=8)
        self.rowconfigure(0, weight=1)

        self.menuBar.grid(row=0, column=0, sticky="news")
        self.pageContainer.grid(row=0, column=1, sticky="news")

    def run(self):
        self.mainloop()

    def poweroff(self):
        answer = msg.askyesno("POWER OFF???", "POWER OFF???")
        if answer:
            self.destroy()


    def updateVaules(self):
        self.pageContainer.homepage.update()

if __name__ == '__main__':

    testApp = View()
    testApp.run()