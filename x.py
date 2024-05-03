import requests
import json

# Definir la URL del endpoint
url = "https://openweathermap.org/api/one-call-3/onecall"

# Definir los parámetros de la solicitud
params = {
    "lat": 30.489772,
    "lon": 99.771335,
    "appid": "f2c7227101062f8b180323eb31973383",  # Reemplazar con su clave API de OpenWeatherMap
    "lang":"zh_cn",
    "exclude": "current,minutely,hourly,alerts"  # Excluir datos que no se necesiten

}

# Enviar la solicitud GET al endpoint
response = requests.get(url, params=params)

# Verificar si la solicitud fue exitosa
if response.status_code == 200:
    # Convertir la respuesta JSON a un diccionario
    data = json.loads(response.text)

    # Acceder a los datos históricos
    historical_data = data["daily"]

    # Recorrer los datos históricos
    for day in historical_data:
        # Obtener la fecha
        date = day["dt"]

        # Obtener la temperatura máxima
        temperature_max = day["temp"]["max"]

        # Obtener la temperatura mínima
        temperature_min = day["temp"]["min"]

        # Obtener la presión atmosférica
        pressure = day["pressure"]

        # Obtener la humedad
        humidity = day["humidity"]

        # Imprimir los datos históricos
        print(f"Fecha: {date}")
        print(f"Temperatura máxima: {temperature_max} °C")
        print(f"Temperatura mínima: {temperature_min} °C")
        print(f"Presión atmosférica: {pressure} hPa")
        print(f"Humedad: {humidity} %")
        print("----------------")
else:
    # Imprimir un mensaje de error si la solicitud no fue exitosa
    print(f"Error: {response.status_code}")
