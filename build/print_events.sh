#!/bin/sh

cd /home/user/CLionProjects/evsieve/target/release/ || { echo "Error changing directory"; exit 1; }
sudo ./evsieve --input /dev/input/by-id/usb-Logitech_USB_Receiver-if02-event-mouse --print