#!/usr/bin/python3

""" Update name from State object if id == 2 """


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
    state = session.query(State).filter(State.id == 2).first()
    if state:
        state.name = "New Mexico"
        session.commit()
