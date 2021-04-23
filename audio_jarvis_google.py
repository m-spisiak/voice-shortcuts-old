import speech_recognition as sr
import time
import pyautogui as pag

r = sr.Recognizer()

#keywords = [("copy", 1), ("paste", 1), ("snap",1), ("select all",1) ]
#keywords2 =  ["copy","paste","snap","select all"]

source = sr.Microphone(device_index=1)


def callback(recognizer, audio):

    try:
        speech = recognizer.recognize_google(audio)
        if "copy" in speech:
            copy()
        elif "paste" in speech:
            paste()
        elif "snap" in speech:
            snap()
        elif "select all" in speech:
            select_all()

    except sr.UnknownValueError:
        print("Oops! Didn't catch that")


def copy():
    print("copying")
    pag.keyDown("ctrl")
    pag.press("c")
    pag.keyUp("ctrl")

def paste():
    print("pasting")
    pag.keyDown("ctrl")
    pag.press("v")
    pag.keyUp("ctrl")

def snap():
    print("cutting")
    pag.keyDown("ctrl")
    pag.press("x")
    pag.keyUp("ctrl")

def select_all():
    print("selcting all")
    pag.keyDown("ctrl")
    pag.press("a")
    pag.keyUp("ctrl")

def start_recognizer():
    r.listen_in_background(source, callback)
    time.sleep(1000000)
    

start_recognizer()
