import ssl
import paho.mqtt.publish as publish
import paho.mqtt.client as mqtt
import pandas as pd

# Configuración de certificados
ca_cert = "./certs/ca.crt"
client_cert = "./certs/cliente.crt"
client_key = "./certs/cliente.key"

# Configuración de mensajes a publicar
data = pd.read_csv("new_temperature.csv")
for index, row in data.head(30).iterrows():

    datetime, Temperatura, Tiempo, Direccion_viento, Velocidad_viento= row
    
    # Comprobación de rango de temperatura
    if Temperatura < -20 or Temperatura > 500:
        # Registrar error o descartar la fila
        pass

    # Comprobación de formato de tiempo
    try:
        datetime.strptime(Tiempo, "%Y-%m-%d %H:%M:%S")
        
    except ValueError:
        # Registrar error o descartar la fila
        pass

    # Comprobación de valores válidos en dirección del viento
    if Direccion_viento < 0 or Direccion_viento > 360:
        # Registrar error o descartar la fila
        print("La dirección es errónea")

        pass
        

    # Comprobación de rango de velocidad del viento
    if Velocidad_viento < 0 or Velocidad_viento > 100:
        # Registrar error o descartar la fila
        pass
    topic = f'home/Portland/viento'
    
    message = f'Temperatura: {Temperatura}, Tiempo: {Tiempo}, Direccion_viento: {Direccion_viento}, Velocidad_viento: {Velocidad_viento}'
    
    # comprobaciones 

    publish.single(topic, message, hostname="192.168.208.2", port=8883, tls={'ca_certs': ca_cert, 'certfile': client_cert, 'keyfile': client_key}, protocol=mqtt.MQTTv311)
