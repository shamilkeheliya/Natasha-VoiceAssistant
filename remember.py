import editables
import speak
import commands as cmd

def remember():
    speak.speak('What should I remember?')
    answer = cmd.takeCommand().lower()
    file_name = editables.remember + '/remember.txt'
    file = open(file_name, 'w')
    file.write(answer)
    speak.speak('Okay, I\'ll remember it')
    file.close()


def read_remember():
    file_name = editables.remember + '/remember.txt'
    file = open(file_name, 'r')
    speak.speak(file.read())