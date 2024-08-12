import os
import pandas as pd
import seaborn as sbn
import matplotlib.pyplot as plt
import tensorflow as tf
from tensorflow.keras.models import Sequential, load_model
from tensorflow.keras.layers import Dense
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import MinMaxScaler
from sklearn.metrics import mean_absolute_error, mean_squared_error

os.environ['TF_ENABLE_ONEDNN_OPTS'] = '0'


raw_data = pd.read_csv("merc.csv")
# print(raw_data.describe())

########PREP
# dropping non numeric attrs
raw_data.drop(["model","fuelType","transmission"], inplace=True, axis=1)

# cleaning outliers by price
raw_data = raw_data.sort_values("price",ascending=True)
q1 = raw_data["price"].quantile(0.25)
q3 = raw_data["price"].quantile(0.75)
iqr = q3 - q1
iqrMin = q1 - (1.5*iqr)
iqrMax = q3 + (1.5*iqr)
clean_data = raw_data[~((raw_data["price"]<iqrMin) | (raw_data["price"]>iqrMax))]



# sbn.displot(raw_data["price"])
# sbn.displot(clean_data["price"])
# sbn.boxplot(raw_data["price"])
# print(raw_data.info())
# sbn.scatterplot(x="mileage", y="price", data = raw_data, )

# print(clean_data.groupby("year").mean()["price"])
# print(clean_data.sort_values("year", ascending= True))

clean_data = clean_data[clean_data["year"] != 1970]



plt.show()