from new_trip_data.new_trip_data import *
import pickle

def predict_new_trip():
    print("""\n                         SELECCIÓN DE TAXI

    ¿Un nuevo usuario acaba de contratar nuestro servicio de taxis? Veamos cuál de nuestros coches es el idoneo
    para este trabajo."""
    )

    ## Get Inputs
    origin = input("""\n
    ¿Dónde es la recogida? 
    
    """)

    destination = input("""\n
    ¿Cuál es el destino? 
    
    """)

    waypoints = input("""\n
    ¿Hay que hacer alguna parada intermedia? (S/N) 
    
    """)

    wp = []
    while waypoints == 'S':

        point = input("""\n
    ¿Dónde será la parada? 
        
    """)

        wp.append(point)

        waypoints = input("""\n
    ¿Hay que hacer alguna otra parada intermedia? (S/N) 
        
    """)

    ## Get data for the new trip
    if len(wp) == 0:
        new_trip_df = trip_data(origin=origin, destination=destination)
    else:
        new_trip_df = trip_data(origin=origin, destination=destination, waypoints=wp)

    ## Get the models
    sp95_filename = '3_modeling/random_forest/models/sp95_rfr_model.pkl'
    sp98_filename = '3_modeling/random_forest/models/sp98_rfr_model.pkl'

    with open(sp95_filename, 'rb') as file:
        sp95_model = pickle.load(file)

    with open(sp98_filename, 'rb') as file:
        sp98_model = pickle.load(file)

    ## Make predictions
    sp95_predict = sp95_model.predict(new_trip_df)[0]
    sp98_predict = sp98_model.predict(new_trip_df)[0]

    sp95_price = sp95_predict * 1.38
    sp98_price = sp98_predict * 1.46

    new_trip_df['SP95_prediction'] = round(sp95_predict, 3)
    new_trip_df['SP95_price'] = round(sp95_price, 3)

    new_trip_df['SP98_prediction'] = round(sp98_predict, 3)
    new_trip_df['SP98_price'] = round(sp98_price, 3)

    ## Show the predictions
    print("\n")
    print("\n")
    print(new_trip_df)
    
    if sp95_price < sp98_price:
        print("\nPara este viaje será más conveniente utilizar un taxi con gasolina SP95")
    elif sp95_price > sp98_price:
        print("\nPara este viaje será más conveniente utilizar un taxi con gasolina SP98")
    else:
        print("\nPara este viaje es indiferente utilizar un taxi con gasolina SP98 o SP95")

predict_new_trip()
