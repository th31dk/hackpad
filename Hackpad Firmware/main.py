import board

from kmk.kmk_keyboard import KMKKeyboard
from kmk.keys import KC
from kmk.modules.layers import Layers
from kmk.scanners import DiodeOrientation
from kmk.extensions.RGB import RGB
from kmk.extensions.display import Display, TextEntry
from kmk.extensions.display.ssd1306 import SSD1306
from kmk.modules.encoder import EncoderHandler
from kmk.extensions.media_keys import MediaKeys

keyboard = KMKKeyboard()
layers = Layers()
keyboard.modules.append(layers)

keyboard.col_pins = (board.GP26, board.GP28, board.GP27)
keyboard.row_pins = (board.GP2, board.GP3, board.GP4)
keyboard.diode_orientation = DiodeOrientation.COL2ROW

rgb = RGB(pixel_pin=board.GP1, num_pixels=16)
keyboard.extensions.append(rgb)

display = Display(
    display=SSD1306(sda=board.GP6, scl=board.GP7),
    entries=[
        TextEntry(text='hi!', x=0, y=0),
    ],
    height=32
)
keyboard.extensions.append(display)

media_keys = MediaKeys()
keyboard.extensions.append(media_keys)

encoder_handler = EncoderHandler()
encoder_handler.divisor = 2
encoder_handler.pins = ((board.GP0, board.GP29, None),)
encoder_handler.map = [
    ((KC.VOLD, KC.VOLU, KC.NO),),
]
keyboard.modules.append(encoder_handler)


# --- EMOJI KEYS (Discord Compatible) ---
EM1 = KC.MACRO(macro="😀")
EM2 = KC.MACRO(macro="🔥")
EM3 = KC.MACRO(macro="💀")
EM4 = KC.MACRO(macro="😂")
EM5 = KC.MACRO(macro="👍")
EM6 = KC.MACRO(macro="🌈")
EM7 = KC.MACRO(macro="❤️")
EM8 = KC.MACRO(macro="😎")
EM9 = KC.MACRO(macro="🤖")

# ---- KEYMAP ----
keyboard.keymap = [
    [
        EM1, EM2, EM3,
        EM4, EM5, EM6,
        EM7, EM8, EM9,
    ]
]

# ---- RUN ----
if __name__ == '__main__':
    keyboard.go()
