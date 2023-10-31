import time
import pyautogui
import screen_brightness_control as sbc
from delay import *

@delay(1)
def PlayPause():
    pyautogui.press("space")

@delay(0.5)
def Forward():
    pyautogui.hotkey("alt","right")

@delay(0.5)
def Backward():
    pyautogui.hotkey("alt","left")

@delay(1)
def FullScreen():
    pyautogui.press("f")

@delay(2)
def ExitFullScreen():
    pyautogui.press("esc")

#@delay(2)
def VolumeUp():
    pyautogui.hotkey("ctrl","up")

#@delay(2)
def VolumeDown():
    pyautogui.hotkey("ctrl","down")

@delay(1)
def mute():
    pyautogui.press("m")

#@delay(1)
def BrightnessUp():
    sbc.set_brightness("+10")

#@delay(1)
def BrightnessDown():
    sbc.set_brightness("-10")

