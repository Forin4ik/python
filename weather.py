import pyowm

owm = pyowm.OWM('3e8d209ca8d6bbe7943dfe0e02d6f17d', Language = "ru")

place = input("введите населенный пункт:")

observatorion = owm.weather_at_place(place)
w = observatorion.get_weather()
print(w)