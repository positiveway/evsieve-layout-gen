#!/bin/sh

sudo /home/user/CLionProjects/evsieve/target/release/evsieve --input /dev/input/by-id/usb-Logitech_USB_Receiver-if02-event-mouse grab \
        --hook key:insert  toggle=:1 \
        --hook key:delete  toggle=:2 \
        --block key:insert key:delete \
        --toggle "" @norm_layout @dev_layout \
        --map key:c@dev_layout key:leftctrl key:c \
        --map key:v@dev_layout key:leftctrl key:v \
        --map key:x@dev_layout key:leftctrl key:x \
        --map key:z@dev_layout key:leftctrl key:z \
        --map key:f@dev_layout key:leftctrl key:f \
        --map key:w@dev_layout key:leftctrl key:w \
        --map key:l@dev_layout key:leftctrl key:leftalt key:l \
        --output