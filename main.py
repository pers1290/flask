import os
from flask import Flask, flash, request, redirect, render_template
from werkzeug.utils import secure_filename
import sqlite3

app = Flask(__name__)
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'
UPLOAD_FOLDER = 'static/avatar/'
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif'}
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
fon = '/static/fon_img/fon_1.jpg'
avatar = 'static/img_2/profil.png'
name = ''


def allowed_file(filename):
    return '.' in filename and \
        filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


@app.route('/tinttye', methods=['POST', 'GET'])
def tinttye():
    global fon
    global avatar
    connection = sqlite3.connect('db/User.db')
    cursor = connection.cursor()
    cursor.execute('SELECT * FROM Users')
    users = cursor.fetchall()
    connection.commit()
    connection.close()
    len_db = len(users)
    index_list = []
    if len_db % 2 == 0:
        for i in range(0, len_db, 2):
            index_list.append(i)
    else:
        for i in range(0, len_db + 1, 2):
            index_list.append(i)
        users.append(('', 'Tinttye bot', '', '', '/static/img_2/MARS-6.png'))
    return render_template('main.html', file_list=users, index_list=index_list, fon=fon, avatar=avatar)


@app.route('/registration', methods=['POST', 'GET'])
def registration():
    return render_template('registration.html')


@app.route('/change_fon', methods=['POST', 'GET'])
def change_fon():
    global fon
    fon_list = {1: '/static/fon_img/fon_1.jpg', 2: '/static/fon_img/fon_2.jpg', 3: '/static/fon_img/fon_3.jpg'}
    error = ''
    if request.method == 'GET':
        return render_template('change_fon.html', error=error)
    elif request.method == 'POST':
        try:
            number = int(request.form.get('email'))
            fon = fon_list[number]
            return redirect("/tinttye")
        except:
            error = 'Ошибка'
            return render_template('change_fon.html', error=error)


@app.route('/login', methods=['POST', 'GET'])
def login():
    global name
    if request.method == 'GET':
        return render_template('registr.html')
    elif request.method == 'POST':
        answer_1 = request.form.get('firstname')
        answer_2 = request.form.get('email')
        answer_3 = request.form.get('pasvord')
        try:
            # connection = sqlite3.connect('db/Reg.db')
            # cursor = connection.cursor()
            # cursor.execute('INSERT INTO Reg (name, password, phone, favourites) VALUES (?, ?, ?, ?)',
            #                (answer_1, answer_3, answer_2, avatar,''))
            # connection.commit()
            # connection.close()
            name = answer_1
            return redirect("/personal_account")
        except:
            return '<h1>Ошибка</h1>'


@app.route('/personal_account', methods=['POST', 'GET'])
def personal_account():
    global name
    global avatar
    if request.method == 'POST':
        if 'file' not in request.files:
            flash('ERROR')
            return redirect(request.url)
        file = request.files['file']
        if file.filename == '':
            flash('ERROR')
            return redirect(request.url)
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            avatar = f'/static/avatar/{filename}'
            return render_template('personal_account.html', avatar=avatar, name=name)
    return render_template('personal_account.html', avatar=avatar, name=name)


if __name__ == '__main__':
    app.run(port=8000, host='127.0.0.1')
