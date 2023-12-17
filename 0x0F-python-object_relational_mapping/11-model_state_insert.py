#!/usr/bin/python3
"""
This module contains script that lists all State
objects from the database hbtn_0e_6_usa
"""
import sys
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, Session
engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
    sys.argv[1], sys.argv[2], sys.argv[3]))
Session = sessionmaker(bind=engine)
session = Session()
state1 = State(name="Louisiana")
session.add(state1)
session.commit()
print(state1.id)
