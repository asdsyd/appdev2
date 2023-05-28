from flask_sqlalchemy import SQLAlchemy
from datetime import date,datetime,timedelta
import uuid
convention = {
    "ix": 'ix_%(column_0_label)s',
    "uq": "uq_%(table_name)s_%(column_0_name)s",
    "ck": "ck_%(table_name)s_%(constraint_name)s",
    "fk": "fk_%(table_name)s_%(column_0_name)s_%(referred_table_name)s",
    "pk": "pk_%(table_name)s"
}

metadata = MetaData(naming_convention=convention)
db = SQLAlchemy(metadata=metadata)
class User(db.Model):
    __tablename__ = 'users'
    user_id = db.Column(db.Integer(),primary_key=True,autoincrement=True)
    username = db.Column(db.String(),unique=True)
    password = db.Column(db.String(), nullable=False)
    email = db.Column(db.String(), nullable=False)
    ratings = db.relationship('UserRating',backref="user",lazy='dynamic')
    bookings = db.relationship("Booking",backref="user",lazy="dynamic")



class Admin(db.Model):
    __tablename__ = 'admins'
    
    username = db.Column(db.String(), primary_key=True)
    password = db.Column(db.String(), nullable=False)
    # email = db.Column(db.String())


class Theatre(db.Model):
    __tablename__ = 'theatres'

    id = db.Column(db.String(36), primary_key=True, default=lambda: str(uuid.uuid4()))
    name = db.Column(db.String(), nullable=False, unique=True)
    place = db.Column(db.String(), nullable=False)
    locaton = db.Column(db.String(), nullable=False)
    capacity = db.Column(db.Integer(), nullable=False)
    movies = db.relationship('Movie', backref='theatre', lazy="dynamic")

class Movie(db.Model):
    __tablename__ = 'movies'

    id = db.Column(db.String(36), primary_key=True, default=lambda: str(uuid.uuid4()))
    name = db.Column(db.String(), nullable=False)
    tags = db.Column(db.String(), nullable=False)
    ticketPrice = db.Column(db.Float(), nullable=False)
    startTime = db.Column(db.DateTime(), nullable=False)
    endTime = db.Column(db.DateTime(), nullable=False)
    seatsSold = db.Column(db.Integer(), nullable=False)
    totalSeats = db.Column(db.Integer(), nullable=False)
    theatreId = db.Column(db.Integer(), db.ForeignKey('theatres.id'))
    theatre_name = db.Column(db.String(),nullable=False)
    bookings = db.relationship("Booking",backref="movie",lazy="dynamic")
    image = db.Column(db.String())


class UserRating(db.Model):
    __tablename__ = 'userRating'
    id = db.Column(db.String(36), primary_key=True, default=lambda: str(uuid.uuid4()))
    userid = db.Column(db.Integer(), db.ForeignKey('users.user_id'))
    movie = db.Column(db.Integer(),db.ForeignKey("movieratings.movie_name"))
    rating = db.Column(db.Integer(), nullable=False)
    __table_args__ = (
        db.CheckConstraint('rating <= 5', name='rating_should_be_less_than_5'),
    )

class MovieRatings(db.Model):
    __tablename__ = 'movieratings'
    movie_name = db.Column(db.String(),primary_key=True)
    rating = db.Column(db.Float())

class Booking(db.Model):
    __tablename__ = "userBooking"
    id = db.Column(db.String(36), primary_key=True, default=lambda: str(uuid.uuid4()))
    userid = db.Column(db.Integer(), db.ForeignKey('users.user_id'))
    movie_id = db.Column(db.Integer(),db.ForeignKey("movies.id"))






# class UserInfo(db.Model):
#     __tablename__ = 'userinfo'
#     username = db.Column(db.String(), db.ForeignKey('users.username'))
#     profile_id = db.Column(db.Integer(), primary_key=True)
#     bio = db.Column(db.String())
#     skin = db.Column(db.String())
#     top = db.Column(db.String())
#     hairColor = db.Column(db.String())
#     eyes = db.Column(db.String())
#     eyebrows = db.Column(db.String())
#     mouth = db.Column(db.String())
#     facialHair = db.Column(db.String())
#     facialHairColor = db.Column(db.String())
#     clothing = db.Column(db.String())
#     clothingColor = db.Column(db.String())
#     accessories = db.Column(db.String())
#     accessoriesColor = db.Column(db.String())
#
#     user = db.Relationship('User', back_populates='userinfo', lazy=True)

