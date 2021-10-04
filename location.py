import webbrowser as web
import speak


def location(query):
    location = query.replace("where is","")
    speak.speak('Locating' + location)
    web.open_new_tab("https://www.google.com/maps/place/"+location)