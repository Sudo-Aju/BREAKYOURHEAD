import board
import busio
import time
import displayio
import terminalio
import random
import adafruit_displayio_ssd1306
from adafruit_display_text import label

from kmk.kmk_keyboard import KMKKeyboard
from kmk.keys import KC
from kmk.scanners import DiodeOrientation
from kmk.modules.encoder import EncoderHandler
from kmk.extensions import Extension
from kmk.extensions.media_keys import MediaKeys

class StopwatchScreen(Extension):
    def __init__(self):

        self.start_time = time.monotonic()

        self.screen_ok = False
        self.stars = []
        try:
            displayio.release_displays()
            self.i2c = busio.I2C(board.D5, board.D4)
            self.display_bus = displayio.I2CDisplay(self.i2c, device_address=0x3C)
            self.display = adafruit_displayio_ssd1306.SSD1306(
                self.display_bus, width=128, height=64)
            
            self.group = displayio.Group()
            
            for i in range(15):
                star = label.Label(terminalio.FONT, text=".", color=0xFFFFFF)
                star.x = random.randint(0, 128)
                star.y = random.randint(0, 64)
                self.stars.append(star)
                self.group.append(star)


            self.header = label.Label(terminalio.FONT, text="SESSION TIME", color=0xFFFFFF, x=30, y=10)
            self.timer_label = label.Label(terminalio.FONT, text="00:00", color=0xFFFFFF, x=25, y=35, scale=3)
            
            self.group.append(self.header)
            self.group.append(self.timer_label)
            self.display.root_group = self.group
            self.screen_ok = True
        except:
            self.screen_ok = False

    def on_runtime_enable(self, keyboard): return
    def on_runtime_disable(self, keyboard): return
    def during_bootup(self, keyboard): return
    def before_matrix_scan(self, keyboard): return
    
    def after_matrix_scan(self, keyboard):
        if not self.screen_ok: return
        
        if random.random() > 0.8:
            star = random.choice(self.stars)
            star.x = (star.x - 1) % 128
            star.y = (star.y + random.randint(-1, 1)) % 64

        elapsed = time.monotonic() - self.start_time
        

        minutes = int(elapsed // 60)
        seconds = int(elapsed % 60)
        time_str = "{:02d}:{:02d}".format(minutes, seconds)
        
        try:
            self.timer_label.text = time_str
        except: pass
        return


keyboard = KMKKeyboard()
keyboard.extensions.append(MediaKeys())
keyboard.extensions.append(StopwatchScreen())

keyboard.row_pins = (board.D6, board.D7)
keyboard.col_pins = (board.D8, board.D9, board.D10)
keyboard.diode_orientation = DiodeOrientation.COL2ROW

encoder_handler = EncoderHandler()
encoder_handler.pins = ((board.D0, board.D1, None, False), (board.D2, board.D3, None, False))
keyboard.modules.append(encoder_handler)



keyboard.keymap = [[KC.LGUI(KC.C), KC.LGUI(KC.V), KC.LGUI(KC.LBRC), KC.LGUI(KC.Z), KC.LGUI(KC.LSFT(KC.Z)), KC.LGUI(KC.RBRC)]]

encoder_handler.map = [[(KC.PGUP, KC.PGDN), (KC.LGUI(KC.MINUS), KC.LGUI(KC.EQUAL))]]

if __name__ == '__main__':
    keyboard.go()
