import webbrowser as web
import speak
import os
from colorama import Fore, Style
import editables


def open_google():
    speak.speak('Opening Google')
    os.startfile(editables.chrome)


def open_youtube():
    speak.speak('Opening YouTube')
    web.open('https://www.youtube.com')


def open_facebook():
    speak.speak('Opening FaceBook')
    web.open('https://www.facebook.com')


def open_whatsapp():
    speak.speak('Opening WhatsApp')
    web.open('https://web.whatsapp.com')


def search_google(query):
    query = query.replace('google', '')
    query = query.lower()

    print(Fore.LIGHTYELLOW_EX + 'Opening Google and search about ' + Fore.LIGHTBLUE_EX + query + Style.RESET_ALL)
    speak.speak_only(f'Opening google and search about {query}')

    web.open('https://www.google.com/search?q=' + query)


def search_youtube(query):
    query = query.replace('youtube', '')
    query = query.lower()

    print(Fore.LIGHTYELLOW_EX + 'Opening YouTube and search about ' + Fore.LIGHTBLUE_EX + query + Style.RESET_ALL)
    speak.speak_only(f'Opening YouTube and search about {query}')

    web.open('https://www.youtube.com/results?search_query=' + query)


def search_facebook(query):
    query = query.replace('facebook', '')
    query = query.lower()

    print(Fore.LIGHTYELLOW_EX + 'Opening FaceBook and search about ' + Fore.LIGHTBLUE_EX + query + Style.RESET_ALL)
    speak.speak_only(f'Opening FaceBook and search about {query}')

    web.open('https://www.facebook.com/search/?q=' + query)


