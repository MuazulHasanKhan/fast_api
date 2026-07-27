from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

SQLALCHEMY_DATABASE_URL = "sqlite:///./test.db" # sqlite:// format, to signify current directory ./ then name


# To establish the connection with the database
#  Allows to work through multiple threads. This is important for web applications where multiple requests can be handled simultaneously.
engine = create_engine(SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False}) # connect_args is only needed for sqlite. For other databases, it can be omitted.

# Session maker is a factory for creating new Session objects. It is configured with the engine and other options.
# AUtoflush = False means that changes made to objects in the session will not be automatically flushed to the database until explicitly requested. This can improve performance in some cases, but it also means that you need to be careful to flush changes when necessary.
# Autocommit = False means that changes made to objects in the session will not be automatically committed to the database until explicitly requested. This allows for more control over when changes are persisted, but it also means that you need to be careful to commit changes when necessary.
SessionLocal = sessionmaker(bind = engine, autocommit = False, autoflush = False)


# The declarative base class is a foundational class that all of our SQLAlchemy models will inherit from. It provides the necessary functionality for defining database tables and their relationships in an object-oriented manner.
Base = declarative_base() # This is the base class for our models. All models will inherit from this class.

