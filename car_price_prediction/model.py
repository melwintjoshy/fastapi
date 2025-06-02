from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.tree import DecisionTreeRegressor
from sklearn.ensemble import RandomForestRegressor
from sklearn.neural_network import MLPRegressor
from sklearn.preprocessing import LabelEncoder
from sklearn.metrics import mean_squared_error
from sklearn.preprocessing import StandardScaler
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

df = pd.read_csv(r"D:\fastapi\car_price_prediction\CarPrice_Assignment.csv")
X = df.drop('price', axis=1)
y = df.price

brand = []
for name in X.CarName:
    s = name.split(" ")
    brand.append(s[0])

features = ["brand", "fueltype", "citympg", "highwaympg", "horsepower", "peakrpm", "carbody"]

X['brand'] = pd.DataFrame(brand)

X = pd.DataFrame(X, columns=features)

string_df = X.select_dtypes(include=['object'])

# scaler = StandardScaler()
# numeric_cols = X.select_dtypes(include=['number']).columns
# X[numeric_cols] = scaler.fit_transform(X[numeric_cols])

encoder = LabelEncoder()
for col in string_df:
    X[col] = encoder.fit_transform(X[col])

xtrain, xtest, ytrain, ytest = train_test_split(X, y, test_size=0.2, random_state=42)

model= RandomForestRegressor(random_state=42)
model.fit(xtrain, ytrain)
ypred = model.predict(xtest)
mse = mean_squared_error(ypred, ytest)
print(f"{model} model has MSE = {mse ** .5}")

def predict(values):
    ypred = model.predict(values)
    return f"The predicted price of the car is Rs.{int(ypred)}"
