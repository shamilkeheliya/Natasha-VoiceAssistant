import os
import speak
import editables


def open_firefox():
    speak.speak('Opening Firefox')
    os.startfile(editables.firefox)


def open_android_studio():
    speak.speak('Opening Android Studio')
    os.startfile(editables.android_studio)


def open_telegram():
    speak.speak('Opening Telegram')
    os.startfile(editables.telegram)
