from fastapi import FastAPI, Query
import random

app = FastAPI()


SENSOR_LOCATIONS = {
    "1": "Living Room",
    "2": "Bedroom",
    "3": "Kitchen"
}

LOCATIONS_SENSOR = {
    "Living Room": "1",
    "Bedroom": "2",
    "Kitchen": "3"
}

@app.get("/temperature")
def get_temperature(location: str = Query(...)):
    return {
        "location": location,
        "sensor_id": LOCATIONS_SENSOR.get(location, "0"),
        "temperature": round(random.uniform(-40, 40), 1)
    }

@app.get("/temperature/{sensor_id}")
def get_temperature_sensor(sensor_id: str):
    return {
        "location": SENSOR_LOCATIONS.get(sensor_id,"Unknown"),
        "sensor_id": sensor_id,
        "temperature": round(random.uniform(-40, 40), 1)
    }
