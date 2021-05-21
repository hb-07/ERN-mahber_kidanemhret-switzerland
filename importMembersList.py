import os
import psycopg2, csv


from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker

engine = create_engine("postgresql+psycopg2://Bsrat:asmayt@localhost:5433/mahhberKidanemhret")
db = scoped_session(sessionmaker(bind=engine))

def main():
    f = open("members.csv")
    reader = csv.reader(f)
    for id, username, lastname, place, email, password in reader:
        db.execute("INSERT INTO members (id, username, lastname, place, email, password) VALUES (:id, :username, :lastname, :place, :email, :password)",
                    {"id": id, "username": username, "lastname": lastname, "place": place, "email": email, "password": password})
        print(f"Added new member with id {id} and name {username}." )
    db.commit()


if __name__ == "__main__":
    main()
