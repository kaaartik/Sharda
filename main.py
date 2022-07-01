from email import message
from unicodedata import name
from flask import Flask, redirect, render_template, request, url_for, session
import sqlite3
from werkzeug.utils import secure_filename
import uuid as uuid
import os
import json
app = Flask(__name__)
app.secret_key = 'yash'
upload_folder = 'static/images/'
app.config['upload_folder'] = upload_folder


# class process():
#     nam = None


# getprocess = process()


def sessionblank():
    session["successful"] = ''


@app.route('/')
def index():
    sessionblank()
    return render_template("index.html")


@app.route('/buy')
def buy():
    connection = sqlite3.connect('database.db')
    my_cursor = connection.cursor()
    my_cursor.execute("Select * from sharda2")
    lala = my_cursor.fetchall()
    connection.close()
    temp = ''
    if session["successful"] != '':
        temp = session["successful"]
        session.pop("successful", None)
    return render_template("Buy.html", lala=lala, temp=temp)


@app.route('/sell')
def sell():
    sessionblank()
    return render_template("sell.html")


@app.route('/upload')
def upload():
    sessionblank()
    return render_template("upload.html")


@app.route('/selldetails', methods=['post', 'get'])
def selldetails():
    sessionblank()
    firstname = request.form['first_name']
    lastname = request.form['last_name']
    email = request.form['email']
    phone = request.form['phone']
    housename = request.form['house_name']
    carpetarea = request.form['carpet_area']
    age = request.form['age_building']
    loc1 = request.form['nearby_loc1']
    loc2 = request.form['nearby_loc2']
    price = request.form['price']
    type = request.form['type']
    size = request.form['size']
    face = request.form['face']
    parking = request.form['parking']
    bathroom = request.form['bathroom']
    balcony = request.form['balcony']
    possess = request.form['possess']
    power = request.form['power']
    furnish = request.form['furnish']
    gated = request.form['gated']
    input1 = request.files['input1']
    input2 = request.files['input2']
    input3 = request.files['input3']
    input4 = request.files['input4']
    input5 = request.files['input5']
    input6 = request.files['input6']
    input7 = request.files['input7']
    input8 = request.files['input8']
    maintain = request.form['Maintainence']
    water = request.form['water']
    bedroom = request.form['bedroom']
    unit = request.form['unit']

    a = float(price)
    b = unit
    print("---------------------")
    print(a)
    print(b)

    if(a<=99 and b=="Lakhs"):
        output = 1

    elif(a>=1 and a<=2):
        output = 2

    elif(a>2 and a<=3):
        output = 3

    elif(a>3 and a<=4):
        output = 4

    elif(a>4 and a<=5):
        output = 5

    elif(a>5):
        output = 6
    pic = secure_filename(input1.filename)
    pic1 = str(uuid.uuid1()) + "_" + pic
    saver = request.files['input1']
    saver.save(os.path.join(app.config['upload_folder'], pic1))
    input1 = pic1

    pic = secure_filename(input2.filename)
    pic1 = str(uuid.uuid1()) + "_" + pic
    saver = request.files['input2']
    saver.save(os.path.join(app.config['upload_folder'], pic1))
    input2 = pic1

    pic = secure_filename(input3.filename)
    pic1 = str(uuid.uuid1()) + "_" + pic
    saver = request.files['input3']
    saver.save(os.path.join(app.config['upload_folder'], pic1))
    input3 = pic1

    pic = secure_filename(input4.filename)
    pic1 = str(uuid.uuid1()) + "_" + pic
    saver = request.files['input4']
    saver.save(os.path.join(app.config['upload_folder'], pic1))
    input4 = pic1

    pic = secure_filename(input5.filename)
    pic1 = str(uuid.uuid1()) + "_" + pic
    saver = request.files['input5']
    saver.save(os.path.join(app.config['upload_folder'], pic1))
    input5 = pic1

    pic = secure_filename(input6.filename)
    pic1 = str(uuid.uuid1()) + "_" + pic
    saver = request.files['input6']
    saver.save(os.path.join(app.config['upload_folder'], pic1))
    input6 = pic1

    pic = secure_filename(input7.filename)
    pic1 = str(uuid.uuid1()) + "_" + pic
    saver = request.files['input7']
    saver.save(os.path.join(app.config['upload_folder'], pic1))
    input7 = pic1

    pic = secure_filename(input8.filename)
    pic1 = str(uuid.uuid1()) + "_" + pic
    saver = request.files['input8']
    saver.save(os.path.join(app.config['upload_folder'], pic1))
    input8 = pic1

    connection = sqlite3.connect('database.db')
    my_cursor = connection.cursor()
    id = my_cursor.execute(
        "SELECT id from sharda2 ORDER BY id DESC LIMIT 1").fetchone()
    id = id[0]
    id = id+1
    print(id)
    my_cursor.execute("INSERT INTO sharda2 VALUES(?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)", (id, firstname, lastname, email, phone, housename,
                      carpetarea, age, loc1, loc2, price, type, size, face, parking, bathroom, balcony, possess, power, furnish, gated, input1, input2, input3, input4, input5, input6, input7, input8, maintain, bedroom, water,unit,output))

    connection.commit()
    connection.close()
    session["successful"] = "You have successfull registered"
    return redirect(url_for('buy'))


@app.route('/selldetails1', methods=['post', 'get'])
def selldetails1():
    sessionblank()
    firstname = request.form['first_name']
    lastname = request.form['last_name']
    email = request.form['email']
    phone = request.form['phone']
    housename = request.form['house_name']
    carpetarea = request.form['carpet_area']
    age = request.form['age_building']
    loc1 = request.form['nearby_loc1']
    loc2 = request.form['nearby_loc2']
    price = request.form['price']
    type = request.form['type']
    size = request.form['size']
    face = request.form['face']
    parking = request.form['parking']
    bathroom = request.form['bathroom']
    balcony = request.form['balcony']
    possess = request.form['possess']
    power = request.form['power']
    furnish = request.form['furnish']
    gated = request.form['gated']
    input1 = request.files['input1']
    input2 = request.files['input2']
    input3 = request.files['input3']
    input4 = request.files['input4']
    input5 = request.files['input5']
    input6 = request.files['input6']
    input7 = request.files['input7']
    input8 = request.files['input8']
    maintain = request.form['Maintainence']
    water = request.form['water']
    bedroom = request.form['bedroom']
    unit = request.form['unit']

    a = float(price)
    b = unit
    print("---------------------")
    print(a)
    print(b)

    if(a<=99 and b=="Lakhs"):
        output = 1

    elif(a>=1 and a<=2):
        output = 2

    elif(a>2 and a<=3):
        output = 3

    elif(a>3 and a<=4):
        output = 4

    elif(a>4 and a<=5):
        output = 5

    elif(a>5):
        output = 6
    pic = secure_filename(input1.filename)
    pic1 = str(uuid.uuid1()) + "_" + pic
    saver = request.files['input1']
    saver.save(os.path.join(app.config['upload_folder'], pic1))
    input1 = pic1

    pic = secure_filename(input2.filename)
    pic1 = str(uuid.uuid1()) + "_" + pic
    saver = request.files['input2']
    saver.save(os.path.join(app.config['upload_folder'], pic1))
    input2 = pic1

    pic = secure_filename(input3.filename)
    pic1 = str(uuid.uuid1()) + "_" + pic
    saver = request.files['input3']
    saver.save(os.path.join(app.config['upload_folder'], pic1))
    input3 = pic1

    pic = secure_filename(input4.filename)
    pic1 = str(uuid.uuid1()) + "_" + pic
    saver = request.files['input4']
    saver.save(os.path.join(app.config['upload_folder'], pic1))
    input4 = pic1

    pic = secure_filename(input5.filename)
    pic1 = str(uuid.uuid1()) + "_" + pic
    saver = request.files['input5']
    saver.save(os.path.join(app.config['upload_folder'], pic1))
    input5 = pic1

    pic = secure_filename(input6.filename)
    pic1 = str(uuid.uuid1()) + "_" + pic
    saver = request.files['input6']
    saver.save(os.path.join(app.config['upload_folder'], pic1))
    input6 = pic1

    pic = secure_filename(input7.filename)
    pic1 = str(uuid.uuid1()) + "_" + pic
    saver = request.files['input7']
    saver.save(os.path.join(app.config['upload_folder'], pic1))
    input7 = pic1

    pic = secure_filename(input8.filename)
    pic1 = str(uuid.uuid1()) + "_" + pic
    saver = request.files['input8']
    saver.save(os.path.join(app.config['upload_folder'], pic1))
    input8 = pic1

    connection = sqlite3.connect('database1.db')
    my_cursor = connection.cursor()
    id = my_cursor.execute(
        "SELECT id from sharda3 ORDER BY id DESC LIMIT 1").fetchone()
    id = id[0]
    id = id+1
    print(id)
    my_cursor.execute("INSERT INTO sharda3 VALUES(?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)", (id, firstname, lastname, email, phone, housename,
                      carpetarea, age, loc1, loc2, price, type, size, face, parking, bathroom, balcony, possess, power, furnish, gated, input1, input2, input3, input4, input5, input6, input7, input8, maintain, bedroom, water,unit,output))

    connection.commit()
    connection.close()
    session["successful"] = "You have successfull registered"
    return redirect(url_for('rentbuy'))


@app.route('/rentbuy')
def rentbuy():
    connection = sqlite3.connect('database1.db')
    my_cursor = connection.cursor()
    my_cursor.execute("Select * from sharda3")
    lala = my_cursor.fetchall()
    connection.close()
    temp = ''
    if session["successful"] != '':
        temp = session["successful"]
        session.pop("successful", None)
    return render_template("rentbuy.html", lala=lala, temp=temp)


@app.route('/rentsell')
def rentsell():
    return render_template("rentsell.html")

# @app.route('/info')
# def info():
#     sessionblank()
#     lame = getprocess.nam
#     return render_template("info.html", name=lame)


@app.route('/info/<string:id>')
def info(id):
    sessionblank()
    connection = sqlite3.connect('database.db')
    my_cursor = connection.cursor()
    name = my_cursor.execute(
        "Select * from sharda2 where id=?", (id,)).fetchone()
    print(name)
    return render_template("info.html", name=name)


@app.route('/info1/<string:id>')
def info1(id):
    sessionblank()
    connection = sqlite3.connect('database1.db')
    my_cursor = connection.cursor()
    name = my_cursor.execute(
        "Select * from sharda3 where id=?", (id,)).fetchone()
    return render_template("info.html", name=name)


if(__name__) == '__main__':
    app.run(debug=True)
