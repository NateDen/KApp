from flask import *


from flask import Flask, request, render_template, send_from_directory, redirect, url_for, json, jsonify, Response
import json, psycopg2, collections
from flask_cors import CORS

app = Flask(__name__)
app.config['SECRET_KEY'] = 'no'
CORS(app)
conn = psycopg2.connect(database="deqf8fkgsoiihn",user="oziyrfgbiacyrj",host='ec2-174-129-226-234.compute-1.amazonaws.com',port='5432', password="085f5ec587cecd96c07ba2d6f0631fbcf240a20ea34f40a5da7eada44d618196")
cursor = conn.cursor()


@app.route('/', methods = ['GET'])
def hello_world():
    if request.method == 'GET':
        return render_template('Home.html')


@app.route('/open_room',methods = ['GET'])
#this function is for redirecting and then populating the drop down list in all pages
def form_open_room():
    if request.method == 'GET':
        return render_template('open_room.html')

    
@app.route('/open_room', methods = ['POST'])
def write_open_room_to_db():
    
    user_id = request.form['user_identification']
    product_name = request.form['product_identification']
    pic_id = request.form['pic_identification']
    details = request.form['details']
    category = request.form['category']
    price = request.form['price']
    quantity = request.form['quantity']
    
    #buy_time = request.form['how_many_hours']
    #hours = True;    
    #if request.form['radio_hours'] != 'hours':
        #hours = False;
        #buy_time = request.form['how_many_days']
                
    #product_arrival = request.form['delivery_fee']
    #days = True;            
    #if request.form['i_deliver'] != 'me':
        #days = False;        
        #product_arrival = request.form['location']
    
    
    #cursor.execute("INSERT INTO kbankapp.openrooms (user_id, product_name) VALUES (%s, %s)", (user_id, product_name));       
    
    
    cursor.execute("INSERT INTO kbankapp.openrooms (user_id, product_name, pic_id, details, category, price, quantity) VALUES (%s, %s, %s, %s, %s, %s, %s)", (user_id, product_name, pic_id, details, category, price, quantity));  
    
    #if days != True:
        #cursor.execute("INSERT INTO Open_Rooms (How_Many_Hours) VALUES (%s)", (hours));       
    #else:
        #cursor.execute("INSERT INTO Open_Rooms (How_Many_Days) VALUES (%s)", (days));                  
    
    conn.commit()
    print(user_id, product_name, pic_id, details, category, price, quantity)    
    return render_template('Home.html')

if __name__ == '__main__':
    app.config['SECRET_KEY'] = 'no'    
    app.debug = True
    debug = True
    app.run(debug = True)