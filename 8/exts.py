from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Column, String, NVARCHAR, VARCHAR, create_engine, text, TEXT
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

db = SQLAlchemy()