import pandas as pd
import tensorflow as tf

df =pd.read_csv("C:/Users/Stiv/Desktop/dataset_aritmetico.csv") 


X = df[["A", "B"]].values  
#y = df["Suma"].values      
#y = df["Resta"].values
y = df["Multiplicacion"].values
#y = df["Division"].values               

model = tf.keras.Sequential([
    tf.keras.layers.Input(shape=(2,)),
    tf.keras.layers.Dense(10, activation='relu'),
    tf.keras.layers.Dense(1)
])


model.compile(optimizer='adam', loss='mse', metrics=['mae'])


model.fit(X, y, epochs=200, verbose=1)


#model.save("modelo_suma.h5")
#model.save("modelo_resta.h5")
model.save("modelo_multiplicacion.h5")
#model.save("modelo_division.h5")


import numpy as np
print("Predicción de 4 * 5:", model.predict(np.array([[4, 5]]))[0][0])