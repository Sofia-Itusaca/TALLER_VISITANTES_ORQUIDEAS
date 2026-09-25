from fastapi import APIRouter, HTTPException
from app.services.weather_service import WeatherService
from app.services.prediction_service import PredictionService

router = APIRouter(prefix="/api", tags=["clima"])

weather_service = WeatherService()
prediction_service = PredictionService()


@router.get("/health")
def health():
    return {"status": "ok", "service": "clima-visitantes-backend"}


@router.get("/dashboard")
def dashboard():
    try:
        data = weather_service.get_forecast(days=7)

        for day in data["days"]:
            prediction = prediction_service.estimate(
                day["description"],
                day["rainMm"],
                day["date"],
            )
            day["prediction"] = prediction

        return data

    except Exception as exc:
        raise HTTPException(
            status_code=502,
            detail="No fue posible obtener el pronóstico meteorológico.",
        ) from exc
