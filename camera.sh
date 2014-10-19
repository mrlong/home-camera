#!/bin/sh

sudo raspistill -t 5000 -w 600 -h 480  -o a.jpg
#sudo raspivid -t 50000 -o a.h264
#sudo MP4Box -add a.h264 a.mp4
sudo python camera.py
