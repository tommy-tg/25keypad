import supervisor
import board
import storage
import usb_cdc

from digitalio import DigitalInOut, Direction, Pull

#supervisor.set_next_stack_limit(4096 + 4096)

row = DigitalInOut(board.GP2)
col = DigitalInOut(board.GP25)

row.direction = Direction.INPUT
col.direction = Direction.OUTPUT

row.pull = Pull.DOWN
col.value = True

if not row.value:
    storage.disable_usb_drive()
    usb_cdc.disable()
