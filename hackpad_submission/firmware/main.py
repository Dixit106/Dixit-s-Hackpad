# You import all the IOs of your board
import board

# These are imports from the kmk library
from kmk.kmk_keyboard import KMKKeyboard
from kmk.scanners.keypad import KeysScanner
from kmk.keys import KC
from kmk.modules.macros import Press, Release, Tap, Macros

# This is the main instance of your keyboard
keyboard = KMKKeyboard()

# Add the macro extension
macros = Macros()
keyboard.modules.append(macros)

# Define your pins here!
# These match the pins you used in KiCad (D0, D1, D2, D3, D6, D7)
PINS = [board.D0, board.D1, board.D2, board.D3, board.D6, board.D7]

# Tell kmk we are not using a key matrix
keyboard.matrix = KeysScanner(
    pins=PINS,
    value_when_pressed=False,
)

# Here you define the buttons corresponding to the pins
# I added 6 keys here to match your 6 switches.
# You can change these later!
keyboard.keymap = [
    [
     KC.A,    KC.B, 
     KC.C,    KC.D, 
     KC.E,    KC.F
    ]
]

# Start kmk!
if __name__ == '__main__':
    keyboard.go()