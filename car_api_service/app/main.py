import os
import uvicorn
from fastapi import FastAPI, HTTPException, status
import requests

app = FastAPI()

CAR_API_URL = "https://carapi.app/api"


@app.get("/health", status_code=status.HTTP_200_OK)
async def service_alive():
    return {"message": "Service alive"}


@app.get("/car/make/{make}/model/{model}")
async def get_car_by_make_model(make: str, model: str):
    response = requests.get(f"{CAR_API_URL}/makes/{make}/models/{model}")
    if response.status_code != 200:
        raise HTTPException(status_code=response.status_code, detail="Error fetching car data")
    return response.json()


@app.get("/car/vin/{vin}")
async def get_car_by_vin(vin: str):
    response = requests.get(f"{CAR_API_URL}/vin/{vin}")
    if response.status_code != 200:
        raise HTTPException(status_code=response.status_code, detail="Error fetching car data")
    return response.json()


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=int(os.getenv('PORT', 80)))
