from flask import Flask,render_template, jsonify, request, url_for
import random
import json
import pymongo
from pymongo import MongoClient
# import json
from bson import json_util
from flask import Markup
value = Markup('First line.<br>Second line.<br>')

cluster = MongoClient('mongodb+srv://prakash-1211:prakash@cluster0.enw9p.mongodb.net/myFirstDatabase?retryWrites=true&w=majority')

db = cluster["learning_challenge"]
col = db["Name"]

app  = Flask(__name__)
PORT = 3000

@app.route("/", methods=["GET","POST"])
def startpy():

    return render_template("index.html") 



@app.route("/submit", methods=["GET","POST"])
def submit():
    name = request.form.get("feature-title")
    desc  = request.form.get("short_summary")

    col.insert_one({ "Name": name , "description": desc })
    for x in col.find():
        
       

        val=x['Name']
        val2=x['description'] 
    result = {
        'Name' : val ,
        'description' : val2
    }  
    # {{ org.backgroundInfo | replace(‘\n’, ‘<br>’) }} 

    # return json.dumps(result) 
    return render_template('result.html', result = result)
    

@app.route("/file", methods=["GET"])
def file():
    response=[]
    for main in col.find():
        value = main['Name']
        value2 = main['description']
        
        main = {
             'Name' : value ,
             'description' : value2
        }  
        response.append(main)
        print(response)

        
    # return json.dumps(response) 
    return render_template('main.html', main = response)

@app.route("/find/<username>", methods=["GET"])
def find(username):
    db = cluster["learning_challenge"]
    col = db["Name"]
   
    mydata=[]
    myquery = { "Name": username }

    for mydoc in col.find(myquery):
        mydata.append(mydoc)


    print(mydata)
    return render_template('find.html', data=mydata)

    # name =  mydoc['name']
    # desc,

    # for x in mydoc:
    #   print(x)


    # data={
    #     'name' : mydoc['name'],
    #     'description' : mydoc['description']
    # }

    
  




    


if __name__ == "__main__":
    app.run(debug = True,host="0.0.0.0",port = PORT)
