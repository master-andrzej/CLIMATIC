import ipaddress
import time
import tkinter as tk
import tkinter.messagebox as messagebox
import os
import subprocess
import socket
import platform

####################################################################################
# global variables

_appPath = "./src/GUI/view.py"
_gitPath = ""
_theme = "grey"
_imgPath = "../img/"

_fullSizeWindow = "1024x600"
_bigWindow = "300x300"
_smallWindow = "50x50"
_windowPosition = "-0+0"

_mainAppIsRunning = False
####################################################################################
######## main window parameters

root = tk.Tk()
root.attributes("-topmost", True)
root.wm_attributes()


root.geometry(_bigWindow+_windowPosition)
#root.wm_attributes('-toolwindow', True)
root.overrideredirect(1)

    ####################################################################################
    ######## frame1

frame1 = tk.Frame(root, bg="grey")

    #buttons images
runIMG = tk.PhotoImage(file = _imgPath+"start.png").subsample(20,20)
stopIMG = tk.PhotoImage(file = _imgPath+"stop.png").subsample(20,20)
restartIMG = tk.PhotoImage(file = _imgPath+"restart.png").subsample(20,20)
updateIMG = tk.PhotoImage(file = _imgPath+"update.png").subsample(20,20)
poweroffIMG = tk.PhotoImage(file = _imgPath+"poweroff.png").subsample(20,20)
minimizeIMG = tk.PhotoImage(file = _imgPath+"minimize.png").subsample(20,20)
settingsIMG = tk.PhotoImage(file = _imgPath+"settings.png").subsample(20,20)

    #buttons
runBTN = tk.Button(frame1, text="run", bg = _theme, image = runIMG, compound="top")
stopBTN = tk.Button(frame1, text ="stop", bg=_theme, image=stopIMG, compound="top")
restartBTN = tk.Button(frame1, text = "restart", bg =_theme, image=restartIMG, compound="top")
updateBTN = tk.Button(frame1, text="update", bg=_theme, image=updateIMG, compound="top")
poweroffBTN = tk.Button(frame1, text="poweroff",bg=_theme, image=poweroffIMG, compound="top")
minimizeBTN = tk.Button(frame1, text = "minimalize",bg =_theme, image=minimizeIMG, compound="top")
settingsBTN = tk.Button(frame1, text = "settings", bg = _theme, image=settingsIMG, compound="top")

    #layout
frame1.rowconfigure(0, weight=1)
frame1.rowconfigure(1, weight=1)
frame1.rowconfigure(2, weight=1)
frame1.rowconfigure(3, weight=1)
frame1.columnconfigure(0, weight=1)
frame1.columnconfigure(1, weight=1)

runBTN.grid(row=0, column=0, sticky="news")
stopBTN.grid(row=0, column=1, sticky="news")
restartBTN.grid(row=1, column=0, sticky="news")
updateBTN.grid(row=1, column=1, sticky="news")
poweroffBTN.grid(row=3, column=0, sticky="news")
minimizeBTN.grid(row=3, column=1, sticky="news")
settingsBTN.grid(row=2, column=0, sticky="news")

    #buttons commands
minimizeBTN.config(command=lambda :minimalize())
poweroffBTN.config(command=lambda :poweroff())
runBTN.config(command=lambda :run())
stopBTN.config(command=lambda :stop())
updateBTN.config(command=lambda :update())
restartBTN.config(command=lambda: restart())
settingsBTN.config(command=lambda :settings())

    #functions frame1
def poweroff():
    if messagebox.askyesno("poweroff???","poweroff???"):
        os.system("poweroff")

def run():
    global _mainAppIsRunning, app, _appPath
    if _mainAppIsRunning == False:
        app = subprocess.Popen(["python3",_appPath])
        _mainAppIsRunning = True
    else:
        print("main app is already running!!!")
        messagebox.showinfo(title="INFO",message="App is already running!!!")

def stop():
    global _mainAppIsRunning, app
    if _mainAppIsRunning==True:
        app.kill()
        _mainAppIsRunning = False
    else:
        print("first start app!!!")
        messagebox.showinfo(title="INFO", message="App is already stopped!!!")

def restart():
    global _mainAppIsRunning
    if _mainAppIsRunning==True:
        stop()
        time.sleep(2)
        run()
    else:
        print("first start app!!!")
        messagebox.showinfo(title="INFO", message="First need to start app!!!")

def update():
    if _mainAppIsRunning == True:
        messagebox.showerror("ERROR", "First stop currently opened app!", parent=root)
    else:
        if messagebox.askyesno(title="UPDATE", message="Do you want update to the newest version???"):
            pass

def minimalize(*args):
    root.geometry(_smallWindow)
    frame1.forget()
    frame2.pack(expand=True, fill="both")

def settings():
    frame1.forget()
    frame3.pack(expand=True, fill="both")
    root.geometry(_fullSizeWindow)

    ####################################################################################
    ######## frame2

frame2 = tk.Frame(root)

    #buttons images
maximalizeIMG = tk.PhotoImage(file=_imgPath+"maximalize.png").subsample(20, 20)

    #buttons
maximalizeBTN = tk.Button(frame2, text="maximalize", bg=_theme, image=maximalizeIMG)

    #layout
maximalizeBTN.pack(expand=True, fill="both")

    #button commands
maximalizeBTN.config(command=lambda: maximalize())

    #functions frame2
def maximalize():
    root.geometry(_bigWindow)
    frame2.forget()
    frame1.pack(expand=True, fill="both")

####################################################################################
######## frame3

frame3 = tk.Frame(root)

frame3.rowconfigure(0, weight=20)
frame3.rowconfigure(1, weight=1)

frame3.columnconfigure(0, weight=20)
frame3.columnconfigure(1, weight=1)

# frame3 widgets
sliderFrame = tk.Scale(frame3, from_=0, to=100, showvalue = False)
sliderFrame.grid(row=0, column=1, sticky="news")

contentFrame = tk.Frame(frame3)
contentFrame.propagate(0)
contentFrame.grid(row = 0, column = 0, sticky="news")

font="Arial, 16"

"""networkFrame = tk.LabelFrame(contentFrame, text="Network:", font=font)
networkFrame.pack(expand=True, fill='both')

if platform.machine() == "AMD64":
    data = subprocess.check_output(['ipconfig', '/all']).decode('utf-8').split('\n')

elif platform.machine()=="ARM7":
    data = subprocess.check_output(['ifconfig', '-a']).decode('utf-8').split('\n')"""


#networkParameters=""
"""for item in data:
    if item != "":
        networkParameters = networkParameters +"\n"+str(item.split('\r')[:-1])

        print(item.split()[:-3])"""


"""networkParametersLabel = tk.Label(networkFrame, text=networkParameters)
networkParametersLabel.pack(side="left")"""

languageFrame = tk.LabelFrame(contentFrame, text="Language:", font=font)
languageFrame.pack(expand=True, fill="both")

parametersFrame = tk.LabelFrame(contentFrame, text="Parameters:", font=font)
parametersFrame.pack(expand=True, fill="both")

communicationFrame = tk.LabelFrame(contentFrame, text = "Communication:", font=font)
communicationFrame.pack(expand=True, fill="both")



steeringFrame = tk.Frame(frame3, relief="groove", borderwidth=2)
steeringFrame.propagate(0)
steeringFrame.grid(row=1, column=0, sticky="news", columnspan=2)
steeringFrame.rowconfigure(0, weight=1)

for i in range(5):
    steeringFrame.columnconfigure(i, weight=1)


# buttons images
backIMG = tk.PhotoImage(file=_imgPath+"back.png").subsample(15,15)

# buttons
applyBTN = tk.Button(steeringFrame, text="Apply")
cancelBTN = tk.Button(steeringFrame, text="Cancel")
backBTN=tk.Button(steeringFrame, text="back", image=backIMG)

# buttons commands
applyBTN.config(command=lambda: apply())
cancelBTN.config(command=lambda: cancel())
backBTN.config(command=lambda: back())

backBTN.grid(row=0, column=0, sticky="news")
cancelBTN.grid(row=0, column=3, sticky="news")
applyBTN.grid(row=0, column=4, sticky="news")




# functions frame3

def apply():
    pass


def cancel():
    answer = messagebox.askyesnocancel("Cancel", "Do you want to discard changes?")
    if answer == True:
        print("settings saved")
        back()
    elif answer == False:
        print("discard changes")
        back()


def back():
    root.geometry(_bigWindow)
    frame3.forget()
    frame1.pack(expand=True, fill="both")

####################################################################################
# ######## main app


if __name__ == '__main__':
    minimalize()        # start window
    root.bind("<FocusOut>", minimalize)
    root.focus_set()
    root.mainloop()
