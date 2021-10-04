import speech_recognition
from colorama import Fore, Style


def takeCommand():
    r = speech_recognition.Recognizer()
    with speech_recognition.Microphone() as source:
        print(Fore.YELLOW + 'Listening....' + Style.RESET_ALL)
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print(Fore.YELLOW + 'Recognizing....' + Style.RESET_ALL)
        query = r.recognize_google(audio, language='en-UK')
        print(query)

    except Exception as ex:
        print(ex)
        print(Fore.YELLOW + 'Please tell again' + Style.RESET_ALL)
        return 'None'

    return query


def takeCommand_without_print():
    r = speech_recognition.Recognizer()
    with speech_recognition.Microphone() as source:
        print(Fore.YELLOW + 'Listening....' + Style.RESET_ALL)
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print(Fore.YELLOW + 'Recognizing....' + Style.RESET_ALL)
        query = r.recognize_google(audio, language='en-UK')

    except Exception as ex:
        print(ex)
        print(Fore.YELLOW + 'Please tell again' + Style.RESET_ALL)
        return 'None'

    return query
