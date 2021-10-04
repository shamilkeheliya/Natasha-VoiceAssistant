import stop_listening
import whatsapp
import wolframalphaFunctions
import location
import news
import remember
import about_natasha
import basic
import chrome
import commands as cmd
import cpu
import notes
import screenshot
import songs
import wiki
import speak
import applications as app
import editables

name = editables.name
real_name = editables.real_name
real_password = editables.real_password
notLogged = True
password_count = 0


if __name__ == "__main__":

    # Password
    """speak.speak('Hello, Please tell me the password?')
    while notLogged:
        password_count = password_count + 1
        password = cmd.takeCommand_without_print().lower()

        if password == real_password:
            notLogged = False
        elif password_count >= 5:
            speak.speak('Going offline')
            quit()
        elif password == 'none':
            speak.speak('Please tell me the password?')
        elif 'bye bye' in password:
            speak.speak('Going offline')
            quit()
        elif 'go offline' in password:
            speak.speak('Going offline')
            quit()
        else:
            speak.speak('Wrong Password, Please try again....') """

    # Main
    basic.greeting(name, real_name)
    while True:
        query = cmd.takeCommand().lower()

        # Date
        if 'date' in query:
            basic.tell_date()

        # Time
        elif 'time' in query:
            basic.tell_time()

        # Welcome
        elif 'thanks' in query:
            speak.speak('Pleasure to help you')
        elif 'thank you' in query:
            speak.speak('Pleasure to help you')

        # Go offline
        elif 'bye bye' in query:
            basic.go_offline(name, real_name)
        elif 'go offline' in query:
            basic.go_offline(name, real_name)

        # Shutdown Computer
        elif 'shutdown' in query:
            basic.shutdown()
        elif 'turn off computer' in query:
            basic.shutdown()
        elif 'turn off my computer' in query:
            basic.shutdown()
        elif 'turn off the computer' in query:
            basic.shutdown()

        # Restart Computer
        elif 'restart' in query:
            basic.restart()
        elif 'reboot' in query:
            basic.restart()

        # Logout
        elif 'logout' in query:
            basic.logout()
        elif 'sign out' in query:
            basic.logout()
        elif 'log out' in query:
            basic.logout()

        # Name
        elif 'what is your name' in query:
            about_natasha.say_name()
        elif 'what\'s your name' in query:
            about_natasha.say_name()
        elif 'your name' in query:
            about_natasha.say_name()

        # Introduce
        elif 'introduce' in query:
            about_natasha.introduce()
        elif 'who are you' in query:
            about_natasha.introduce()
        elif 'tell me about you' in query:
            about_natasha.introduce()
        elif 'yourself' in query:
            about_natasha.introduce()

        # Wikipedia
        elif 'wikipedia' in query:
            wiki.wikipedia_search(query, name, real_name)

        # Open Chrome
        elif 'open google' in query:
            chrome.open_google()
        elif 'open chrome' in query:
            chrome.open_google()

        # Search Google
        elif 'google' in query:
            chrome.search_google(query)

        # Open Youtube
        elif 'open youtube' in query:
            chrome.open_youtube()

        # Search Youtube
        elif 'youtube' in query:
            chrome.search_youtube(query)

        # Search Youtube
        elif 'open whatsapp' in query:
            chrome.open_whatsapp()

        # Open FaceBook
        elif 'open facebook' in query:
            chrome.open_facebook()
        elif 'open fb' in query:
            chrome.open_facebook()

        # Search FaceBook
        elif 'facebook' in query:
            chrome.search_facebook(query)
        elif 'fb' in query:
            chrome.search_facebook(query)

        # CPU
        elif 'cpu' in query:
            cpu.cpu_battery()

        # Open Firefox
        elif 'open firefox' in query:
            app.open_firefox()

        # Open Android Studio
        elif 'open android studio' in query:
            app.open_android_studio()

        # Open Telegram
        elif 'open telegram' in query:
            app.open_telegram()
        elif 'open tg' in query:
            app.open_telegram()

        # Take Note
        elif 'note' in query:
            notes.write_note()

        # Tell Story
        elif 'story' in query:
            notes.read_note()

        # Screenshot
        elif 'screenshot' in query:
            screenshot.screenshot()
        elif 'take a ss' in query:
            screenshot.screenshot()
        elif 'take ss' in query:
            screenshot.screenshot()
        elif 'get ss' in query:
            screenshot.screenshot()
        elif 'get a ss' in query:
            screenshot.screenshot()

        # Sinahala Song
        elif 'sinhala song' in query:
            songs.play_sinhala_song()
        elif 'sinhala songs' in query:
            songs.play_sinhala_song()

        # Sinahala Song
        elif 'english song' in query:
            songs.play_english_song()
        elif 'english songs' in query:
            songs.play_english_song()

        # Play Song
        elif 'song' in query:
            songs.play_song()
        elif 'songs' in query:
            songs.play_song()

        # Read Remember
        elif 'read remember' in query:
            remember.read_remember()
        elif 'what do you remember' in query:
            remember.read_remember()
        elif 'do you remember' in query:
            remember.read_remember()

        # Remember
        elif 'remember' in query:
            remember.remember()

        # News
        elif 'news' in query:
            news.news()

        # Location
        elif 'where is' in query:
            location.location(query)

        # Calculator
        elif 'calculate' in query:
            wolframalphaFunctions.calculate(query)

        # Explain
        elif 'what is' in query:
            wolframalphaFunctions.explain(query)
        elif 'who is' in query:
            wolframalphaFunctions.explain(query)

        # Sleep
        elif 'stop listening' in query:
            stop_listening.stopListening()
        elif 'stop listen' in query:
            stop_listening.stopListening()
        elif 'sleep' in query:
            stop_listening.stopListening()

        # Send WhatsApp Message
        elif 'whatsapp' in query:
            whatsapp.sendwhatsapp()

        # Natasha (Should be last One)
        elif 'hello natasha' in query:
            basic.greeting(name, real_name)
        elif 'natasha' in query:
            about_natasha.natasha()
