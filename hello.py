import os
from flask_sqlalchemy import SQLAlchemy
from flask import Flask, render_template, session, redirect, url_for
from flask_bootstrap import Bootstrap
from flask_moment import Moment
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired
from datetime import  datetime


basedir = os.path.abspath(os.path.dirname(__file__))

app = Flask(__name__)
app.config['SECRET_KEY'] = 'hard to guess string'
app.config['SQLACHEMY_DATABASE_URI'] =\
    'sqlite:///' + os.path.join(basedir, 'data.sqlite')
app.config['SQLALCHEMY_TRACK_modifications'] = False

db = SQLAlchemy(app)
bootstarp = Bootstrap(app)
moment = Moment(app)


class Role(db.Model):
    __tablename__ = 'roles'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), unique=True)

    def __repr__(self):
        return '<Role %r>' % self.name

class User(db.Model):
    __tablename__ = 'users'
    td = db.Column

class NameForm(FlaskForm):
    name = StringField('What is your name', validators=[DataRequired])
    submit = SubmitField('Submit')


@app.errorhandler(404)
def pae_not_found(e):
    return render_template('404.html'), 404


@app.errorhandler(500)
def internal_server_error(E):
    return render_template('500.html'), 500


@app.route('/', methods=['GET', 'POST'])
def index():
   form = NameForm()
   if form.validate_on_submit():
       session['name'] = form.name.data
       return redirect(url_for('index'))
   return render_template('index.html', form=form, name=session.get('name'))


if __name__ == '__main__':
    app.run()