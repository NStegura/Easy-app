import eel 
import pyowm

owm = pyowm.OWM("75bb81838d69ebae146a8658d38fa1e2")

@eel.expose
def get_weather(place):
    mgr = owm.weather_manager()
    print(place)
    observation = mgr.weather_at_place(place)
    w = observation.weather

    temp1 = w.temperature('celsius')['temp']
    print(temp1)
    #print("В городе " + place + " сейчас " + str(temp) + " градусов!")
    return "В городе " + place + " сейчас " + str(temp1) + " градусов! \f"  +  get_answer(temp1)

def get_answer(temp1):
    if temp1 > 10:
        return "T-SHIRT!!!!"
    else:
        return "COAT!!!!"


eel.init("web")

eel.start("main.html", size=(900, 900))
