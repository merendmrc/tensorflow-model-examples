from tensorflow.keras.models import load_model, Sequential
from sklearn.metrics import mean_squared_error, mean_absolute_error
import pandas as pd
import numpy as np

model = load_model("sequential_model_2.h5", custom_objects={"mse": mean_squared_error})
data = np.array([2016,6300,569,28,5.5]).reshape(1,-1)
data = pd.DataFrame(data,columns=["year","mileage","tax", "mpg","engineSize"])
tahmin = model.predict(data)
print(tahmin)

