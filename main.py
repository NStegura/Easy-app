import eel 
import pyowm

owm = pyowm.OWM("75bb81838d69ebae146a8658d38fa1e2")

@eel.expose
def get_weather(place):
    mgr = owm.weather_manager()
    print(place)
    observation = mgr.weather_at_place(place)
    w = observation.weather

    temp = w.temperature('celsius')['temp']
    print("В городе " + place + " сейчас " + str(temp) + " градусов!")
    return "В городе " + place + " сейчас " + str(temp) + " градусов!"

eel.init("web")

eel.start("main.html", size=(500, 500))
