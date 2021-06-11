"""CircuitPython Essentials NeoPixel example by Adafrut.multipass bystuartriggs5/28"""
import time
import board
import neopixel
import terminalio
import digitalio
import displayio
from adafruit_display_text import label
import adafruit_displayio_ssd1306
from audiocore import WaveFile

led = neopixel.NeoPixel(board.NEOPIXEL, 1)
led.brightness = 0.5

def mpup():
    led[0] = (255, 0, 0)
    time.sleep(1)
    led[0] = (0, 0, 0)

def mpdone():
    led[0] = (0, 255, 0)
    time.sleep(2)
    led[0] = (0, 0, 0)

try:
    from audioio import AudioOut
except ImportError:
    try:
        from audiopwmio import PWMAudioOut as AudioOut
    except ImportError:
        pass  # not always supported by every board!

button = digitalio.DigitalInOut(board.A1)
button.switch_to_input(pull=digitalio.Pull.UP)

wave_file = open("multipass3.wav", "rb")
wave = WaveFile(wave_file)
audio = AudioOut(board.A0)

displayio.release_displays()

# NeoPixels Section
pixel_pin = board.A3
num_pixels = 8
pixels = neopixel.NeoPixel(pixel_pin, num_pixels, brightness=0.10, auto_write=False)

# i2c Section for OLED Display
i2c = board.I2C()
display_bus = displayio.I2CDisplay(i2c, device_address=0x3C)
display = adafruit_displayio_ssd1306.SSD1306(display_bus, width=128, height=32)

# Make the display context for Fhloston Paradise Access
splash = displayio.Group(max_size=10)
display.show(splash)
inner_bitmap = displayio.Bitmap(118, 24, 1)


def oleddis():
    inner_palette = displayio.Palette(1)
    inner_palette[0] = 0x000000  # Black
    inner_sprite = displayio.TileGrid(
        inner_bitmap, pixel_shader=inner_palette, x=5, y=4
    )
    splash.append(inner_sprite)

    time.sleep(0.005)

    inner_palette = displayio.Palette(1)
    inner_palette[0] = 0x000000  # Black
    inner_sprite = displayio.TileGrid(
        inner_bitmap, pixel_shader=inner_palette, x=5, y=4
    )
    splash.append(inner_sprite)
    time.sleep(0.005)
    text = "V A C C I N E  "
    text_area = label.Label(terminalio.FONT, text=text, color=0xFFFF00, x=15, y=15)
    splash.append(text_area)
    time.sleep(1)

    color_palette = displayio.Palette(1)
    color_palette[0] = 0xFFFFFF  # White

    time.sleep(0.005)

    inner_palette = displayio.Palette(1)
    inner_palette[0] = 0x000000  # Black
    inner_sprite = displayio.TileGrid(
        inner_bitmap, pixel_shader=inner_palette, x=5, y=4
    )
    splash.append(inner_sprite)

    #  Text Setup for OLED Display for 1 Time Cycle
    text = "C H E C K I N G ..."
    text_area = label.Label(terminalio.FONT, text=text, color=0xFFFF00, x=15, y=15)
    splash.append(text_area)

    color_palette = displayio.Palette(1)
    color_palette[0] = 0xFFFFFF  # White

    time.sleep(0.2)

def passdone():
    inner_palette = displayio.Palette(1)
    inner_palette[0] = 0x000000  # Black
    inner_sprite = displayio.TileGrid(
        inner_bitmap, pixel_shader=inner_palette, x=5, y=4
    )
    splash.append(inner_sprite)
    time.sleep(0.005)
    text = "C O M P L E T E !!!  "
    text_area = label.Label(terminalio.FONT, text=text, color=0xFFFF00, x=15, y=15)
    splash.append(text_area)
    time.sleep(1)

    color_palette = displayio.Palette(1)
    color_palette[0] = 0xFFFFFF  # White

    time.sleep(0.5)

def wheel(pos):
    # Input a value 0 to 255 to get a color value.
    # The colours are a transition r - g - b - back to r.
    if pos < 0 or pos > 255:
        return (0, 0, 0)
    if pos < 85:
        return (255 - pos * 3, pos * 3, 0)
    if pos < 170:
        pos -= 85
        return (0, 255 - pos * 3, pos * 3)
    pos -= 170
    return (pos * 3, 0, 255 - pos * 3)

def rainbow_cycle(wait):
    for j in range(255):
        for i in range(num_pixels):
            rc_index = (i * 256 // num_pixels) + j
            pixels[i] = wheel(rc_index & 255)
        pixels.show()
        time.sleep(wait)

# NeoPixel Pattern
def color_chase(color, wait):  # wait
    for i in range(num_pixels):
        pixels[i] = color
        time.sleep(wait)
        pixels.show()
    time.sleep(0.000001)

# NeoPixel Color Selection
TURNBLUE = (0, 0, 255)
TURNOFF = (0, 0, 0)
TURNGREEN = (0, 255, 0)
TURNRED = (255, 0, 0)
TURNYELLOW = (255, 255, 0)

def pixelsplay():
    pixels.fill(TURNYELLOW)
    pixels.show()
    time.sleep(1)
    pixels.fill(TURNGREEN)
    pixels.show()
    time.sleep(1)
    pixels.fill(TURNOFF)
    pixels.show()

def newpix3():
    # color_chase(TURNGREEN, 0.21)  # Increase the number to slow down the color chase
    # color_chase(TURNBLUE, 0.1252)
    # pixels.fill(TURNOFF)
    # pixels.show()
    # time.sleep(0.02)
    color_chase(TURNGREEN, 0.15)  # Increase the number to slow down the color chase
    color_chase(TURNYELLOW, 0.15)
    pixels.fill(TURNOFF)
    pixels.show()
    # time.sleep(0.02)

# Main Loop
while True:
    mpup()
    audio.play(wave)
    # This allows you to do other things while the audio plays!
    t = time.monotonic()
    while time.monotonic() - t < 4:
        pass
    oleddis()
    pixelsplay()
    #  newpix3()
    passdone()
    mpdone()
    audio.pause()
    print("Waiting for button press to continue!")
    while button.value:
        pass
    audio.resume()
    while audio.playing:
        pass
    oleddis()  # print("Done!")
    # gettext()
#    rainbow_cycle(TURNGREEN, 0.1)  # Increase the number to slow down the color chase
#    color_chase(TURNBLUE, 0.1)
    # pixels.show()
