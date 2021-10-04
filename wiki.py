import wikipedia
import speak
from colorama import Fore, Style


def wikipedia_search(query, name, real_name):
    query = query.replace('wikipedia', '')
    print(Fore.LIGHTYELLOW_EX + 'Searching about ' + Fore.LIGHTBLUE_EX + query + Style.RESET_ALL)
    speak.speak_only(f'Searching about {query} on Wikipedia')

    try:
        result = wikipedia.summary(query, sentences=3)
        speak.speak(f'According to the Wikipedia, {result}')
    except:
        print(Fore.GREEN + f'Sorry {real_name}, I can\'t find anything about {query} in Wikipedia' + Style.RESET_ALL)
        speak.speak_only(f'Sorry {name}, I can\'t find anything about {query} in Wikipedia')
