import datetime
from flask import request, jsonify
from flask_jwt_extended import create_access_token, create_refresh_token,jwt_required,get_jwt,get_jwt_identity
from flask_restful import Resource, abort
from config import USER_UPLOAD_FOLDER
from models import db, User,Theatre,Movie,Booking,UserRating,MovieRatings
from werkzeug.security import generate_password_hash, check_password_hash

datetime = datetime.datetime
class UserRegister(Resource):

    def post(self):
        image = None
        if request.content_type == 'multipart/form-data': 
            username = request.form['username']
            password = request.form['password']
            email = request.form['email']
            image = request.files["image"]
        else:
            username = request.json['username']
            password = request.json['password']
            email = request.json['email']

        if username is None:
            return abort(400, message='Username not provided.')

        if password is None:
            return abort(400, message='Password not provided.')

        user = db.session.query(User).get(username)

        if  user:
            return abort(401, message='Username already exists.')

        hashed_pw = generate_password_hash(password)
        if not image:
            user = User(
                username=username,
                password=hashed_pw,
                email=email,
            )
        else:
            image_path = f"{USER_UPLOAD_FOLDER}+/{image.filename}"
            user = User(username=username,
                        password=hashed_pw,
                        email=email,
            profile_image=image_path
                        )
            image.save(image_path)


        db.session.add(user)


        db.session.commit()

        access_token = create_access_token(identity=username,additional_claims={'role':"user"})
        refresh_token = create_refresh_token(identity=username,additional_claims={"role":"user"})

        response = jsonify({'message' : 'You have successfully registered.',
                            'accessToken' : access_token,
                            'refresh_token' : refresh_token,
                            'username' : username,
                            })
        response.status_code=201

        return response

class GetUserShow(Resource):
    @jwt_required()
    def get(self,movie_id):
        role = get_jwt().get("role")
        if role != "user":
            return abort(401,message="Unauthorized")
        movie = Movie.query.filter_by(id=movie_id).first()
        if not movie:
            return abort(404,message="movie not found")
        serialized_movie =[]
        serialized_movie.append(movie.name)
        serialized_movie.append(movie.ticketPrice)
        serialized_movie.append(movie.startTime)
        serialized_movie.append(movie.endTime)
        serialized_movie.append(movie.theatre_name)
        Avialiable_seats = movie.totalSeats-movie.seatsSold
        serialized_movie.append(Avialiable_seats)
        resp = jsonify(serialized_movie)
        resp.status_code = 200
        return resp

class BookingShow(Resource):
    @jwt_required()
    def post(self,th_id,movie_id):
        role = get_jwt().get("role")
        if role != "user":
            return abort(401,message="Unauthorized")
        theatre_exists = Theatre.query.filter_by(id=th_id).first()
        if not theatre_exists:
            return abort(404,message="theatre doesnt exists")
        movie = Movie.query.filter_by(id=movie_id).first()
        if not movie:
            return abort(404,message="movie doesnt exists")
        number = request.json["number"]
        if number is None or number <=0 or number == '':
            return abort(401,message="number of seats is empty or zero")
        if number>movie.totalSeats:
            return abort(401,message="number of seats is greater than available seats")
        identity = get_jwt_identity()
        id = User.query.filter_by(username=identity).first().user_id
        booking_instance = Booking()
        booking_instance.userid = int(id)
        booking_instance.movie_id = movie_id
        try:
            db.session.add(booking_instance)
            movie.seatsSold += number 
            db.session.commit()
            
            resp= jsonify({
                "message":"Booking confirmed"
            })
            resp.status_code=200
            return resp
        except:
            return abort(500,message="some server error")




class GetUserVenues(Resource):
    @jwt_required()
    def get(self):
        role= get_jwt().get("role")
        if role != "user":
            return abort(401,message="unauthorized access")
        all_venues=Theatre.query.all()
        serialized_venues = []
        for v in all_venues:
            c = {
                "id":v.id,
                "name":v.name,
            }

            if v.movies:


                f =[]
                for d in v.movies:
                    if datetime.now()>d.startTime:
                            f.append({
                                "movie_id":d.id,
                                "movie_name":d.name,
                                "image":d.image,
                                "description":d.description,
                                "start":d.startTime,
                                "end":d.endTime,
                                "seats":d.totalSeats - d.seatsSold
                            })
                c["movies"] = f
            serialized_venues.append(c)
        response = jsonify({
            "venues":serialized_venues
        })
        response.status_code=200
        return response

class UserCheck(Resource):
    @jwt_required()
    def get(self):
        role= get_jwt().get("role")
        if role != "user":
            return abort(401,message="unauthorized access")
        identity = get_jwt_identity()
        admin = User.query.filter_by(username=identity)
        if not admin:
            return abort(401,message="admin name not found in the database")
        reponse = jsonify({
            "message":"success"
        })
        reponse.status_code=200
        return reponse
class UserLogin(Resource):

    def post(self):

        username = request.json['username']
        password = request.json['password']

        if username is None:
            return abort(400, message='Username not provided.')

        if password is None:
            return abort(400, message='Password not provided.')

        user = User.query.filter_by(username=username).first()

        if not user:
            return abort(401, message='Username provided does not exist.')

        if not check_password_hash(user.password, password):
            return abort(401, message='Wrong Password')


        access_token = create_access_token(identity=username,additional_claims={"role":"user"})
        refresh_token = create_refresh_token(identity=username,additional_claims={"role":"user"})


        response = jsonify({'message' : 'You have been logged in successfully!',
                            'accessToken' : access_token,
                            'refresh_token' : refresh_token,
                            'username': username,
                            })
        response.status_code=200

        return response
    

class getBookings(Resource):
    @jwt_required()
    def get(self):
        role= get_jwt().get("role")
        if role != "user":
            return abort(401,message="unauthorized access")
        identity = get_jwt_identity()
        id = User.query.filter_by(username = identity).first().id
        bookings = Booking.query.filer_by(userid=id)