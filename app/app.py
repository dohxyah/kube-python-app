import pymongo
import datetime
from flask import Flask
from flask import request

__author__ = "Ruven Milshtein"

app = Flask(__name__)

# Replace your client from mongodb atlas
client = pymongo.MongoClient("mongodb+srv://root:dohxyah023@kube-mongo-cluster-0.3glfz.mongodb.net/test?retryWrites=true&w=majority")

# Replace the test with your DB name
db = client.test

# Replace the colection name with your collection
collection  = db['users']


def morse_ip(ip_client):
    choices = {'0': '-----', '1': '.----', '2': '..---', '3': '...--', '4': '....-', '5': '.....', '6': '-....',
               '7': '--...', '8': '---..', '9': '----.', '.': '·-·-·-'}
    morse_code = ""
    for digit in ip_client:
        morse_code = morse_code + choices.get(digit) + " "
    return morse_code

def addusertodb(ip_client):

    # check if the user/ip exist in the db
    if len(list(collection.find({'ip': ip_client}))) == 0:
        collection.insert({'ip': ip_client, 'counter': 1, 'lastime': datetime.datetime.now()})
    else: # The user exit, need to update him
        collection.find_one_and_update({'ip': ip_client}, {'$inc': {'counter': 1}, '$set': {'lasttime': datetime.datetime.now()}})


@app.route('/', methods=["GET"])
def hello():
    ip_client_list = morse_ip(request.environ['REMOTE_ADDR'])
    addusertodb(request.environ['REMOTE_ADDR'])
    counter = list(collection.find({'ip': request.environ['REMOTE_ADDR']}))
    counter = counter[0]['counter']

    return "Hello {} \nYour morse ip code is {}\n It's your {} time in the website".format(request.environ['REMOTE_ADDR'], ip_client_list,counter)


if __name__ == "__main__":
    app.run(host="0.0.0.0",port=80, debug=True)

