import os
import speak
import datetime as dt
import commands as cmd
from colorama import Fore, Style


# Time
def tell_time():
    time = dt.datetime.now().strftime("%H:%M:%S")
    print(Fore.GREEN + dt.datetime.now().strftime("%H:%M") + Style.RESET_ALL)
    speak.speak_only(time)


# Date
def tell_date():
    date = dt.datetime.now().date()
    speak.speak(date)


# Greeting
def greeting(name, real_name):
    hour = dt.datetime.now().hour

    if hour < 4:
        print(Fore.GREEN + f'Hello {real_name}' + Style.RESET_ALL)
        speak.speak_only(f'Hello {name}')
    elif hour < 12:
        print(Fore.GREEN + f'Good Morning {real_name}' + Style.RESET_ALL)
        speak.speak_only(f'Good Morning {name}')
    elif hour < 16:
        print(Fore.GREEN + f'Good Afternoon {real_name}' + Style.RESET_ALL)
        speak.speak_only(f'Good Afternoon {name}')
    else:
        print(Fore.GREEN + f'Good Evening {real_name}' + Style.RESET_ALL)
        speak.speak_only(f'Good Evening {name}')

    speak.speak('How can I help you?')


# Go offline
def go_offline(name, real_name):
    print(Fore.GREEN + f'Good bye {real_name}, Have a nice day!' + Style.RESET_ALL)
    speak.speak_only(f'Good bye {name}, Have a nice day!')
    quit()


# Shutdown Computer
def shutdown():
    speak.speak('Do you want to shutdown your computer?')
    answer = cmd.takeCommand().lower()

    if 'yes' in answer or 'sure' in answer:
        speak.speak('Shutting down computer!')
        os.system("shutdown /s /t 1")


# Restart Computer
def restart():
    speak.speak('Do you want to restart your computer?')
    answer = cmd.takeCommand().lower()

    if 'yes' in answer or 'sure' in answer:
        speak.speak('Restarting computer!')
        os.system("shutdown /r /t 1")


def logout():
    os.system("shutdown -1")