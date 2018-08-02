from flask import Flask, render_template, request
import sqlite3 as sql
from pymongo import MongoClient
import datetime
client = MongoClient('localhost:27017')
db = client.test_database
app = Flask(__name__)

@app.route('/')
def home():
   return render_template('home.html')

@app.route('/student')
def new_student():
   return render_template('student.html')


@app.route('/Customer')
def Customer():
   return render_template('Customer.html')

@app.route('/Product')
def Product():
   return render_template('Product.html')

@app.route('/Order')
def Order():
   return render_template('Order.html')

@app.route('/add_product')
def Add_Product():
   return render_template('add_product.html')

@app.route('/show_product')
def Show_Product():
   post=db.products.find()
   return render_template("show_product.html",rows = post)


@app.route('/add_customer')
def Add_Customer():
   return render_template('add_customer.html')

@app.route('/show_customer')
def Show_Customer():
    post=db.customers.find()
    return render_template("show_customer.html",rows = post)

@app.route('/add_order')
def Add_Order():
   return render_template('add_order.html')

@app.route('/show_order')
def Show_Order():
   post=db.orders.find()
   return render_template('show_order.html',rows=post)

@app.route('/add_cust',methods = ['POST', 'GET'])
def add_cust():
   if request.method == 'POST':
      try:
         cid = request.form['cid']
         cname = request.form['cname']
         age = request.form['age']
         gender = request.form['gender']
         city = request.form['city']
         phone = request.form['phone']

         post = {"cid": cid,
         "cname": cname,
         "age": age,
         "gender": gender,
         "city" :city,
         "phone": phone,
         "date": datetime.datetime.utcnow()}
         posts = db.customers
         post_id = posts.insert_one(post).inserted_id
         print(post_id)
         msg = "Record successfully added"
      except:

         msg = "error in insert operation"
      
      finally:
         return render_template("result.html",msg = msg)

@app.route('/add_prod',methods = ['POST', 'GET'])
def add_prod():
   if request.method == 'POST':
      try:
         pid = request.form['pid']
         pname = request.form['pnm']
         manu = request.form['pmanu']
         price = request.form['pprice']

         post = {"pid": pid,
         "pname": pname,
         "manu":manu,
         "price": price}
         posts = db.products
         post_id = posts.insert_one(post).inserted_id
         print(post_id)
         msg = "Record successfully added"
      except:

         msg = "error in insert operation"

      finally:
         return render_template("result.html",msg = msg)



@app.route('/add_ord',methods = ['POST', 'GET'])
def add_ord():
   if request.method == 'POST':
      try:
         ono = request.form['ono']
         month = request.form['month']
         custido = request.form['custido']
         prido = request.form['prido']
         qo= request.form['qo']

         post = {"ono": ono,
         "month": month,
         "custido":custido,
         "prido":  prido,
        "qo":qo}
         posts = db.orders
         post_id = posts.insert_one(post).inserted_id
         print(post_id)
         msg = "Record successfully added"
      except:

         msg = "error in insert operation"

      finally:
         return render_template("result.html",msg = msg)



@app.route('/list')
def list():
   post=db.posts.find()
   return render_template("list.html",rows = post)

if __name__ == '__main__':
   app.run(debug = True)