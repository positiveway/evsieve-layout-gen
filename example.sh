evsieve --input /dev/input/by-id/keyboard grab \
        --hook key:f8  toggle=:1 \
        --hook key:f10 toggle=:2 \
        --toggle "" @norm_layout @dev_layout \
        --map key:c@dev_layout key:leftctrl key:c \
        --map key:v@dev_layout key:leftctrl key:v \
        --map key:l@dev_layout key:leftctrl key:leftalt key:l \
        --output