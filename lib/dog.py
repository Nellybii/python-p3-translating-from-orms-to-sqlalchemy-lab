from models import Dog
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

def create_table(base, engine):
    engine = create_engine('sqlite:///lib/dogs.db')
    base.metadata.create_all(bind=engine)
    Session = sessionmaker(bind=engine)
    return Session()

def save(session, dog):
    session.add(dog)
    session.commit()

def get_all(session):
    return session.query(Dog).all()

def find_by_name(session, name):
    return session.query(Dog).filter_by(name=name).first()

def find_by_id(session, dog_id):
    return session.query(Dog).filter_by(id=dog_id).first()

def find_by_name_and_breed(session, name, breed):
    return session.query(Dog).filter_by(name=name, breed=breed).first()

def update_breed(session, dog, new_breed):
    dog.breed = new_breed
    session.commit()
