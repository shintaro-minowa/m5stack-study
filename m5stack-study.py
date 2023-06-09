from m5stack import *
from m5ui import *
from uiflow import *
import time
import unit

setScreenColor(0x000000)
tof0 = unit.get(unit.TOF, unit.PORTA)

label0 = M5TextBox(85, 83, "Text", lcd.FONT_DejaVu72, 0x08feab, rotate=0)
label1 = M5TextBox(227, 174, "mm", lcd.FONT_DejaVu24, 0xFFFFFF, rotate=0)
label2 = M5TextBox(29, 31, "distance:", lcd.FONT_DejaVu24, 0xFFFFFF, rotate=0)

# C Major Scale
c_major_scale = [262, 294, 330, 349, 392, 440, 494, 523]

def play_scale(note):
    speaker.sing(note, 1/8)

while True:
    label0.setText(str(tof0.distance))
    distance = tof0.distance

    if distance < 1000:
        scale_index = int(distance / 125)
        play_scale(c_major_scale[scale_index])

    wait_ms(2)
