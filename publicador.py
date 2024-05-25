import ssl
import paho.mqtt.publish as publish
import paho.mqtt.client as mqtt
import pandas as pd

# Configuración de certificados
ca_cert = "./certs/ca.crt"
client_cert = "./certs/cliente.crt"
client_key = "./certs/cliente.key"

# Configuración de mensajes a publicar
data = pd.read_csv("Portland.csv")
for index, row in data.head(30).iterrows():

    datetime, Temperatura, Tiempo, Direccion_viento, Velocidad_viento= row
    
    topic = f'home/Portland/viento'
    
    message = f'Temperatura: {Temperatura}, Tiempo: {Tiempo}, Direccion_viento: {Direccion_viento}, Velocidad_viento: {Velocidad_viento}'
    
    print(Temperatura)
    print()
    # comprobaciones 

    publish.single(topic, message, hostname="0.0.0.0", port=8883, tls={'ca_certs': ca_cert, 'certfile': client_cert, 'keyfile': client_key}, protocol=mqtt.MQTTv311)
