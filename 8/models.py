# coding: utf-8
from sqlalchemy import Column, Integer, String, Text
from flask_sqlalchemy import SQLAlchemy


db = SQLAlchemy()


class Model(db.Model):
    __tablename__ = 'model'

    name = db.Column(db.Integer, primary_key=True)
    path = db.Column(db.Text(collation='utf8_general_ci'), nullable=False)


class User(db.Model):
    __tablename__ = 'user'

    id = db.Column(db.Integer, primary_key=True)
    telephone = db.Column(db.String(11), nullable=False)
    username = db.Column(db.String(50), nullable=False)
    password = db.Column(db.String(100), nullable=False)
