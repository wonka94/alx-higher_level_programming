#!/usr/bin/python3
"""
Deletes all State objects with a name
containing the letter 'a' from the
database `hbtn_0e_6_usa`.
"""

from sys import argv
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    """
    Deletes all State objects with a name containing
    the letter 'a' from the database.
    """

    db_uri = 'mysql+mysqldb://{}:{}@localhost:3306/{}'.format(
        argv[1], argv[2], argv[3])
    engine = create_engine(db_uri)
    Session = sessionmaker(bind=engine)

    session = Session()

    query = session.query(City, State).join(State)

    for c, s in query.all():
        print("{}: ({:d}) {}".format(s.name, c.id, c.name))

    session.commit()
    session.close()
