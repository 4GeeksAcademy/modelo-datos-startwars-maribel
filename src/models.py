from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import String, Boolean, ForeignKey, Table, Column
from sqlalchemy.orm import Mapped, mapped_column, relationship

db = SQLAlchemy()


class User(db.Model):
    id: Mapped[int] = mapped_column(primary_key=True)
    email: Mapped[str] = mapped_column(String(50), unique=True, nullable=False)
    password: Mapped[str] = mapped_column(nullable=False)
    is_active: Mapped[bool] = mapped_column(Boolean(), nullable=False)
    favorite_planet: Mapped[list["Planet"]] = relationship(secondary = "planet_user", back_populates="planet")
    favorite_people: Mapped[list["People"]] = relationship(secondary = "people_user", back_populates="people")
    favorite_starship: Mapped[list["Starship"]] = relationship(secondary = "starship_user", back_populates="starship")
    
class Planet(db.Model):

    __tablename__ = "planet"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(50), unique=True, nullable=False)
    diameter: Mapped[str] = mapped_column(String(50), nullable=False)
    gravity: Mapped[str] = mapped_column(String(50), nullable=False)
    climate: Mapped[str] = mapped_column(String(30), nullable=False)
    terrain: Mapped[str] = mapped_column(String(100), nullable=False)

    users: Mapped[list["User"]] = relationship(secondary="favorite_planet",back_populates="favorite_planets")


class People(db.Model):

    __tablename__ = "people"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(120), unique=True, nullable=False)
    eye_color: Mapped[str] = mapped_column(String(120),  nullable=False)
    gender: Mapped[str] = mapped_column(String(120),  nullable=False)
    hair_color: Mapped[str] = mapped_column(String(120), nullable=False)
    height: Mapped[int] = mapped_column(nullable=False)
    
    users: Mapped[list["User"]] = relationship(secondary="favorite_people",back_populates="favorite_people")

class Starship(db.Model):

    __tablename__ = "starship"
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(120), unique=True, nullable=False)
    consumables: Mapped[str] = mapped_column(String(120),  nullable=False)
    model: Mapped[str] = mapped_column(String(120),  nullable=False)
    length: Mapped[int] = mapped_column(nullable=False)
    passengers: Mapped[int] = mapped_column(nullable=False)

    users: Mapped[list["User"]] = relationship(secondary="favorite_starship",back_populates="favorite_starship")
 

favorites = Table(
    "favorites",
    db.metadata,
    Column("planet_id", ForeignKey("planet.id")),
    Column("user_id", ForeignKey("user.id")),
    Column("people_id", ForeignKey("people.id")), 
    Column("starship_id", ForeignKey("starship.id"))
)





