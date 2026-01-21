from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import String, Boolean, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

db = SQLAlchemy()


class User(db.Model):
    id: Mapped[int] = mapped_column(primary_key=True)
    email: Mapped[str] = mapped_column(String(50), unique=True, nullable=False)
    password: Mapped[str] = mapped_column(nullable=False)
    is_active: Mapped[bool] = mapped_column(Boolean(), nullable=False)

    favorite_planets: Mapped[list["Planet"]] = relationship(secondary="favorite_planet", back_populates="fav_planet")
    favorite_peoples: Mapped[list["People"]] = relationship(secondary="favorite_people", back_populates="fav_people")
    favorite_starships: Mapped[list["Starship"]] = relationship(secondary="favorite_starship", back_populates="fav_starship")

class Planet(db.Model):

    __tablename__ = "planet"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(50), unique=True, nullable=False)
    diameter: Mapped[str] = mapped_column(String(50), nullable=False)
    gravity: Mapped[str] = mapped_column(String(50), nullable=False)
    climate: Mapped[str] = mapped_column(String(30), nullable=False)
    terrain: Mapped[str] = mapped_column(String(100), nullable=False)
    

    fav_planet: Mapped[list["User"]] = relationship(secondary="favorite_planet", back_populates="favorite_planets")


favorite_planet = db.Table(
    "favorite_planet",
    db.metadata, 
    db.Column("planet_id", ForeignKey("planet.id"), primary_key=True),
    db.Column("user_id", ForeignKey(("user.id")), primary_key=True)
)

class People(db.Model):

    __tablename__ = "people"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(120), unique=True, nullable=False)
    eye_color: Mapped[str] = mapped_column(String(120),  nullable=False)
    gender: Mapped[str] = mapped_column(String(120),  nullable=False)
    hair_color: Mapped[str] = mapped_column(String(120), nullable=False)
    height: Mapped[int] = mapped_column(nullable=False)

    fav_people: Mapped[list["User"]] = relationship(secondary="favorite_people", back_populates="favorite_people")



    favorite_people= db.Table(
    "favorite_people",
    db.metadata, 
    db.Column("people_id", ForeignKey("people.id"), primary_key=True),
    db.Column("user_id", ForeignKey(("user.id")), primary_key=True)
)


class Starship(db.Model):

    __tablename__ = "starship"
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(120), unique=True, nullable=False)
    consumables: Mapped[str] = mapped_column(String(120),  nullable=False)
    model: Mapped[str] = mapped_column(String(120),  nullable=False)
    length: Mapped[int] = mapped_column(nullable=False)
    passengers: Mapped[int] = mapped_column(nullable=False)


    fav_starship: Mapped[list["User"]] = relationship(secondary="favorite_starship", back_populates="favorite_starship")



    favorite_starship= db.Table(
    "favorite_starship",
    db.metadata, 
    db.Column("starship_id", ForeignKey("starship.id"), primary_key=True),
    db.Column("user_id", ForeignKey(("user.id")), primary_key=True)
)





