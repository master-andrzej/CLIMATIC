***************************************************************
source:
https://www.waveshare.com/wiki/7inch_HDMI_LCD_(C)
***************************************************************


Introduction
7-inch HDMI display, with a resolution of 1024×600 and a capacitive touch panel, which supports Raspberry Pi and can also be used as a computer monitor.

More
Features
7-inch IPS screen with a hardware resolution of 1024×600.
5-points capacitive touch control.
Using with Raspberry Pi, it supports Raspbian / Ubuntu / Kali / Retropie and WIN10 IoT, no need to install any drivers.
Using as a computer monitor, it supports Windows 10 / 8.1 / 8 / 7, five-point touch, no need to install any drivers.
Support backlight control, more power saving.
Instructions
Working with PC
This LCD can support Windows 7/8 / 8.1 / 10 system.

How to use:

1) Turn on the backlight switch on the back of the LCD.

2) Connect the Touch interface of the LCD to the USB interface of the PC. Wait for a while, the windows will automatically recognize the touch function.

3) Connect the HDMI interface of the LCD to the HDMI interface of the PC.

Note: When the computer is connected to several different displays at the same time, only this LCD can be used to control the cursor on the main display, so we recommended to set this LCD as the main display.

Working with Raspberry Pi
This LCD can support Raspbian / Ubuntu / Kali / Retropie and WIN10 IoT systems. When the LCD works on systems such as Raspberry Pi, the resolution must be set manually, otherwise, it will cause abnormal display. There is no such problem when the LCD works on the PC version of Windows.

Please download the latest version of the image on the Raspberry Pi official website.

1) Download the compressed file to the PC, and unzip it to get the .img file.

2) Connect the TF card to the PC, use SDFormatter.exe software to format the TF card.

3) Open the Win32DiskImager.exe software, select the system image downloaded in step 1, and click‘Write’ to write the system image.

4) After the image has finished writing, open the config.txt file in the root directory of the TF card, add the following code at the end of config.txt, then save and quit the TF card safely.

max_usb_current=1
hdmi_group=2
hdmi_mode=87
hdmi_cvt 1024 600 60 6 0 0 0
hdmi_drive=1
5) Insert the TF card into the Raspberry Pi

6) Turn on the backlight switch on the back of the LCD.

7) Connect the Touch interface of the LCD to the USB interface of the Raspberry Pi.

8) Connect the HDMI interface of the LCD to the HDMI interface of the Raspberry Pi, power on the Raspberry Pi, and wait for a few seconds until the LCD displays normally.

Touch Settings on Win 10 PC
Some users want to connect more than one display to their PC. Here we talk about how to setting the touch to make the touchscreen control its screen separately.

Connect touchscreen to PC. Here we use a standard PC monitor and connect a 7inch HDMI LCD (C) for example. We make the monitor as the main screen and the touchscreen as a secondary screen.
By default, The touchscreen can only control the cursor on the main screen. Here we set it to control the secondary screen.
Open Control Panel and search Tablet PC setting on the control panel and open the tool.


Rotation(Working with Raspberry Pi)
Display Rotating

Add this statement in the config.txt file (the config file is located in the root directory of the TF card, which is named /boot):

display_rotate=1 #1：90；2: 180； 3: 270
Note: For Raspberry Pi 4, you need to comment out dtoverlay=vc4-fkms-V3D.

#dtoverlay=vc4-fkms-V3D.
And then restart the Raspberry Pi after saving.

sudo reboot
Touch Rotating

After the display is rotated, the position of touch is incorrect because the touch doesn’t change with the display angle. So the touch also needs to be modified.

1.Install libinput.

sudo apt-get install xserver-xorg-input-libinput
If the system you installed is Ubuntu or Jetson Nano. The installation code is:

sudo apt install xserver-xorg-input-synaptics
2.Create the xorg.conf.d directory under /etc/X11/ (if the directory already exists, proceed directly to step 3).

sudo mkdir /etc/X11/xorg.conf.d
3.Copy the 40-libinput-conf file to the directory you created just now.

sudo cp /usr/share/X11/xorg.conf.d/40-libinput.conf /etc/X11/xorg.conf.d/
4.Edit this file.

sudo nano /etc/X11/xorg.conf.d/40-libinput.conf
Find the part of the touchscreen, add the following statement inside, and then save the file.

Option "CalibrationMatrix" "0 1 0 -1 0 1 0 0 1"
Similar to the picture below:

Touch roate.jpg
5. Restart the Raspberry Pi.

sudo reboot
Note:

90 degree rotation: Option "CalibrationMatrix" "0 1 0 -1 0 1 0 0 1"

180 degree rotation: Option "CalibrationMatrix" "-1 0 1 0 -1 1 0 0 1"

270 degree rotation: Option "CalibrationMatrix" "0 -1 1 1 0 0 0 0 1"