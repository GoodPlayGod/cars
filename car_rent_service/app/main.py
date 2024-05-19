import os
import uvicorn
from fastapi import FastAPI, Depends, HTTPException, status
from sqlalchemy.orm import Session
from typing import List, Annotated
from car_rent_model.model import Car
from car_rent_database.database import CarDB, SessionLocal

app = FastAPI()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


db_dependency = Annotated[Session, Depends(get_db)]


@app.get("/health", status_code=status.HTTP_200_OK)
async def service_alive():
    return {"message": "Service alive"}


@app.post("/add_car", response_model=Car)
async def add_car(car: Car, db: db_dependency):
    new_car = CarDB(**car.dict())
    db.add(new_car)
    db.commit()
    db.refresh(new_car)
    return new_car


@app.get("/cars", response_model=List[Car])
async def list_cars(db: db_dependency):
    return db.query(CarDB).all()


@app.get("/get_car_by_id/{car_id}", response_model=Car)
async def get_car_by_id(car_id: int, db: db_dependency):
    car = db.query(CarDB).filter(CarDB.id == car_id).first()
    if not car:
        raise HTTPException(status_code=404, detail="Car not found")
    return car


@app.delete("/delete_car/{car_id}")
async def delete_car(car_id: int, db: db_dependency):
    car = db.query(CarDB).filter(CarDB.id == car_id).first()
    if not car:
        raise HTTPException(status_code=404, detail="Car not found")
    db.delete(car)
    db.commit()
    return {"message": "Car deleted successfully"}


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=int(os.getenv('PORT', 80)))
