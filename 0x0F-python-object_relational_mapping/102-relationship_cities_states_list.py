#!/usr/bin/python3
"""
This module contains script that lists all
City objects from the database hbtn_0e_101_usa,
"""
import sys
from relationship_state import Base, State
from relationship_city import City
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, Session
if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
        sys.argv[1], sys.argv[2], sys.argv[3]))
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()
    records = session.query(City).order_by(City.id).all()
    for row in records:
        print("{}: {} -> {}".format(row.id, row.name, row.state.name))
