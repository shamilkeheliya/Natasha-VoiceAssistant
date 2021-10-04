import datetime
import editables
import speak
import commands as cmd


def write_note():
    speak.speak('What should I write?')
    answer = cmd.takeCommand().lower()
    date = datetime.datetime.now().date()
    time = datetime.datetime.now().strftime("%H-%M-%S")
    file_name = editables.notes + '/' + str(date) + '-' + str(time) + '.txt'
    file = open(file_name, 'w')
    file.write(f"""
Date: {date}
Time: {time}
    
{answer}
    """)
    speak.speak('Done taking Notes')


def read_note():
    file_name = editables.notes + '/note.txt'
    file = open(file_name, 'r')
    speak.speak(file.read())
