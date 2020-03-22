# encoding: utf-8

import pymysql
from flask import Flask, render_template, request, redirect, url_for, session, flash
from flask_sqlalchemy import SQLAlchemy

import config
from exts import db
from models import User, Model

pymysql.install_as_MySQLdb()

app = Flask(__name__)
app.config.from_object(config)
db.init_app(app)
db = SQLAlchemy(app)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/get_path', methods=['GET', 'POST'])
def get_path():
    if request.method == 'POST':
        keyword = request.form.get('keyword')
        getpath = Model.query.filter_by(name=keyword).first()
        path = getpath[0]
        return render_template('STL.html', path=path)
    else:
        return render_template('search.html')


@app.route('/search/', methods=['GET', 'POST'])
def search():
    if request.method == 'GET':
        return render_template('search.html')
    else:
        pass


@app.route('/login/', methods=['GET', 'POST'])
def login():
    if request.method == 'GET':
        return render_template('login.html')
    else:
        telephone = request.form.get('telephone')
        password = request.form.get('password')
        user = User.query.filter(User.telephone == telephone, User.password == password).first()
        if user:
            session['user_id'] = user.id
            session.permanent = True
            return redirect(url_for('index'))
        else:
            return "用户名或密码错误，请重新输入"


@app.route('/regist/', methods=['GET', 'POST'])
def regist():
    if request.method == 'GET':
        return render_template('regist.html')
    else:
        telephone = request.form.get('telephone')
        username = request.form.get('username')
        password1 = request.form.get('password1')
        password2 = request.form.get('password2')

        # 手机号码验证
        user = User.query.filter(User.telephone == telephone).first()
        if user:
            return '该手机号码已经被注册'
        else:
            if password1 != password2:
                return '两次填写的密码不一致，请重新输入'
            else:
                user = User(telephone=telephone, username=username, password=password1)
                db.session.add(user)
                db.session.commit()
                flash('You can now login.')
                return redirect(url_for('login'))


if __name__ == '__main__':
    app.run()
