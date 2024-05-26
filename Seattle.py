import ssl
import paho.mqtt.publish as publish
import pandas as pd
import paho.mqtt.client as mqtt
import time

# Configuración de certificados
ca_cert = "./certs/ca.crt"
client_cert = "./certs/Seattle.crt"
client_key = "./certs/Seattle.key"

# Leer datos del CSV
data = pd.read_csv("Seattle.csv")

# Publicar mensajes con un retraso de 3 segundos
for index, row in data.iterrows():
    datetime, Temperatura, Tiempo, Direccion_viento, Velocidad_viento = row
    Temperatura = Temperatura - 273
    topic = f'home/Seattle/viento'
    message = f'Temperatura: {Temperatura}, Tiempo: {Tiempo}, Direccion_viento: {Direccion_viento}, Velocidad_viento: {Velocidad_viento}'
    publish.single(
        topic,
        message,
        hostname="0.0.0.0",
        port=8883,
        qos=2,
        tls={'ca_certs': ca_cert, 'certfile': client_cert, 'keyfile': client_key},
        protocol=mqtt.MQTTv311
    )
    time.sleep(10)
