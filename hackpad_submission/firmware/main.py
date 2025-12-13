import board
from kmk.kmk_keyboard import KMKKeyboard
from kmk.scanners.keypad import KeysScanner
from kmk.keys import KC
from kmk.modules.macros import Press, Release, Tap, Macros
from kmk.modules.encoder import EncoderHandler

keyboard = KMKKeyboard()

# --- 1. ROTARY ENCODER SETUP ---
encoder_handler = EncoderHandler()
keyboard.modules.append(encoder_handler)

# ⚠️ SOLDER CHECK: Connect your Encoder's Side Pins to D8 and D9
# The middle pin of the encoder usually goes to GND.
encoder_handler.pins = ((board.D8, board.D9, None, False),)

# What the knob does: Volume Up (Right) / Volume Down (Left)
encoder_handler.map = [ ((KC.VOLU, KC.VOLD),) ]


# --- 2. SWITCHES SETUP (Direct Wiring) ---
# This assumes you wired each switch to its own pin (1 leg to Pin, 1 leg to GND)
# PINS used: D0, D1, D2, D3, D6, D7
keyboard.matrix = KeysScanner(
    pins=[board.D0, board.D1, board.D2, board.D3, board.D6, board.D7],
    value_when_pressed=False,
)

# --- 3. KEYMAPPING ---
# Assigning basic keys. You can change 'KC.A' to whatever you want later!
keyboard.keymap = [
    [
        KC.A,    KC.B, 
        KC.C,    KC.D, 
        KC.E,    KC.F,
    ]
]

if __name__ == '__main__':
    keyboard.go()
