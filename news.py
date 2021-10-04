import json
from urllib.request import urlopen
import editables
import speak


def news():
    try:
        jsonObj = urlopen(f"https://newsapi.org/v2/top-headlines?country=us&category=business&apiKey={editables.newsAPIkey}")
        data = json.load(jsonObj)

        for item in data['articles']:
            speak.speak(item['title'])

    except:
        speak.speak('I can\'t search news at the moment')