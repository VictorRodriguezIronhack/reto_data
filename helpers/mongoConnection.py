from pymongo import MongoClient
from bson.objectid import ObjectId

client = MongoClient()
db = client.get_database("car_fuel_api")

def getConsumeDist(distance, consume):
    curs=db.car_fuel.find({"distance": distance}, {"_id":0,"consume":1})
    return list(curs)

def getConsumeSpeed(speed, consume):
    curs=db.car_fuel.find({"speed": speed}, {"_id":0,"consume":1})
    return list(curs)

def getConsumeTemp(temp_outside, consume):
    curs=db.car_fuel.find({"temp_outside": temp_outside}, {"_id":0,"consume":1})
    return list(curs)

def getConsumeFuel(gas_type, consume):
    curs=db.car_fuel.find({"gas_type": gas_type}, {"_id":0,"consume":1})
    return list(curs)