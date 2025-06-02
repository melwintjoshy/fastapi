from model import predict
from pydantic import BaseModel
from fastapi import FastAPI
import pandas as pd

app = FastAPI()
        
class Output(BaseModel):
    brand : int
    fueltype : int
    citympg : int
    highwaympg : int
    horsepower : int
    peakrpm	: int
    carbody : int

@app.post("/cars/price_prediction")
def car_price_prediction(input : Output):
    data = input.model_dump()
    return predict(pd.DataFrame([data], columns = ["brand", "fueltype", "citympg", "highwaympg", "horsepower", "peakrpm", "carbody"]))
