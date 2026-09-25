# SPEC 03 — PREDICCIÓN DE VISITANTES ESPERADOS

## 1. Nombre de la especificación

Predicción de visitantes esperados según las condiciones climáticas y los datos históricos.

## 2. Objetivo

Estimar la cantidad de visitantes esperados en Las Orquídeas, Tingo María, a partir de las condiciones meteorológicas obtenidas mediante WeatherAPI y de los datos históricos registrados en la base de datos del proyecto.

## 3. Descripción

El sistema utiliza información meteorológica y datos históricos para generar una estimación de la cantidad de personas que podrían visitar Las Orquídeas durante los próximos días.

La predicción considera principalmente la relación entre las condiciones climáticas y el comportamiento histórico de los visitantes.

La base de datos inicial del proyecto se encuentra en un archivo Excel y contiene registros de ejemplo utilizados para implementar y probar el funcionamiento del modelo. Estos datos son simulados y deben ser reemplazados o calibrados posteriormente con registros reales de visitantes y clima de Las Orquídeas.

## 4. Fuentes de información

El sistema utiliza dos fuentes principales:

### 4.1. Información meteorológica

Se obtiene mediante WeatherAPI y contiene información como:

- Condición climática.
- Temperatura.
- Cantidad de lluvia.
- Probabilidad de lluvia.
- Fecha del pronóstico.

### 4.2. Base histórica

La base histórica se encuentra inicialmente en un archivo Excel y contiene información relacionada con:

- Fecha.
- Lugar.
- Condición climática.
- Temperatura máxima.
- Cantidad de lluvia.
- Humedad.
- Cantidad de visitantes.

## 5. Datos de entrada

Para realizar la estimación se utilizan:

- Fecha del pronóstico.
- Condición climática.
- Temperatura.
- Cantidad de lluvia.
- Probabilidad de lluvia.
- Día de la semana.
- Datos históricos de visitantes.
- Parámetros del modelo almacenados en la hoja correspondiente del Excel.

## 6. Proceso de predicción

El proceso general es el siguiente:

1. El sistema obtiene el pronóstico meteorológico mediante WeatherAPI.
2. Se identifica la condición climática prevista.
3. El sistema obtiene los parámetros correspondientes desde el archivo Excel.
4. Se consideran variables como temperatura, lluvia y día de la semana.
5. El modelo calcula una cantidad estimada de visitantes.
6. El sistema genera además un rango aproximado de visitantes.
7. El resultado se muestra junto con la información meteorológica.

### Flujo general

```text
              WeatherAPI
                  ↓
        Pronóstico meteorológico
                  ↓
       ┌─────────────────────┐
       │ Condición climática │
       │ Temperatura         │
       │ Lluvia              │
       │ Prob. de lluvia     │
       │ Fecha               │
       └─────────────────────┘
                  ↓
        Modelo de predicción
                  ↑
                  │
       Base histórica / Excel
                  │
       ┌─────────────────────┐
       │ Fecha               │
       │ Clima               │
       │ Temperatura         │
       │ Lluvia              │
       │ Visitantes          │
       └─────────────────────┘
                  ↓
       Visitantes esperados
                  ↓
              Frontend
```

## 7. Modelo inicial

La primera versión utiliza parámetros definidos en la hoja **Modelo** del archivo Excel.

Los parámetros permiten establecer un valor base de visitantes para diferentes condiciones climáticas y aplicar factores relacionados con la temperatura, la lluvia y los fines de semana.

La estructura inicial contempla condiciones como:

- Soleado.
- Parcialmente nublado.
- Nublado.
- Lluvia ligera.
- Lluvia.

El resultado corresponde a una estimación inicial y no representa todavía una predicción estadística definitiva.

## 8. Resultado

Para cada día del pronóstico, el sistema presenta:

- Fecha.
- Condición climática.
- Temperatura máxima.
- Probabilidad de lluvia.
- Cantidad de lluvia.
- Visitantes estimados.
- Rango aproximado de visitantes.

Ejemplo de presentación:

```text
Fecha: 26/09/2026
Clima: Lluvia ligera
Temperatura máxima: 28 °C
Probabilidad de lluvia: 60 %
Lluvia: 2 mm

Visitantes esperados: 45
Rango estimado: 38 – 52 visitantes
```

Los valores mostrados anteriormente son únicamente un ejemplo de presentación.

## 9. Base de datos inicial

La información utilizada para desarrollar y probar el sistema se encuentra en:

```text
data/base_datos_clima_visitantes_orquideas.xlsx
```

El archivo contiene las hojas:

- **Historial:** registros de ejemplo de clima y visitantes.
- **Modelo:** parámetros iniciales utilizados para la estimación.
- **Predicciones:** ejemplos de resultados calculados.
- **Resumen:** descripción general de la información.

Los registros actuales son datos simulados creados para validar el funcionamiento del sistema. Para obtener predicciones con mayor sustento, deberán incorporarse posteriormente datos reales de visitantes de Las Orquídeas.

## 10. Manejo de errores y datos faltantes

Si no existe un parámetro específico para una condición meteorológica, el sistema utiliza una categoría climática disponible de acuerdo con la lógica definida en el modelo.

Si la información meteorológica no puede obtenerse, no se genera una nueva predicción y el sistema informa que no fue posible obtener el pronóstico.

## 11. Criterios de aceptación

- El sistema debe obtener el pronóstico meteorológico desde la SPEC 02.
- El sistema debe utilizar la información almacenada en el archivo Excel.
- El sistema debe relacionar las condiciones climáticas con una estimación de visitantes.
- El sistema debe mostrar una estimación para cada día disponible del pronóstico.
- El sistema debe mostrar la cantidad estimada y un rango aproximado.
- El sistema debe indicar que los datos actuales son una implementación inicial cuando corresponda.
- La base histórica debe poder actualizarse posteriormente con datos reales.
- El sistema debe evitar mostrar una predicción cuando no dispone de la información necesaria.

## 12. Relación con la SPEC 02

La SPEC 02 proporciona los datos meteorológicos que utiliza esta especificación.

```text
SPEC 02
Consulta del clima
       ↓
Datos meteorológicos
       ↓
SPEC 03
Predicción de visitantes
       ↓
Visitantes esperados
```

## 13. Evolución futura

Como mejora del proyecto, los datos simulados pueden ser reemplazados progresivamente por registros reales de visitantes de Las Orquídeas.

Con una cantidad suficiente de registros reales, el modelo podrá calibrarse utilizando variables como:

- Temperatura.
- Lluvia.
- Condición climática.
- Día de la semana.
- Temporada.
- Cantidad histórica de visitantes.

Esto permitirá que las predicciones estén basadas en el comportamiento observado en el lugar y no únicamente en parámetros iniciales de demostración.
