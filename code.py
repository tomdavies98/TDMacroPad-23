import time
import digitalio
import usb_hid
from adafruit_hid.keyboard import Keyboard
from adafruit_hid.keycode import Keycode
from adafruit_display_text import label
import board
import busio
import displayio
import terminalio
import adafruit_displayio_sh1106
import rotaryio
import time
from board import *
import board
from adafruit_hid.consumer_control import ConsumerControl
from adafruit_hid.consumer_control_code import ConsumerControlCode

# Encoder setup
Enc = rotaryio.IncrementalEncoder(board.GP17, board.GP16, divisor=8)
Last_position = 0

displayio.release_displays()
sda, scl = board.GP0, board.GP1

i2c = busio.I2C(scl, sda)
display_bus = displayio.I2CDisplay(i2c, device_address=0x3C)

WIDTH = 128
HEIGHT = 64
BORDER = 5
display = adafruit_displayio_sh1106.SH1106(display_bus, width=WIDTH, height=HEIGHT)

splash = displayio.Group()
display.show(splash)
CurrentScreenMsg = ""
color_bitmap = displayio.Bitmap(WIDTH, HEIGHT, 1)
color_palette = displayio.Palette(1)
color_palette[0] = 0xFFFFFF  # White

bg_sprite = displayio.TileGrid(color_bitmap, pixel_shader=color_palette, x=0, y=0)
splash.append(bg_sprite)

inner_bitmap = displayio.Bitmap(WIDTH - BORDER * 2, HEIGHT - BORDER * 2, 1)
inner_palette = displayio.Palette(1)
inner_palette[0] = 0x000000  # Black
inner_sprite = displayio.TileGrid(inner_bitmap, pixel_shader=inner_palette, x=BORDER, y=BORDER)
splash.append(inner_sprite)

text = ""
text_area = label.Label(terminalio.FONT, text=text, color=0xFFFFFF, x=14, y=HEIGHT // 2 - 1)

splash.append(text_area)

def SendKeysPress(keys):
    global keyboard
    #Additional delays below allow macro to work over remote desktop

    for key in keys:
        keyboard.press(key)
        time.sleep(0.1)

    for key in keys:
        keyboard.release(key)
        time.sleep(0.1)

def UpdateScreen():
    global text
    global text_area
    global splash

    text = CurrentScreenMsg
    text_area.text = text

Profiles = ["General", "Rider-IDE", "Discord"]
CurrentProfile = 0
InfoOnly = False

Button1 = "btn1"
Button2 = "btn2"
Button3 = "btn3"
Button4 = "btn4"
Button5 = "btn5"
Button6 = "btn6"
Button7 = "btn7"
Button8 = "btn8"
Button9 = "btn9"
Button10 = "btn10"
Button11 = "btn11"
Button12 = "btn12"

profile_swap_pin = board.GP15
btn1_pin = board.GP14
btn2_pin = board.GP13
btn3_pin = board.GP12
btn4_pin = board.GP11
btn5_pin = board.GP10
btn6_pin = board.GP9
btn7_pin = board.GP8
btn8_pin = board.GP7
btn9_pin = board.GP6
btn10_pin = board.GP5
btn11_pin = board.GP4
btn12_pin = board.GP18

keyboard = Keyboard(usb_hid.devices)

#Volume control consumer
consumer = ConsumerControl(usb_hid.devices)

profile_swap_btn = digitalio.DigitalInOut(profile_swap_pin)
profile_swap_btn.direction = digitalio.Direction.INPUT
profile_swap_btn.pull = digitalio.Pull.DOWN

btn1_btn = digitalio.DigitalInOut(btn1_pin)
btn1_btn.direction = digitalio.Direction.INPUT
btn1_btn.pull = digitalio.Pull.DOWN

btn2_btn = digitalio.DigitalInOut(btn2_pin)
btn2_btn.direction = digitalio.Direction.INPUT
btn2_btn.pull = digitalio.Pull.DOWN

btn3_btn = digitalio.DigitalInOut(btn3_pin)
btn3_btn.direction = digitalio.Direction.INPUT
btn3_btn.pull = digitalio.Pull.DOWN

btn4_btn = digitalio.DigitalInOut(btn4_pin)
btn4_btn.direction = digitalio.Direction.INPUT
btn4_btn.pull = digitalio.Pull.DOWN

btn5_btn = digitalio.DigitalInOut(btn5_pin)
btn5_btn.direction = digitalio.Direction.INPUT
btn5_btn.pull = digitalio.Pull.DOWN

btn6_btn = digitalio.DigitalInOut(btn6_pin)
btn6_btn.direction = digitalio.Direction.INPUT
btn6_btn.pull = digitalio.Pull.DOWN

btn7_btn = digitalio.DigitalInOut(btn7_pin)
btn7_btn.direction = digitalio.Direction.INPUT
btn7_btn.pull = digitalio.Pull.DOWN

btn8_btn = digitalio.DigitalInOut(btn8_pin)
btn8_btn.direction = digitalio.Direction.INPUT
btn8_btn.pull = digitalio.Pull.DOWN

btn9_btn = digitalio.DigitalInOut(btn9_pin)
btn9_btn.direction = digitalio.Direction.INPUT
btn9_btn.pull = digitalio.Pull.DOWN

btn10_btn = digitalio.DigitalInOut(btn10_pin)
btn10_btn.direction = digitalio.Direction.INPUT
btn10_btn.pull = digitalio.Pull.DOWN

btn11_btn = digitalio.DigitalInOut(btn11_pin)
btn11_btn.direction = digitalio.Direction.INPUT
btn11_btn.pull = digitalio.Pull.DOWN

btn12_btn = digitalio.DigitalInOut(btn12_pin)
btn12_btn.direction = digitalio.Direction.INPUT
btn12_btn.pull = digitalio.Pull.DOWN

def UpdateCurrentScreenMessage(newMsg):
    global CurrentScreenMsg

    CurrentScreenMsg = newMsg

def GetPreviousProfile(currentProfilePos):
    global Profiles

    length_Profiles = len(Profiles)-1
    newPos = currentProfilePos -1

    if(newPos < 0):
        newPos = length_Profiles

    return newPos

def GetNextProfile(currentProfilePos):
    global Profiles

    length_Profiles = len(Profiles)-1
    newPos = currentProfilePos + 1

    if(newPos > length_Profiles):
        newPos = 0

    return newPos

def GeneralProfileShortcuts(buttonToPress, infoOnly):
    global Button1
    global Button2
    global Button3
    global Button4
    global btn1_btn
    global btn2_btn
    global btn3_btn
    global btn4_btn
    global btn5_btn
    global btn6_btn
    global btn7_btn
    global btn8_btn
    global btn9_btn
    global btn10_btn
    global btn11_btn
    global btn12_btn
    global text
    global CurrentScreenMsg

    if buttonToPress == Button2:
        UpdateCurrentScreenMessage("COPY")
        if infoOnly:
            return

        SendKeysPress([Keycode.LEFT_CONTROL, Keycode.C])
    elif buttonToPress == Button3:
        UpdateCurrentScreenMessage("PASTE")
        if infoOnly:
            return

        SendKeysPress([Keycode.LEFT_CONTROL, Keycode.V])

    elif buttonToPress == Button4:
        UpdateCurrentScreenMessage("SEARCH")
        if infoOnly:
            return
        SendKeysPress([Keycode.LEFT_CONTROL, Keycode.F])
    elif buttonToPress == Button5:
        UpdateCurrentScreenMessage("TAB-OUT")
        if infoOnly:
            return
        SendKeysPress([Keycode.ALT, Keycode.TAB])
    elif buttonToPress == Button6:
        UpdateCurrentScreenMessage("LOCK-PC")
        if infoOnly:
            return
        SendKeysPress([Keycode.WINDOWS, Keycode.L])
    elif buttonToPress == Button7:
        UpdateCurrentScreenMessage("SELECT-ALL")
        if infoOnly:
            return
        SendKeysPress([Keycode.LEFT_CONTROL, Keycode.A])
    elif buttonToPress == Button8:
        UpdateCurrentScreenMessage("UNDO")
        if infoOnly:
            return
        SendKeysPress([Keycode.LEFT_CONTROL, Keycode.Z])
    elif buttonToPress == Button9:
        UpdateCurrentScreenMessage("REDO")
        if infoOnly:
            return
        SendKeysPress([Keycode.LEFT_CONTROL, Keycode.Y])
    elif buttonToPress == Button10:
        UpdateCurrentScreenMessage("SCREENSHOT")
        if infoOnly:
            return
        SendKeysPress([Keycode.WINDOWS, Keycode.LEFT_SHIFT, Keycode.S])
    elif buttonToPress == Button11:
        UpdateCurrentScreenMessage("TASK-MANAGER")
        if infoOnly:
            return
        SendKeysPress([Keycode.LEFT_CONTROL, Keycode.LEFT_SHIFT, Keycode.ESCAPE])
    elif buttonToPress == Button12:
        UpdateCurrentScreenMessage("MINIMIZE-ALL")
        if infoOnly:
            return
        SendKeysPress([Keycode.WINDOWS, Keycode.M])

def CodingProfileShortcuts(buttonToPress, infoOnly):
    global Button1
    global Button2
    global Button3
    global Button4
    global btn1_btn
    global btn2_btn
    global btn3_btn
    global btn4_btn
    global btn5_btn
    global btn6_btn
    global btn7_btn
    global btn8_btn
    global btn9_btn
    global btn10_btn
    global btn11_btn
    global btn12_btn
    global text
    global CurrentScreenMsg

    if buttonToPress == Button2:
        UpdateCurrentScreenMessage("DUPLICATE")
        print("DUPLICATE")
        if infoOnly:
            return
        SendKeysPress([Keycode.LEFT_CONTROL, Keycode.D])
    elif buttonToPress == Button3:
        UpdateCurrentScreenMessage("COMMENT")
        if infoOnly:
            return
        SendKeysPress([Keycode.LEFT_CONTROL, Keycode.LEFT_SHIFT, Keycode.FORWARD_SLASH])
    elif buttonToPress == Button4:
        UpdateCurrentScreenMessage("DEBUG")
        if infoOnly:
            return
        SendKeysPress([Keycode.ALT, Keycode.F5])
    elif buttonToPress == Button5:
        UpdateCurrentScreenMessage("USAGES")
        if infoOnly:
            return
        SendKeysPress([Keycode.LEFT_SHIFT, Keycode.F12])
    elif buttonToPress == Button6:
        UpdateCurrentScreenMessage("BREAKPOINTS")
        if infoOnly:
            return
        SendKeysPress([Keycode.LEFT_CONTROL, Keycode.ALT, Keycode.B])
    elif buttonToPress == Button7:
        UpdateCurrentScreenMessage("TODO")
        if infoOnly:
            return
        SendKeysPress([Keycode.LEFT_CONTROL, Keycode.ALT, Keycode.D])
    elif buttonToPress == Button8:
        UpdateCurrentScreenMessage("FIND-FILE")
        if infoOnly:
            return
        SendKeysPress([Keycode.LEFT_CONTROL, Keycode.LEFT_SHIFT, Keycode.T])
    elif buttonToPress == Button9:
        UpdateCurrentScreenMessage("UNDO")
        if infoOnly:
            return

        SendKeysPress([Keycode.LEFT_CONTROL, Keycode.Z])
    elif buttonToPress == Button10:
        UpdateCurrentScreenMessage("REDO")
        if infoOnly:
            return

        SendKeysPress([Keycode.LEFT_CONTROL, Keycode.Y])
    elif buttonToPress == Button11:
        UpdateCurrentScreenMessage("Minimize All")
        if infoOnly:
            return

        SendKeysPress([Keycode.WINDOWS, Keycode.M])

def DiscordProfileShortcuts(buttonToPress, infoOnly):
    global Button1
    global Button2
    global Button3
    global Button4
    global btn1_btn
    global btn2_btn
    global btn3_btn
    global btn4_btn
    global btn5_btn
    global btn6_btn
    global btn7_btn
    global btn8_btn
    global btn9_btn
    global btn10_btn
    global btn11_btn
    global btn12_btn
    global text
    global CurrentScreenMsg

    if buttonToPress == Button2:
        UpdateCurrentScreenMessage("MUTE")
        if infoOnly:
            return
        SendKeysPress([Keycode.LEFT_CONTROL, Keycode.LEFT_SHIFT, Keycode.M])
    elif buttonToPress == Button3:
        UpdateCurrentScreenMessage("DEAFEN")
        if infoOnly:
            return
        SendKeysPress([Keycode.LEFT_CONTROL, Keycode.LEFT_SHIFT, Keycode.D])
    elif buttonToPress == Button4:
        UpdateCurrentScreenMessage("GIF-PICKER")
        if infoOnly:
            return
        SendKeysPress([Keycode.LEFT_CONTROL, Keycode.G])
    elif buttonToPress == Button5:
        UpdateCurrentScreenMessage("SEARCH")
        if infoOnly:
            return
        SendKeysPress([Keycode.LEFT_SHIFT, Keycode.F])
    elif buttonToPress == Button6:
        UpdateCurrentScreenMessage("UPLOAD")
        if infoOnly:
            return
        SendKeysPress([Keycode.LEFT_CONTROL, Keycode.LEFT_SHIFT, Keycode.U])
    elif buttonToPress == Button7:
        UpdateCurrentScreenMessage("INBOX")
        if infoOnly:
            return
        SendKeysPress([Keycode.LEFT_CONTROL, Keycode.I])
    elif buttonToPress == Button8:
        UpdateCurrentScreenMessage("SCROLL-UP")
        if infoOnly:
            return
        SendKeysPress([Keycode.PAGE_UP])
    elif buttonToPress == Button9:
        UpdateCurrentScreenMessage("SCROLL-DOWN")
        if infoOnly:
            return

        SendKeysPress([Keycode.PAGE_DOWN])
    elif buttonToPress == Button10:
        UpdateCurrentScreenMessage("MARK-READ")
        if infoOnly:
            return

        SendKeysPress([Keycode.LEFT_SHIFT, Keycode.ESCAPE])
    elif buttonToPress == Button11:
        UpdateCurrentScreenMessage("JUMP-UNREAD")
        if infoOnly:
            return

        SendKeysPress([Keycode.LEFT_SHIFT, Keycode.PAGE_UP])

def PressProfileSpecificButton(buttonToPress, infoOnly):
    global InfoOnly
    currentProfile = Profiles[CurrentProfile]
    if currentProfile == "General":
        GeneralProfileShortcuts(buttonToPress, infoOnly)
    elif currentProfile == "Discord":
        DiscordProfileShortcuts(buttonToPress, infoOnly)
    elif currentProfile == "Rider-IDE":
        CodingProfileShortcuts(buttonToPress, infoOnly)

    InfoOnly = False

while True:
    CurrentScreenMsg = Profiles[CurrentProfile]

    if btn1_btn.value:
        InfoOnly = True

    current_position = Enc.position
    position_change = current_position - Last_position
    if position_change > 0:
        consumer.send(ConsumerControlCode.VOLUME_INCREMENT)
        consumer.send(ConsumerControlCode.VOLUME_INCREMENT)
        consumer.send(ConsumerControlCode.VOLUME_INCREMENT)
        consumer.send(ConsumerControlCode.VOLUME_INCREMENT)
        consumer.send(ConsumerControlCode.VOLUME_INCREMENT)
    elif position_change < 0:
        consumer.send(ConsumerControlCode.VOLUME_DECREMENT)
        consumer.send(ConsumerControlCode.VOLUME_DECREMENT)
        consumer.send(ConsumerControlCode.VOLUME_DECREMENT)
        consumer.send(ConsumerControlCode.VOLUME_DECREMENT)
        consumer.send(ConsumerControlCode.VOLUME_DECREMENT)
    Last_position = current_position

    if profile_swap_btn.value:
        CurrentProfile = GetNextProfile(CurrentProfile)
        CurrentScreenMsg = Profiles[CurrentProfile]
        time.sleep(0.1)
    elif btn2_btn.value:
        PressProfileSpecificButton(Button2, InfoOnly)
        time.sleep(0.1)
    elif btn3_btn.value:
        PressProfileSpecificButton(Button3, InfoOnly)
        time.sleep(0.1)
    elif btn4_btn.value:
        PressProfileSpecificButton(Button4, InfoOnly)
        time.sleep(0.1)
    elif btn5_btn.value:
        PressProfileSpecificButton(Button5, InfoOnly)
        time.sleep(0.1)
    elif btn6_btn.value:
        PressProfileSpecificButton(Button6, InfoOnly)
        time.sleep(0.1)
    elif btn7_btn.value:
        PressProfileSpecificButton(Button7, InfoOnly)
        time.sleep(0.1)
    elif btn8_btn.value:
        PressProfileSpecificButton(Button8, InfoOnly)
        time.sleep(0.1)
    elif btn9_btn.value:
        PressProfileSpecificButton(Button9, InfoOnly)
    elif btn10_btn.value:
        PressProfileSpecificButton(Button10, InfoOnly)
        time.sleep(0.1)
    elif btn11_btn.value:
        PressProfileSpecificButton(Button11, InfoOnly)
        time.sleep(0.1)
    elif btn12_btn.value:
        PressProfileSpecificButton(Button12, InfoOnly)
        time.sleep(0.1)
    time.sleep(0.1)
    UpdateScreen()
