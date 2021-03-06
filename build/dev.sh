#!/bin/sh

cd /home/user/CLionProjects/evsieve/target/release/ || { echo "Error changing directory"; exit 1; }
sudo ./evsieve --input /dev/input/by-id/usb-Logitech_USB_Receiver-if02-event-mouse grab \
        --hook key:delete toggle \
        --block key:delete \
        --toggle "" @norm_layout @dev_layout \
        --map key:c@dev_layout key:leftctrl key:c \
        --map key:v@dev_layout key:leftctrl key:v \
        --map key:x@dev_layout key:leftctrl key:x \
        --map key:a@dev_layout key:leftctrl key:a \
        --map key:z@dev_layout key:leftctrl key:z \
        --map key:y@dev_layout key:leftctrl key:y \
        --map key:f@dev_layout key:leftctrl key:f \
        --map key:s@dev_layout key:leftctrl key:s \
        --map key:e@dev_layout btn:left \
        --map key:d@dev_layout btn:middle \
        --map key:w@dev_layout btn:right \
        --map key:r@dev_layout key:leftalt key:tab \
        --map key:t@dev_layout key:leftctrl key:t \
        --map key:4@dev_layout key:leftctrl key:leftalt key:b \
        --map key:5@dev_layout key:leftalt key:leftshift key:left \
        --map key:insert@dev_layout key:leftalt key:enter \
        --map key:slash@dev_layout key:leftctrl key:slash \
        --map key:g@dev_layout key:leftshift key:f6 \
        --map key:l@dev_layout key:leftctrl key:leftalt key:l \
        --output