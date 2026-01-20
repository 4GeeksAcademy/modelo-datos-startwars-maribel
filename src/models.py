from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import String, Boolean, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column 

db = SQLAlchemy()

class User(db.Model):
    id: Mapped[int] = mapped_column(primary_key=True)
    email: Mapped[str] = mapped_column(String(120), unique=True, nullable=False)
    password: Mapped[str] = mapped_column(nullable=False)
    is_active: Mapped[bool] = mapped_column(Boolean(), nullable=False)


    def serialize(self):
        return {
            "id": self.id,
            "email": self.email,
            # do not serialize the password, its a security breach
        }

class Planet(db.Model):

    __table_name__ = "planet"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(120), unique=True, nullable=False)
    diameter: Mapped[str] = mapped_column(String(120), nullable=False)
    gravity: Mapped[str] = mapped_column(String(120), nullable=False)
    climate: Mapped[str] = mapped_column(String(120), nullable=False)
    terrain: Mapped[str] = mapped_column(String(120), nullable=False)



class People(db.Model):

    __table_name__ = "people"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(120), unique=True, nullable=False)
    eye_color: Mapped[str] = mapped_column(String(120),  nullable=False)
    gender: Mapped[str] = mapped_column(String(120),  nullable=False)
    hair_color: Mapped[str] = mapped_column(String(120), nullable=False)
    height: Mapped[int] = mapped_column( nullable=False)


class Startship(db.Model):

    __table_name__ = "startship"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(120), unique=True, nullable=False)
    consumables: Mapped[str] = mapped_column(String(120),  nullable=False)
    model: Mapped[str] = mapped_column(String(120),  nullable=False)
    length: Mapped[int] = mapped_column(nullable=False)
    passengers: Mapped[int] = mapped_column( nullable=False)
    

class Favorite(db.Model):

    __table_name__ = "favorite"

    id: Mapped[int] = mapped_column(primary_key=True)

    user_id : Mapped[int] = mapped_column(ForeignKey("user.id"))
    people_id :  Mapped[int] = mapped_column(ForeignKey("people.id"))
    planet_id : Mapped[int] = mapped_column(ForeignKey("planet.id"))
    startship_id : Mapped[int] = mapped_column(ForeignKey("startship.id"))