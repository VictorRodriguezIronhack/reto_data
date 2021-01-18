import pandas as pd 
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error


def modelo_predictivo(distancia, velocidad, temp_int, temp_out, ac, rain, sun):
    df= pd.read_csv('measurements.csv', sep=",", decimal=",")

    df_2=df[['distance',
    'consume',
    'speed',
    'temp_inside',
    'temp_outside',
    'gas_type',
    'AC',
    'rain',
    'sun']]
    df_2

    df_2=pd.get_dummies(df_2, columns=['gas_type'], drop_first=True)
    df_2=df_2.dropna()



    X= df_2[['distance',
    'speed',
    'temp_inside',
    'temp_outside',
    'AC',
    'rain',
    'sun',
    'gas_type_SP98'
            ]]

    y=df_2['consume']

    lr = LinearRegression()

    model=lr.fit(X,
            y)


    dict1 = {'distance' : [distancia, distancia], 'speed' : [velocidad, velocidad], 'temp_inside' : [temp_int, temp_int], 'temp_outside': [temp_out, temp_out], 'AC':[ac, ac], 'rain':[rain, rain], 'sun': [sun, sun], 'gas_type_SP98':[0,1]}

    x_eva=pd.DataFrame(dict1)



    y_pred=model.predict(x_eva)

    if y_pred[0]<y_pred[1]:
        return f'El modelo determino un consumo de {round(y_pred[0], 3)} para el gas E10 y {round(y_pred[1], 3)} para SP98, (dicho consumo es por cada 100 Km) por lo tanto para sus condiciones el gas mas optimo es el E10'
    
    else:
        return f'El modelo determino un consumo de {round(y_pred[0],3)} para el gas E10 y {round(y_pred[1], 3)} para SP98, (dicho consumo es por cada 100 Km) por lo tanto para sus condiciones el gas mas optimo es el SP98'
