from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import sessionmaker, declarative_base

# pip install sqlalchemy
Base = declarative_base()


class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    age = Column(Integer)


# echo=True - właczenie logów bazy
engine = create_engine('sqlite:///my_database.db', echo=True)
Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)
session = Session()

new_user = User(name="JAn Kowalski", age=56)
session.add(new_user)  # INSERT INTO users (name, age) VALUES (?, ?)
session.commit()
session.close()

users = session.query(User).all()
for user in users:
    print(user.name)
# SELECT users.id AS users_id, users.name AS users_name, users.age AS users_age
# FROM users

# JAn Kowalski
# JAn Kowalski
# JAn Kowalski
