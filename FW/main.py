print("Starting")

import board
from kmk.kmk_keyboard import KMKKeyboard
from kmk.keys import KC
from kmk.scanners import DiodeOrientation
from kmk.handlers.sequences import send_string, simple_key_sequence
from kmk.modules.layers import Layers
from kmk.modules.tapdance import TapDance
from kmk.extensions.media_keys import MediaKeys
import io

keyboard = KMKKeyboard()

keyboard.row_pins = (board.GP2, board.GP12, board.GP18)
keyboard.col_pins = (board.GP25, board.GP24, board.GP4, board.GP3)
keyboard.diode_orientation = DiodeOrientation.COL2ROW

keyboard.modules = [Layers(), TapDance()]
keyboard.extensions.append(MediaKeys())

f=io.open(".hidden.txt", "rt")
pop_pswd=f.readline()
win_pswd=f.readline()
f.close()

# LAYERS

HOME_LAYER_LINUX = KC.DF(1)
HOME_LAYER_WINDOWS = KC.DF(9)

LAYER_1_LNX = KC.TD(KC.TO(1), KC.TO(5))
LAYER_2_LNX = KC.TD(KC.TO(2), KC.TO(6))
LAYER_3_LNX = KC.TD(KC.TO(3), KC.TO(7))
LAYER_4_LNX = KC.TD(KC.TO(4), KC.TO(8))

LAYER_1_WIN = KC.TD(KC.TO(9), KC.TO(13))
LAYER_2_WIN = KC.TD(KC.TO(10), KC.TO(14))
LAYER_3_WIN = KC.TD(KC.TO(11), KC.TO(15))
LAYER_4_WIN = KC.TD(KC.TO(12), KC.TO(16))

INFO = send_string("HOME LAYER\nPress Bottom Left button to enter LINUX mode\nPress Bottom Right button to enter WINDOWS mode\n\n\nXXXXX\tXXXXX\tXXXXX\tXXXXX\nXXXXX\tXXXXX\tXXXXX\tXXXXX\nLINUX\tXXXXX\tXXXXX\tWINDOWS\n")

POPOS_PSWD = send_string(pop_pswd)
WINDOWS_PSWD = send_string(win_pswd)


########## LINUX MACROS ##########
OPEN_TERMINAL = simple_key_sequence([KC.LGUI(KC.T), KC.MACRO_SLEEP_MS(500)])
CLEAR_TERMINAL = simple_key_sequence([send_string("clear"), KC.MACRO_SLEEP_MS(500), KC.ENTER])
EXIT_TERMINAL = simple_key_sequence([KC.LCTRL(KC.C), KC.MACRO_SLEEP_MS(100), send_string("exit"), KC.MACRO_SLEEP_MS(500), KC.ENTER])
MAINTAIN = simple_key_sequence([OPEN_TERMINAL, send_string("maintain"), KC.ENTER])

SHUTDOWN_IMMEDIATELY = simple_key_sequence([OPEN_TERMINAL, send_string("shutdown now"), KC.ENTER])
RESTART_IMMEDIATELY = simple_key_sequence([OPEN_TERMINAL, send_string("shutdown -r now"), KC.ENTER])
SUSPEND_IMMEDIATELY = simple_key_sequence([OPEN_TERMINAL, send_string("systemctl suspend -i && exit"), KC.ENTER])
REBOOT_ON_WINDOWS = simple_key_sequence([OPEN_TERMINAL, send_string("reboot_on_windows"), KC.MACRO_SLEEP_MS(200), KC.ENTER])
REBOOT = simple_key_sequence([OPEN_TERMINAL, send_string("reboot"), KC.ENTER])
HOSTS = simple_key_sequence([OPEN_TERMINAL, send_string("sudo nano /etc/hosts"), KC.ENTER, KC.MACRO_SLEEP_MS(200), POPOS_PSWD])

XXXXXX = KC.NO

#keymap
keyboard.keymap = [

### START LAYER ###
    [XXXXXX, INFO, INFO, INFO,
     INFO, INFO, INFO, INFO,
     HOME_LAYER_LINUX, INFO, INFO, HOME_LAYER_WINDOWS
    ],





########## LINUX LAYERS ##########

### LAYER 1 LINUX ###
    [LAYER_1_LNX, LAYER_2_LNX, LAYER_3_LNX, LAYER_4_LNX,
     OPEN_TERMINAL, CLEAR_TERMINAL, EXIT_TERMINAL, MAINTAIN,
     XXXXXX, HOSTS, XXXXXX, POPOS_PSWD
    ],


### LAYER 2 LINUX ###
    [LAYER_1_LNX, LAYER_2_LNX, LAYER_3_LNX, LAYER_4_LNX,
     send_string("LAYER 2 LINUX\n"), XXXXXX, XXXXXX, XXXXXX,
     XXXXXX, XXXXXX, XXXXXX, XXXXXX
    ],


### LAYER 3 LINUX ###
    [LAYER_1_LNX, LAYER_2_LNX, LAYER_3_LNX, LAYER_4_LNX,
     send_string("LAYER 3 LINUX\n"), XXXXXX, XXXXXX, XXXXXX,
     XXXXXX, XXXXXX, XXXXXX, XXXXXX
    ],


### LAYER 4 LINUX ###
    [LAYER_1_LNX, LAYER_2_LNX, LAYER_3_LNX, LAYER_4_LNX,
     KC.AUDIO_VOL_UP, KC.AUDIO_MUTE, XXXXXX, XXXXXX,
     KC.AUDIO_VOL_DOWN, KC.MEDIA_PREV_TRACK, KC.MEDIA_PLAY_PAUSE, KC.MEDIA_NEXT_TRACK
    ],


### LAYER 1.1 LINUX ###
    [LAYER_1_LNX, LAYER_2_LNX, LAYER_3_LNX, LAYER_4_LNX,
     send_string("LAYER 1.1 LINUX\n"), XXXXXX, XXXXXX, XXXXXX,
     XXXXXX, XXXXXX, XXXXXX, XXXXXX
    ],


### LAYER 2.1 LINUX ###
    [LAYER_1_LNX, LAYER_2_LNX, LAYER_3_LNX, LAYER_4_LNX,
     SUSPEND_IMMEDIATELY, XXXXXX, XXXXXX, REBOOT_ON_WINDOWS,
     RESTART_IMMEDIATELY, XXXXXX, XXXXXX, SHUTDOWN_IMMEDIATELY
    ],


### LAYER 3.1 LINUX ###
    [LAYER_1_LNX, LAYER_2_LNX, LAYER_3_LNX, LAYER_4_LNX,
     send_string("LAYER 3.1 LINUX\n"), XXXXXX, XXXXXX, XXXXXX,
     XXXXXX, XXXXXX, XXXXXX, XXXXXX
    ],


### LAYER 4.1 LINUX ###
    [LAYER_1_LNX, LAYER_2_LNX, LAYER_3_LNX, LAYER_4_LNX,
     send_string("LAYER 4.1 LINUX\n"), XXXXXX, XXXXXX, XXXXXX,
     XXXXXX, XXXXXX, XXXXXX, XXXXXX
    ],





########## WINDOWS LAYERS ##########

### LAYER 1 WINDOWS ###
    [LAYER_1_WIN, LAYER_2_WIN, LAYER_3_WIN, LAYER_4_WIN,
     send_string("LAYER 1 WINDOWS\n"), XXXXXX, XXXXXX, XXXXXX,
     XXXXXX, XXXXXX, XXXXXX, WINDOWS_PSWD
    ],


### LAYER 2 WINDOWS ###
    [LAYER_1_WIN, LAYER_2_WIN, LAYER_3_WIN, LAYER_4_WIN,
     send_string("LAYER 2 WINDOWS\n"), XXXXXX, XXXXXX, XXXXXX,
     XXXXXX, XXXXXX, XXXXXX, XXXXXX
    ],


### LAYER 3 WINDOWS ###
    [LAYER_1_WIN, LAYER_2_WIN, LAYER_3_WIN, LAYER_4_WIN,
     send_string("LAYER 3 WINDOWS\n"), XXXXXX, XXXXXX, XXXXXX,
     XXXXXX, XXXXXX, XXXXXX, XXXXXX
    ],


### LAYER 4 WINDOWS ###
    [LAYER_1_WIN, LAYER_2_WIN, LAYER_3_WIN, LAYER_4_WIN,
     KC.AUDIO_VOL_UP, KC.AUDIO_MUTE, XXXXXX, XXXXXX,
     KC.AUDIO_VOL_DOWN, KC.MEDIA_PREV_TRACK, KC.MEDIA_PLAY_PAUSE, KC.MEDIA_NEXT_TRACK
    ],


### LAYER 1.1 WINDOWS ###
    [LAYER_1_WIN, LAYER_2_WIN, LAYER_3_WIN, LAYER_4_WIN,
     send_string("LAYER 1.1 WINDOWS\n"), XXXXXX, XXXXXX, XXXXXX,
     XXXXXX, XXXXXX, XXXXXX, XXXXXX
    ],


### LAYER 2.1 LINUX ###
    [LAYER_1_WIN, LAYER_2_WIN, LAYER_3_WIN, LAYER_4_WIN,
     send_string("LAYER 2.1 WINDOWS\n"), XXXXXX, XXXXXX, XXXXXX,
     XXXXXX, XXXXXX, XXXXXX, XXXXXX
    ],


### LAYER 3.1 LINUX ###
    [LAYER_1_WIN, LAYER_2_WIN, LAYER_3_WIN, LAYER_4_WIN,
     send_string("LAYER 3.1 WINDOWS\n"), XXXXXX, XXXXXX, XXXXXX,
     XXXXXX, XXXXXX, XXXXXX, XXXXXX
    ],


### LAYER 4.1 LINUX ###
    [LAYER_1_WIN, LAYER_2_WIN, LAYER_3_WIN, LAYER_4_WIN,
     send_string("LAYER 4.1 WINDOWS\n"), XXXXXX, XXXXXX, XXXXXX,
     XXXXXX, XXXXXX, XXXXXX, XXXXXX
    ]
]



if __name__ == '__main__':
    keyboard.go()
