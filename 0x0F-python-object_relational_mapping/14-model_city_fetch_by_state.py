#!/usr/bin/python3
"""
This module contains script that lists all City
objects from the database hbtn_0e_6_usa
"""
import sys
from model_state import Base, State
from model_city import City
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, Session
if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
        sys.argv[1], sys.argv[2], sys.argv[3]))
    Session = sessionmaker(bind=engine)
    session = Session()
    records = session.query(City.id, City.name, State.name).filter(
            State.id == City.state_id).all()
    for row in records:
        print("{}: ({}) {}".format(row[2], row[0], row[1]))
