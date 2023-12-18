#!/usr/bin/python3
"""
This module contains script that lists all State objects,
and corresponding City objects,
contained in the database hbtn_0e_101_usa
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
    records = session.query(State).all()
    for row in records:
        print("{}: {}".format(row.id, row.name))
        for city_inst in row.cities:
            print("    {}: {}".format(city_inst.id, city_inst.name))
