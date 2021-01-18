from api.app import app
from flask import Flask, render_template, request, send_from_directory,redirect, Response
#from helpers.mongoConnection import *
from bson import json_util #Converts bson to a readable format
import datetime
from bson.objectid import ObjectId
from statistics import mean 



#-----------------------------------------  HOME ROUTE  -----------------------------------------  

#INFO: HOW TO USE API
@app.route("/")
def home():
    return {"Hello":"World"}



'''

#-----------------------------------------  USERS ROUTES  -----------------------------------------
#LIST USERS IN THE DATABASE
@app.route("/users")
def get_users():
    users = db.users.distinct("username")
    return {'TotalUsers':users}



#CREATE USER AND SAVE IT TO THE DB
# - Params : username the user name
# - Returns: user_id
@app.route("/user/create/<username>")  #Get by default
def create_user(username):
    new_user= {"username": username}
    
    if username in db.users.distinct("username"):
        #raise ValueError ("Username already exists.Please, try another username.")
        return {"Error":"Username already exists.Please, try another username."}

    else:
        #insert_data("users",new_user)
        add_user = db.users.insert_one(new_user)
        return json_util.dumps(f"User created succesfully: user_name:{username}, user_id: {add_user.inserted_id} ")






#-----------------------------------------  CHAT ROUTES  -----------------------------------------
#(GET)CREATE CHAT WITH INITIAL PARTICIPANTS:
# - Params : array users ids [user_id]
# - Returns: chat_id
@app.route("/chat/create")
def create_chat():
    chat_name = request.args.get("chat_name")
    chat_users = request.args.getlist("participants")

    #Get ids from the participants
    ids = []
    for i in range(len(chat_users)):
        res = db.users.find({"username":chat_users[i]},{"_id":1})   #Find only the Id for these users
        ids.append(list(res)[0]["_id"])
    
    #Create a dict where the key is the unique user name and the value is its unique ObjectId
    ids_dict = {} 
    for key in chat_users: 
        for value in ids: 
            ids_dict[key] = value 
            ids.remove(value) 
            break  
    
    # Same as previous routes
    if chat_name in db.chats.distinct("chat_name"):
        return {"Error":"Chat already exists.Please, try another super original chat name."}
    else:
        new = db.chats.insert({"chat_name":chat_name, "participants": ids_dict, "created":datetime.datetime.today()})
        return json_util.dumps(f"Chat created succesfully: {new}")



#(GET) ADD MORE USERS TO CHAT
# - Params: chat_id, user_id
# - Returns: chat_id
@app.route("/chat/adduser")
def add_user_to_chat():
    new_user = request.args.get("new_participant")
    existing_chat= request.args.get("chat_name")
    
    chat_id = list(db.chats.find({"chat_name": existing_chat},{"_id":1}))[0]["_id"]
    user_id = list(db.users.find({"username": new_user},{"_id":1}))[0]["_id"]

    # Same as previous routes
    if new_user in db.chats.distinct("participants"):
        return {"Error":"User already in chat.Please, try another."}
    else:
        new = db.chats.update({"_id":ObjectId(chat_id)}, {"$set":{f"participants.{new_user}":user_id }})
        return json_util.dumps(f"User added succesfully: {user_id}")









#-----------------------------------------  MESSAGES ROUTES  ----------------------------------------

#(GET or POST) ADD MESSAGE FROM AN USER_ID TO A CHAT_ID 
# Help: Check that the incoming user is part of this chat id. If not, raise an exception.
# - Params : chat_id, user_id, text
# - Returns: message id
@app.route("/chat/addmessage")
def add_message():
    user = request.args.get("from")
    chat = request.args.get("to")
    text = request.args.get("message")
    
    chat_id = list(db.chats.find({"chat_name": chat},{"_id":1}))[0]["_id"]
    user_id = list(db.users.find({"username": user},{"_id":1}))[0]["_id"]
    
    # Same as previous routes
    if user not in list(list(db.chats.find({"chat_name": chat},{"participants":1}))[0]["participants"].keys()):
        #raise ValueError ("User not in chat.")
        return {"Error":"User not in chat."}
    else:
        new = db.messages.insert({"message":text, "from": user_id, "to":chat_id})
        return json_util.dumps(f"Message added: {new}")





#(GET) GET ALL MESSAGES FROM A CHAT
# - Returns: json array with all messages from this chat_id
@app.route("/chat/list")
def return_messages():
    chat = request.args.get("chat_name") 
    chat_id = list(db.chats.find({"chat_name": chat},{"_id":1}))[0]["_id"]
   
    res = list(db.messages.find({"to": chat_id }, {"message":1}))
    mensa = [res[i]["message"] for i in range(len(res))]
    return json_util.dumps(mensa)
'''


if __name__ == '__main__':
    app.run(debug=True)
   