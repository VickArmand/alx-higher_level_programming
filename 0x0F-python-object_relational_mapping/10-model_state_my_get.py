#!/usr/bin/python3
"""
This module prints the State object with the name
passed as argument from the database hbtn_0e_6_usa
"""
import sys
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, Session
if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
        sys.argv[1], sys.argv[2], sys.argv[3]))
    Session = sessionmaker(bind=engine)
    session = Session()
    records = session.query(State).filter(State.name == sys.argv[4]).all()
    if len(records) == 0:
        print("Not found")
    else:
        for row in records:
            print("{}".format(row.id))
