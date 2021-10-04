import pyttsx3
from colorama import Fore, Style
import editables

engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[editables.gender].id)

rate = engine.getProperty('rate')
engine.setProperty('rate', editables.rate)


def speak(audio):
    print(Fore.GREEN + str(audio) + Style.RESET_ALL)
    engine.say(audio)
    engine.runAndWait()


def speak_only(audio):
    engine.say(audio)
    engine.runAndWait()