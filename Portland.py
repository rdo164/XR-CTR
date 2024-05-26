import ssl
import paho.mqtt.publish as publish
import paho.mqtt.client as mqtt
import pandas as pd

# Configuración de certificados
ca_cert = "./certs/ca.crt"
client_cert = "./certs/Portland.crt"
client_key = "./certs/Portland.key"

# Configuración de mensajes a publicar
data = pd.read_csv("Portland.csv")
for index, row in data.head(30).iterrows():
<<<<<<< HEAD:Portland.py
    datetime,Temperatura,Tiempo,Direccion_viento,Velocidad_viento= row
    Temperatura = Temperatura -273
=======

    datetime, Temperatura, Tiempo, Direccion_viento, Velocidad_viento= row
    
>>>>>>> 64e4fdcaec6381c094a720b569310d31413364cd:publicador.py
    topic = f'home/Portland/viento'
    
    message = f'Temperatura: {Temperatura}, Tiempo: {Tiempo}, Direccion_viento: {Direccion_viento}, Velocidad_viento: {Velocidad_viento}'
<<<<<<< HEAD:Portland.py
    publish.single(topic, message, hostname="0.0.0.0", port=8883, qos=2, tls={'ca_certs': ca_cert, 'certfile': client_cert, 'keyfile': client_key}, protocol=mqtt.MQTTv311)
=======
    
    print(Temperatura)
    print()
    # comprobaciones 

    publish.single(topic, message, hostname="0.0.0.0", port=8883, tls={'ca_certs': ca_cert, 'certfile': client_cert, 'keyfile': client_key}, protocol=mqtt.MQTTv311)
>>>>>>> 64e4fdcaec6381c094a720b569310d31413364cd:publicador.py
