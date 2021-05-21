import os
import psycopg2

from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker

engine = create_engine("postgresql+psycopg2://Bsrat:asmayt@localhost:5433/mahhberKidanemhret")
db = scoped_session(sessionmaker(bind=engine))

def main():

    # find the id of the given username and lastname
    username ="Haileab"
    lastname = "Bsrat"
    row_id = db.execute("SELECT id FROM members WHERE username = :username and lastname = :lastname", {"username":username, "lastname": lastname}).fetchone()
    for i in row_id:
        print(i)
        
    # fetch all the members af the database of mahhberKidanemhret
    members = db.execute("SELECT * FROM members").fetchall()
    for member in members:
        print(f"{member.id},    {member.username},   {member.lastname},  {member.place},     {member.email},    {member.password} " )


if __name__ == "__main__":
    main()
