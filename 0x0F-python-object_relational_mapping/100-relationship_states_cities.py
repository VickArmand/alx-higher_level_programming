#!/usr/bin/python3
"""
This module contains script that creates the State “California”
with the City “San Francisco” from the database hbtn_0e_100_usa
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
    city1 = City(name="San Francisco")
    state1 = State(name="California", cities=[city1])
    session.add(city1)
    session.add(state1)
    session.commit()
