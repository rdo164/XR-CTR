# XR-CTR
# Tiempo en USA

## Miembros del equipo
- **Colaboradores:** Xabier Telleria Salegi, Rodrigo Ruiz-Cuevas

## Explicación de los Pasos Seguidos
Este proyecto tiene como objetivo conectar un broker MQTT con una base de datos InfluxDB para almacenar datos meteorológicos de diferentes ciudades de Estados Unidos y realizar análisis con Grafana. Se utilizan varios publicadores para enviar datos y un suscriptor para procesarlos y almacenarlos.

## Instrucciones de Uso

### Instalación
1. Clonar el repositorio:

``
git clone https://github.com/rdo164/XR-CTR.git
``
2. Instalar las dependencias:

``
pip install -r requirements.txt
``
3. Generar los certificados
``
cd certs
dos2unix certificados.sh
bash certificados.sh
``
## Ejecución
Ejecución del subscritor
``
docker-compose up -d
python3 subscritor.py
``
Publicar datos desde CSV
``
python3 Portland.py
python3 Denver.py
python3 Dallas.py
python3 Seattle.py
python3 LasVegas.py
``
Generar y Publicar Datos Sintéticos
``
python3 NewYork.py
``

## Posibles vías de mejora
1. Implementar autenticación y autorización en Grafana para una mayor seguridad.
2. Agregar más validaciones de datos para garantizar la integridad de la información.
3. Optimizar el rendimiento del procesamiento de datos y el almacenamiento en la base de datos.
4. Mejorar la documentación y los comentarios en el código para facilitar la comprensión y el mantenimiento.

## Retos Encontrados
1. Configuración adecuada de los certificados para la comunicación segura con el broker MQTT.
2. Validación de los datos recibidos para garantizar su calidad y coherencia.
3. Configuración de InfluxDB y Grafana para la correcta visualización y análisis de los datos.

## Alternativas Posibles

1. Utilizar otras bases de datos de series temporales como Prometheus o TimescaleDB en lugar de InfluxDB.
2. Explorar diferentes opciones de visualización y análisis de datos además de Grafana, como Kibana o Superset.



