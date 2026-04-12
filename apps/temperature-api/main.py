from fastapi import FastAPI, Query
import random

app = FastAPI()

@app.get("/temperature")
def get_temperature(location: str = Query(...)):
    return {
        "location": location,
        "temperature": round(random.uniform(-10, 35), 1)
    }
