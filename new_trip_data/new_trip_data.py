import googlemaps
from pyowm.owm import OWM
from dotenv import load_dotenv
load_dotenv()
import os
import pandas as pd

def temp_status(g_request, waypoints=False):

    # OpenWeatherMap Key and Service
    owm_key = os.getenv('open_weather_key')
    mgr = OWM(owm_key).weather_manager() 
    
    ## Get Locations
    if waypoints == False:
        locations = [g_request[0]['legs'][0]['start_location'], 
                     g_request[0]['legs'][0]['end_location']]

    elif waypoints == True:
        locations = []

        for leg in g_request[0]['legs']:
            locations.append(leg['start_location'])
            locations.append(leg['end_location'])
            
        locations = [locations[0]] + locations[1::2]

    ## Get temperature and status
    data_ts = {'temp': [], 'status': []}

    for loc in locations:
        lat = loc['lat']
        lon = loc['lng']
        
        weather_location = mgr.weather_at_coords(lat = lat, lon = lon).weather
        
        temp = weather_location.temperature('celsius')['temp']
        status = weather_location.to_dict()['status']
        
        data_ts['temp'].append(temp)
        data_ts['status'].append(status)

    # Mean temperature of the trip
    mean_temp = sum(data_ts['temp']) / len(data_ts['temp'])

    ## AC
    if mean_temp >= 24:
        ac = 1
    else:
        ac = 0

    # Any element
    if 'Snow' in data_ts['status']:
        rain = 0
        snow = 1
        sun = 0
    elif 'Drizzle' or 'Rain' or 'Thunderstorm' in data_ts['status']:
        rain = 1
        snow = 0
        sun = 0
    elif 'Clear' in data_ts['status']:
        rain = 0
        snow = 0
        sun = 1
    else:
        rain = 0
        snow = 0
        sun = 0

    return mean_temp, ac, rain, snow, sun

def return_frame(distance, speed, temperature, ac, rain, snow, sun):

    frame_ready = pd.DataFrame({'distance': [distance],
                                'speed': [speed],
                                'temp_outside': [temperature],
                                'AC': [ac],
                                'rain': [rain],
                                'snow': [snow],
                                'sun': [sun]})

    return frame_ready


def trip_data(origin, destination, waypoints=None):
    # Google Directions Key and Service
    gmaps_key = os.getenv('directions_key')
    gmaps = googlemaps.Client(key=gmaps_key)

    if waypoints == None:
        request = gmaps.directions(origin = origin,
                                   destination = destination)

        # Get Distance
        distance_km = request[0]['legs'][0]['distance']['value'] / 1000
        
        # Get Duration
        duration_hr = request[0]['legs'][0]['duration']['value'] / 3600

        # Get Speed
        speed = distance_km / duration_hr

        # Weather data
        mean_temp, ac, rain, snow, sun = temp_status(request)

        return return_frame(distance_km, speed, mean_temp, ac, rain, snow, sun)

    elif type(waypoints) == list:
        request = gmaps.directions(origin = origin,
                                   destination = destination,
                                   waypoints = waypoints)

        # Dict with the distance and duration of each of the legs
        data = {'distances': [], 'durations': []}

        for leg in request[0]['legs']:
            data['distances'].append(leg['distance']['value'])
            data['durations'].append(leg['duration']['value'])

        # List with the average speeds per leg
        averages = []
    
        for dist, dur in zip(data['distances'], data['durations']):
            distance_km = dist / 1000
            duration_hr = dur / 3600
    
            averages.append(distance_km / duration_hr)

        # Get Distance and Speed
        distance_km = sum(data['distances']) / 1000
        speed = sum(averages) / len(averages)

        # Weather data
        mean_temp, ac, rain, snow, sun = temp_status(request, waypoints=True)      

        return return_frame(distance_km, speed, mean_temp, ac, rain, snow, sun)