# TALLER CLIMA VISITANTES

Sistema web para consultar el clima de **Las Orquídeas - Tingo María** y estimar la cantidad de visitantes esperados según las condiciones meteorológicas.

## Idea

El sistema combina:

1. Pronóstico meteorológico de WeatherAPI.
2. Historial de clima + visitantes.
3. Un modelo inicial de estimación por condición climática.
4. Un dashboard semanal con clima y visitantes estimados.

> Los datos históricos incluidos son **datos simulados de ejemplo**. Deben reemplazarse por registros reales cuando estén disponibles.

## Arquitectura

```text
Navegador
   |
   v
Frontend Svelte/Vite
   |
   | /api/...
   v
Backend FastAPI
   |
   +----> WeatherAPI
   |
   +----> Excel / historial de visitantes
```

La clave de WeatherAPI permanece en el backend.

## Ejecutar localmente

### Backend

```powershell
cd backend
python -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install -r requirements.txt
```

Copia `.env.example` a `.env` y coloca tu clave:

```env
WEATHERAPI_KEY=TU_CLAVE
```

Luego:

```powershell
uvicorn app.main:app --reload
```

Backend:

`http://127.0.0.1:8000`

### Frontend

En otra terminal:

```powershell
cd frontend
npm install
npm run dev
```

Frontend:

`http://localhost:5173`

## Docker

Desde la raíz:

```powershell
docker compose up -d --build
```

Aplicación:

`http://localhost:8080`

## Datos

El archivo:

`data/base_datos_clima_visitantes_orquideas.xlsx`

contiene datos simulados de ejemplo y parámetros iniciales del modelo.
