from flask_sqlalchemy import SQLAlchemy
from datetime import date,datetime,timedelta
db = SQLAlchemy()

class User(db.Model):
    __tablename__ = 'users'
    user_id = db.Column(db.Integer(),primary_key=True,autoincrement=True)
    username = db.Column(db.String(),unique=True)
    password = db.Column(db.String(), nullable=False)
    email = db.Column(db.String(), nullable=False)
    ratings = db.relationship('UserRating',backref="user",lazy='dynamic')

    # How many movies user has booked -> table has to be made
    # userinfo = db.relationship('UserInfo', back_populates='user', lazy=True, uselist=False)

class Admin(db.Model):
    __tablename__ = 'admins'
    
    username = db.Column(db.String(), primary_key=True)
    password = db.Column(db.String(), nullable=False)
    # email = db.Column(db.String())


class Theatre(db.Model):
    __tablename__ = 'theatres'

    id = db.Column(db.Integer(), primary_key=True,autoincrement=True)
    name = db.Column(db.String(), nullable=False, unique=True)
    place = db.Column(db.String(), nullable=False)
    locaton = db.Column(db.String(), nullable=False)
    capacity = db.Column(db.Integer(), nullable=False)
    movies = db.relationship('Movie', backref='theatre', lazy="dynamic")

class Movie(db.Model):
    __tablename__ = 'movies'

    id = db.Column(db.Integer(), primary_key=True,autoincrement=True)
    name = db.Column(db.String(), nullable=False, unique=True)
    rating = db.Column(db.Float(), nullable=False)
    tags = db.Column(db.String(), nullable=False)
    ticketPrice = db.Column(db.Float(), nullable=False)
    startTime = db.Column(db.DateTime(), nullable=False)
    endTime = db.Column(db.DateTime(), nullable=False)
    seatsSold = db.Column(db.Integer(), nullable=False)
    totalSeats = db.Column(db.Integer(), nullable=False)
    theatreId = db.Column(db.Integer(), db.ForeignKey('theatres.id'))
    ratings=db.relationship('UserRating',backref="movie",lazy="dynamic")
    image = db.Column(db.String(), nullable=False)


class UserRating(db.Model):
    __tablename__ = 'userRating'
    id = db.Column(db.Integer(),primary_key=True,autoincrement=True)
    userid = db.Column(db.Integer(), db.ForeignKey('users.user_id'))
    movie_id = db.Column(db.Integer(),db.ForeignKey("movies.id"))
    rating = db.Column(db.Integer(), nullable=False)
    __table_args__ = (
        db.CheckConstraint('rating <= 5', name='rating shoudl be less than 5'),
    )

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

