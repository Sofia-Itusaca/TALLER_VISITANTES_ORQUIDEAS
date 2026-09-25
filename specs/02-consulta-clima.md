# SPEC 02 — CONSULTA DE INFORMACIÓN CLIMÁTICA

## 1. Nombre de la especificación

Consulta de información climática mediante una API externa.

## 2. Objetivo

Permitir que el sistema obtenga y muestre información meteorológica actual y pronosticada para Tingo María, Huánuco, utilizando una API externa de datos climáticos.

## 3. Descripción

El sistema se conecta con WeatherAPI desde el backend desarrollado con FastAPI. La API proporciona información meteorológica que posteriormente es procesada por el backend y enviada al frontend para ser presentada al usuario.

La aplicación utiliza como ubicación de referencia Tingo María, Huánuco, debido a que el proyecto está orientado al análisis de visitantes de Las Orquídeas.

## 4. Fuente de información

**Servicio:** WeatherAPI

La aplicación consulta el servicio meteorológico desde el backend. La clave de acceso se mantiene en una variable de entorno y no se expone directamente en el frontend.

## 5. Datos obtenidos

Entre los principales datos utilizados se encuentran:

- Ubicación.
- Temperatura actual.
- Sensación térmica.
- Humedad.
- Velocidad del viento.
- Condición climática.
- Temperatura máxima y mínima.
- Cantidad de lluvia.
- Probabilidad de lluvia.
- Pronóstico para los siguientes días.
- Icono representativo de la condición climática.

## 6. Flujo de funcionamiento

1. El usuario ingresa al sistema.
2. El frontend solicita información al backend.
3. El backend realiza la consulta a WeatherAPI.
4. WeatherAPI devuelve la información meteorológica.
5. El backend procesa los datos recibidos.
6. El backend entrega la información al frontend en formato JSON.
7. El frontend muestra los datos meteorológicos al usuario.

### Flujo general

```text
Frontend
   ↓
Backend FastAPI
   ↓
WeatherAPI
   ↓
Datos meteorológicos
   ↓
Backend procesa la respuesta
   ↓
Frontend
   ↓
Información climática mostrada
```

## 7. Entrada

La información necesaria para realizar la consulta es:

- Ubicación: Tingo María, Huánuco, Perú.
- Clave de acceso a WeatherAPI.
- Parámetros de consulta definidos por el backend.

## 8. Proceso

El backend realiza una solicitud al servicio WeatherAPI y obtiene el pronóstico meteorológico. Posteriormente, transforma la respuesta para entregar únicamente los datos necesarios para la aplicación.

El backend utiliza FastAPI y realiza la comunicación externa mediante solicitudes HTTP.

## 9. Salida

El sistema presenta al usuario la información meteorológica de Tingo María, incluyendo el estado actual y el pronóstico de los siguientes días.

Esta información constituye además uno de los insumos utilizados posteriormente por la SPEC 03 para estimar la cantidad de visitantes esperados.

## 10. Manejo de errores

Si el servicio meteorológico no responde correctamente o ocurre un problema durante la consulta, el backend devuelve un error controlado y el frontend muestra un mensaje indicando que no fue posible cargar la información.

## 11. Criterios de aceptación

- El sistema debe poder obtener información meteorológica desde WeatherAPI.
- La información debe corresponder a Tingo María, Huánuco.
- El backend debe procesar la respuesta de la API.
- El frontend debe mostrar la información obtenida.
- La clave de WeatherAPI no debe estar escrita directamente en el código del frontend.
- El sistema debe mostrar un mensaje cuando la consulta meteorológica falle.

## 12. Relación con la siguiente especificación

Los datos meteorológicos obtenidos en esta especificación sirven como entrada para la **SPEC 03 — Predicción de visitantes esperados**, donde las condiciones climáticas se relacionan con los datos históricos de visitantes almacenados en la base de datos utilizada por el proyecto.
