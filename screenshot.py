import pyautogui
import editables
import datetime
import speak


def screenshot():
    date = datetime.datetime.now().date()
    time = datetime.datetime.now().strftime("%H-%M-%S")

    image = pyautogui.screenshot()
    image.save(editables.screenshots + '/' + str(date) + '-' + str(time) + '.png')

    speak.speak('Screenshot saved successfully')
