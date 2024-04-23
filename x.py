import requests

# Tu clave API de TomTom
api_key = 'DHv0U5Sq8FHk54W0eNhVvcGwM7kwIS9r'
# Coordenadas para el cuadro delimitador de Madrid, España
bbox = '-3.888954,40.312064,-3.517916,40.643729'
url = f"https://api.tomtom.com/traffic/services/4/incidentDetails?key={api_key}&bbox={bbox}&trafficModelID=0&format=json"

response = requests.get(url)

if response.status_code != 200:
    print("Error en la solicitud: Código de estado", response.status_code)
    print(response.text)  # Esto mostrará el mensaje de error de la API si hay uno
    print(response.text)

else:
    traffic_data = response.json()

print(traffic_data)
