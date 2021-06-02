#!/usr/bin/python3

""" Print all data from State object """


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
    data = session.query(State).first()
    if data:
        print("{}: {}".format(data.id, data.name))
    else:
        print("Nothing")
