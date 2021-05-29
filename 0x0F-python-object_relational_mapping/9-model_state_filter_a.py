#!/usr/bin/python3

""" Print all data from State object if name contains 'a' """


if __name__ == "__main__":

    from sqlalchemy.orm import sessionmaker
    from sqlalchemy import create_engine
    from model_state import Base, State
    from sys import argv

    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                           .format(argv[1], argv[2], argv[3]),
                           pool_pre_ping=True)

    Session = sessionmaker(bind=engine)
    session = Session()
    states = session.query(State)
    for state in states:
        if 'a' in state.name:
            print("{}: {}".format(state.id, state.name))
