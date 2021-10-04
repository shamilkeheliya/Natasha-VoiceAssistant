import time
import commands as cmd
import speak


def stopListening():
    speak.speak('For how long?')
    query = cmd.takeCommand()

    if 'minutes' in query:
        ans = int(query.replace('minutes', ''))
        speak.speak(f'Going sleeping for {ans} minutes')
        time.sleep(ans*60)

    elif 'minute' in query:
        ans = int(query.replace('minute', ''))
        speak.speak(f'Going sleeping for {ans} minute')
        time.sleep(ans*60)

    elif 'hours' in query:
        ans = int(query.replace('hours', ''))
        speak.speak(f'Going sleeping for {ans} hours')
        time.sleep(ans * 60 * 60)

    elif 'hour' in query:
        ans = int(query.replace('hour', ''))
        speak.speak(f'Going sleeping for {ans} hour')
        time.sleep(ans * 60 * 60)

    elif 'seconds' in query:
        ans = int(query.replace('seconds', ''))
        speak.speak(f'Going sleeping for {ans} seconds')
        time.sleep(ans)

    elif 'second' in query:
        ans = int(query.replace('second', ''))
        speak.speak(f'Going sleeping for {ans} second')
        time.sleep(ans)

    else:
        try:
            ans = int(query)
            speak.speak(f'Going sleeping for {ans} seconds')
            time.sleep(ans)
        except:
            speak.speak('Can\'t get it')
