import tkinter as tk
from temp import  _TEMPERATURE, _HUMIDITY
pages = ["Homepage", "Settings", "Network"]


class Page(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        self.pageName = None
        self.label = tk.Label(self, text = str(self.pageName))

    def show(self):
        self.grid(row=0, column=0, sticky="news")
        self.lift()


class Homepage(Page):
    def __init__(self, master):
        Page.__init__(self, master)
        self.pageName = "HOMEPAGE"
        self.config(bg='grey')

        self.columnconfigure(0, weight = 1)
        self.columnconfigure(1, weight =1)

        self.rowconfigure(0, weight=1)
        self.rowconfigure(1, weight=4)

        self.temperatureLabelFrame= tk.LabelFrame(self, text="Temperature", font=("Arial, 30"))
        self.temperatureLabel = tk.Label(self.temperatureLabelFrame, text=str(_TEMPERATURE) +' \N{DEGREE SIGN}', font = ("Arial", 50) )
        self.temperatureLabel.pack(expand=True)
        self.temperatureLabelFrame.grid(row=0, column=0, sticky="news")


        self.humidityLabelFrame = tk.LabelFrame(self, text = "Humidity", font=("Arial, 30"))
        self.humidityLabel = tk.Label(self.humidityLabelFrame, text = str(_HUMIDITY)+" %", font = ("Arial", 50))
        self.humidityLabel.pack(expand=True)
        self.humidityLabelFrame.grid(row=0, column=1, sticky="news")

    def updateValues(self, newHumidity, newTemperature):
        self.humidityLabel.config(text = str(newHumidity)+" %")
        self.temperatureLabel.config(text=str(newTemperature) +' \N{DEGREE SIGN}',)


class Settings(Page):
    def __init__(self, master):
        Page.__init__(self, master)
        self.pageName = "SETTINGS"
        self.config(bg='brown')



class Network(Page):
    def __init__(self, master):
        Page.__init__(self, master)
        self.pageName = "NETWORK"
        self.config(bg='orange')


