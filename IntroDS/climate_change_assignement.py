import pandas as pd
import seaborn as sns
from sklearn.linear_model import LinearRegression


data = pd.read_csv("climate_change.csv")
data_features = data["MEI", "CO2", "CH4", "N20",
                     "CFC-11", "CFC-12", "TSI", "Aerosols", "Temp"]

sns.pairplot(data_features)

x_train = data["MEI", "CO2", "CH4", "N20", "CFC-11",
               "CFC-12", "TSI", "Aerosols", "Temp"][:284]
y_train = data["Temo"][:284]

model = LinearRegression().fit(x_train, y_train)
