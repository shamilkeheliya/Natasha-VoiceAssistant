import psutil
import speak


def cpu_battery():
    usage = str(psutil.cpu_percent())
    speak.speak(f'Using {usage}% of CPU')

    battery = psutil.sensors_battery()
    battery = battery.percent
    speak.speak(f'You have {str(battery)}% battery level')
