#!/bin/bash

# This script is used to install MontionEye on a RPI installed with Raspbian.
# 
# Wajug Team
# October 2016
#

# This step is required to avoid any problems with the pip command
echo "Synchronise the clock"
sudo /etc/init.d/ntp stop
sudo ntpd -q -g
sudo /etc/init.d/ntp start

echo "Install ffmpeg"
sudo wget https://github.com/ccrisan/motioneye/wiki/precompiled/ffmpeg_3.1.1-1_armhf.deb
sudo dpkg -i ffmpeg_3.1.1-1_armhf.deb

echo "Update list of packages"
sudo apt-get update

echo "Install all dependencies"
sudo apt-get -y install python-pip python-dev curl libssl-dev libcurl4-openssl-dev libjpeg-dev libx264-142

echo "Install motion"
sudo wget https://github.com/ccrisan/motioneye/wiki/precompiled/motion-mrdave-raspbian -O /usr/local/bin/motion
sudo chmod +x /usr/local/bin/motion

echo "Install MotionEye"
sudo pip install motioneye

echo "Prepare the conf directory"
sudo mkdir -p /etc/motioneye
sudo cp /usr/local/share/motioneye/extra/motioneye.conf.sample /etc/motioneye/motioneye.conf

echo "Create the media directory"
sudo mkdir -p /var/lib/motioneye

echo "Prepare the init script"
sudo cp /usr/local/share/motioneye/extra/motioneye.systemd-unit-local /etc/systemd/system/motioneye.service
sudo systemctl daemon-reload
sudo systemctl enable motioneye
sudo systemctl start motioneye

echo "Append the video driver"
grep -q bcm2835_v4l2 /etc/modules || echo bcm2835_v4l2 | sudo tee --append /etc/modules

echo "Done!"

echo "Do not forget to enable your camera with:"
echo "sudo raspi-config"
echo "-> enable camera"
echo "-> finish"
echo "-> reboot"
