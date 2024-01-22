#!/usr/bin/python3
# File name   : setup.py
# Author      : Adeept
# Date        : 2020/3/14

import os
import time

curpath = os.path.realpath(__file__)
thisPath = "/" + os.path.dirname(curpath)

def replace_num(file,initial,new_num):  
    newline=""
    str_num=str(new_num)
    with open(file,"r") as f:
        for line in f.readlines():
            if(line.find(initial) == 0):
                line = (str_num+'\n')
            newline += line
    with open(file,"w") as f:
        f.writelines(newline)

for x in range(1,4):
	if os.system("sudo apt-get update") == 0:
		break

os.system("sudo raspi-config nonint do_legacy 0")
os.system("sudo apt-get purge -y wolfram-engine")
os.system("sudo apt-get purge -y libreoffice*")
os.system("sudo apt-get -y clean")
os.system("sudo apt-get -y autoremove")

# for x in range(1,4):
# 	if os.system("sudo apt-get -y upgrade") == 0:
# 		break

for x in range(1,4):
	if os.system("sudo pip3 install -U pip") == 0:
		break

for x in range(1,4):
	if os.system("sudo apt-get install -y python-dev python-pip libfreetype6-dev libjpeg-dev build-essential") == 0:
		break

for x in range(1,4):
	if os.system("sudo -H pip3 install --upgrade luma.oled") == 0:
		break

for x in range(1,4):
	if os.system("sudo apt-get install -y i2c-tools") == 0:
		break

for x in range(1,4):
	if os.system("sudo pip3 install adafruit-pca9685") == 0:
		break

for x in range(1,4):
	if os.system("sudo pip3 install rpi_ws281x") == 0:
		break

for x in range(1,4):
	if os.system("sudo apt-get install -y python3-smbus") == 0:
		break

for x in range(1,4):
	if os.system("sudo pip3 install mpu6050-raspberrypi") == 0:
		break

for x in range(1,4):
	if os.system("sudo pip3 install flask") == 0:
		break

for x in range(1,4):
	if os.system("sudo pip3 install flask_cors") == 0:
		break

for x in range(1,4):
	if os.system("sudo pip3 install websockets") == 0:
		break

try:
	replace_num("/boot/config.txt",'#dtparam=i2c_arm=on','dtparam=i2c_arm=on\nstart_x=1\n')
except:
	print('try again')

for x in range(1,4):
	if os.system("sudo apt-get -y install libqtgui4 libhdf5-dev libhdf5-serial-dev libatlas-base-dev libjasper-dev libqt4-test") == 0:
		break

for x in range(1,4):
	if os.system("sudo pip3 install imutils zmq pybase64 psutil") == 0:   ####
		break

for x in range(1,4):
	if os.system("sudo git clone https://github.com/oblique/create_ap") == 0:
		break

try:
	os.system("cd " + thisPath + "/create_ap && sudo make install")
except:
	pass

try:
	os.system("cd //home/pi/create_ap && sudo make install")
except:
	pass

for x in range(1,4):
	if os.system("sudo apt-get install -y util-linux procps hostapd iproute2 iw haveged dnsmasq") == 0:
		break

for x in range(1,4):
	if os.system("sudo pip uninstall -y numpy") == 0:
		break

for x in range(1,4):
	if os.system("sudo apt-get -y install libgraphite2-3 libatspi2.0-0 libthai0 libxcb-shm0 libxcb-render0 libswscale5 librsvg2-2 libvorbisenc2 libavutil56 libzvbi0 libgsm1 libxinerama1 libxvidcore4 libsrt1.4-gnutls libswresample3 libatk1.0-0 libvorbisfile3 libogg0 libpangoft2-1.0-0 libpgm-5.3-0 libwayland-egl1 libharfbuzz0b libpango-1.0-0 libcairo2 libva-x11-2 libwayland-cursor0 libgfortran5 libxfixes3 libgme0 libxrender1 libvorbis0a libxi6 libudfread0 libspeex1 libwebpmux3 libsodium23 libdatrie1 libatk-bridge2.0-0 libxrandr2 libbluray2 libx264-160 libwavpack1 libxcomposite1 libpangocairo-1.0-0 libsoxr0 libshine3 libxkbcommon0 libvdpau1 libgtk-3-0 libopus0 librabbitmq4 libgdk-pixbuf-2.0-0 libavformat58 libmpg123-0 libxdamage1 libzmq5 libdav1d4 libopenmpt0 libatlas3-base libva2 libva-drm2 libxcursor1 libssh-gcrypt-4 libavcodec58 libaom0 libx265-192 libwayland-client0 libcairo-gobject2 libcodec2-0.9 libpixman-1-0 libdrm2 libsnappy1v5 libnorm1 libopenjp2-7 libtheora0 ocl-icd-libopencl1 libtwolame0 libvpx6 libepoxy0 libchromaprint1 libmp3lame0") == 0:
		break

for x in range(1,4):
	if os.system("sudo pip3 install opencv-python") == 0:					# would auto install correct numpy version
		break

#setup boot
try:
	os.system('sudo touch //lib/systemd/system/raspclaws.service')
	with open("//lib/systemd/system/raspclaws.service",'w') as file_to_write:
		file_to_write.write("[Unit]\n")
		file_to_write.write("Description=RaspClaws Service\n")
		file_to_write.write("After=multi-user.target\n\n")
		file_to_write.write("[Service]\n")
		file_to_write.write("Type=idle\n")
		file_to_write.write("ExecStart=sudo /usr/bin/python " + thisPath + "/server/webServer.py\n\n")
		file_to_write.write("[Install]\n")
		file_to_write.write("WantedBy=multi-user.target\n")
		#you can choose how to control the robot
		# file_to_write.write("#!/bin/sh\nsudo python3 " + thisPath + "/server/server.py")
except:
	pass

os.system('sudo chmod 644 /lib/systemd/system/raspclaws.service')
os.system('sudo systemctl daemon-reload')
os.system('sudo systemctl enable raspclaws.service')

#fix conflict with onboard Raspberry Pi audio
with open('/usr/local/lib/python3.9/dist-packages/Adafruit_GPIO/Platform.py','r') as file :
	filedata = file.read()

filedata = filedata.replace('BCM2835','BCM2711')

with open('/usr/local/lib/python3.9/dist-packages/Adafruit_GPIO/Platform.py','w') as file :
	file.write(filedata)

try:
	os.system('sudo touch /etc/modprobe.d/snd-blacklist.conf')
	with open("/etc/modprobe.d/snd-blacklist.conf",'w') as file_to_write:
		file_to_write.write("blacklist snd_bcm2835")
except:
	pass

print('The program in Raspberry Pi has been installed, disconnected and restarted. \nYou can now power off the Raspberry Pi to install the camera and driver board (Robot HAT). \nAfter turning on again, the Raspberry Pi will automatically run the program to set the servos port signal to turn the servos to the middle position, which is convenient for mechanical assembly.')
print('restarting...')
os.system("sudo reboot")

