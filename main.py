from fastapi import FastAPI
from pydantic import BaseModel
import uvicorn

class HouseFeatures(BaseModel):
    address: str
    surface: float
    rooms: int

app = FastAPI()


@app.get("/")
def read_root():
    return {"message": "Welcome to the House Price Prediction API"}


@app.post("/predict")
def predict_price(features: HouseFeatures):
    addr = features.address
    surf = features.surface
    rms = features.rooms

    estimated_price = 100 + 100 * surf + 10000 * rms

    return {
        "input_address": addr,
        "estimated_price": estimated_price,
        "currency": "EUR"
    }


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8080)