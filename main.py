import streamlit as st

from PIL import Image

portada = Image.open("images/cobify.gif")
st.image(portada, use_column_width=True)
st.write("""
    # Consumo COBIFY según combustible
    
    Se ha analizado el consumo de nuestros coches en función del combustible repostado.
    
    Tenemos registros de un total de 7625 km recorridos.
    Para ello tenemos registros de trece repostajes con un total de 482,5 litros.
    
    En 8 repostajes se ha repostado combustible SP98. En total 284.5 litros.
    En 5 repostajes se ha repostado combustible E10.  En total 198   litros.

    El consumo medio según los litros repostado y los kilómetros realizados es 6.3 litros/100 km.    
    Sin embargo, la media geométrica de los 388 trayectos registrados da un consumo de 4.8 litros/100 km.
    La diferencia es significativa: 30 por ciento inferior al consumo real de litros repostados.
    Esto puede ser debido por:
        a) no tener registrados todos los trayectos realizados entre repostaje y repostaje
        b) la precisión del medidor de consumo de cada trayecto es incorrecta (puede ser debido al tuning de los coches)
        c) tener "perdidas" de combustible
        
    Recomendamos revisar la desviación de dichos registros.
    
    Para el combustible SP98:
    Se han realizado un total de 4249.9 kilómetros.
    Se han repostado un total de 284.5 litros de SP98.
    El consumo medio según los litros repostado y los kilómetros realizados es 6.7 litros/100 km.
    El consumo total según consumo * distancia registrados es                  4.7 litros/100 km.
    La diferencia es de un 41.2 %


    Para el combustible E10:
    Se han realizado un total de 3375.4 kilómetros.
    Se han repostado un total de 198.0 litros de E10.
    El consumo medio según los litros repostado y los kilómetros realizados es 5.9 litros/100 km.
    El consumo total según consumo * distancia registrados es                  4.8 litros/100 km.
    La diferencia es de un 22.7 %
    
    Conclusión:
    El error de medición de consumo se duplica con el combustible SP98 en vez de con el E10.
    Realmente el consumo con ambos combustibles es practicamente el mismo.
    """)
st.image(Image.open("images/Gas_type.png"), use_column_width=True)

st.write("""
    ## Consumo según uso del Aire Acondicionado y/o en días lluviosos
    """)
st.image(Image.open("images/Influencia AC y clima en el consumo.png"), use_column_width=True) 

st.write("""
    ## Recomendación de combustible en función del perfil de trayectos esperados:
    Se tiene información del consumo en función de 
        a) la distancia recorrida
        b) velocidad media
        c) temperatura interior del vehículo
        d) temperatura exterior del vehículo
    No se observa ninguna diferencia de tendencia en el consumo entre los dos combustibles para todas estas variables:
    """)
st.image(Image.open("images/Scatter plots.png"), use_column_width=True)  



st.write("""
    Esto se puede ver también en la siguiente matriz de correlación, donde todos los valores en la columna "consumo" son muy bajos.
    (el 0,99 para los litros consumidos no es determinante por que han sido calculados matemáticamente usando la distancia.)
    """)
st.image(Image.open("images/corr.png"), use_column_width=True) 



st.write("""
    ## Análisis de Daniel Helguera para COBIFY
    """)
st.image(Image.open("images/coche.png"), use_column_width=True) 

