import datetime
from datetime import date,time
import os
from flask import request, jsonify
from flask_jwt_extended import create_access_token, create_refresh_token, jwt_required, get_jwt, get_jwt_identity
from flask_restful import Resource, abort
from sqlalchemy import func
from config import USER_UPLOAD_FOLDER
from models import db, User, Theatre, Movie, Booking, UserRating, MovieRatings
from werkzeug.security import generate_password_hash, check_password_hash

datetime = datetime.datetime



def is_timeframe_within_range(starttime, endtime, timeframe_start, timeframe_end):
    start_time = starttime.time()
    end_time = endtime.time()

    return start_time <= timeframe_start <= end_time or start_time <= timeframe_end <= end_time
 
class UserRegister(Resource):

    def post(self):
        image = None
        if request.content_type == "application/json":
            username = request.json['username']
            password = request.json['password']
            email = request.json['email']
        else:
            username = request.form['username']
            password = request.form['password']
            email = request.form['email']
            image = request.files["image"]

        if username is None:
            return abort(400, message='Username not provided.')

        if password is None:
            return abort(400, message='Password not provided.')
        if email is None:
            return abort(400, message='email not provided.')

        user = User.query.filter_by(username=username).first()

        if user:
            return abort(401, message='Username already exists.')

        hashed_pw = generate_password_hash(password)
        if not image:
            user = User(
                username=username,
                password=hashed_pw,
                email=email,
            )
        else:
            image_path = f"{USER_UPLOAD_FOLDER}/{image.filename}"
            user = User(username=username,
                        password=hashed_pw,
                        email=email,
                        profile_image=image.filename
                        )
            image.save(image_path)

        db.session.add(user)
        db.session.commit()

        access_token = create_access_token(identity=username, additional_claims={'role': "user"})

        response = jsonify({'message': 'You have successfully registered.',
                            'accessToken': access_token,
                            'username': username,
                            })
        response.status_code = 201

        return response


class UpdateProfile(Resource):
    @jwt_required()
    def post(self):
        image =None
        new_username =None
        email = None
        username = get_jwt_identity()
        user = User.query.filter_by(username=username).first()

        if not user:
            return abort(404, message='User not found.')

        if request.content_type == "application/json":
            new_username = request.json.get("username")
            email = request.json.get('email')
        else:
            new_username = request.form.get("username")
            email = request.form.get('email')
            image = request.files.get("image")

        if new_username is not None and new_username != '':
            user.username = new_username

        if email is not None and email != '':
            user.email = email

        if image:
            image_path = f"{USER_UPLOAD_FOLDER}/{image.filename}"
            image.save(image_path)
            if(user.profile_image):
                if(os.path.exists(f"{USER_UPLOAD_FOLDER}/{user.profile_image}")):
                    os.remove(f"{USER_UPLOAD_FOLDER}/{user.profile_image}")
            user.profile_image = image.filename
        try:
            db.session.commit()
            new_access_token = create_access_token(identity=user.username, additional_claims={'role': "user"})
            response = jsonify({
                "username":user.username,
                "accessToken":new_access_token
            })
            response.status_code = 200
            return response
        except Exception as e:
            return abort(500, message='Error in updating profile.')


class GetUserShow(Resource):
    @jwt_required()
    def get(self, movie_id):
        role = get_jwt().get("role")
        if role != "user":
            return abort(401, message="Unauthorized")
        movie = Movie.query.filter_by(id=movie_id).first()
        if not movie:
            return abort(404, message="movie not found")
        serialized_movie = []
        serialized_movie.append(movie.name)
        serialized_movie.append(movie.ticketPrice)
        serialized_movie.append(movie.startTime)
        serialized_movie.append(movie.endTime)
        serialized_movie.append(movie.theatre_name)
        Avialiable_seats = movie.totalSeats - movie.seatsSold
        serialized_movie.append(Avialiable_seats)
        resp = jsonify(serialized_movie)
        resp.status_code = 200
        return resp


class BookingShow(Resource):
    @jwt_required()
    def post(self, th_id, movie_id):
        role = get_jwt().get("role")
        if role != "user":
            return abort(401, message="Unauthorized")
        theatre_exists = Theatre.query.filter_by(id=th_id).first()
        if not theatre_exists:
            return abort(404, message="theatre doesnt exists")
        movie = Movie.query.filter_by(id=movie_id).first()
        if not movie:
            return abort(404, message="movie doesnt exists")
        number = request.json["number"]
        if number is None or number <= 0 or number == '':
            return abort(401, message="number of seats is empty or zero")
        if number > movie.totalSeats:
            return abort(401, message="number of seats is greater than available seats")
        if number > movie.totalSeats - movie.seatsSold:
            return abort(409, message="That many seats are unavailable")
        identity = get_jwt_identity()
        id = User.query.filter_by(username=identity).first().user_id
        booking_instance = Booking()
        booking_instance.userid = int(id)
        booking_instance.numberSeats = number
        da = date(day=datetime.now().day, year=datetime.now().year, month=datetime.now().month)
        booking_instance.booking_time = da
        booking_instance.movie_id = movie_id
        try:
            db.session.add(booking_instance)
            movie.seatsSold += number
            db.session.commit()

            resp = jsonify({
                "message": "Booking confirmed"
            })
            resp.status_code = 200
            return resp
        except:
            return abort(500, message="some server error")


class GetUserVenues(Resource):
    @jwt_required()
    def post(self):
        role = get_jwt().get("role")
        if role != "user":
            return abort(401, message="unauthorized access")
        all_venues = None
        location = None
        start = None
        end = None
        is_start_present= False
        is_end_present = True
        message = request.json["msg"]
        location = request.json.get("location")
        start = request.json.get("start")
        end = request.json.get('end')



        if start is not None and start!='':
                start =datetime.strptime(start, "%H:%M").time()
                is_start_present=True
        if end is not None and end!='':
                end =datetime.strptime(end, "%H:%M").time()
                is_end_present=True
        if (is_start_present and not is_end_present) or (not is_start_present and is_end_present):
            is_start_present=False
            is_end_present=False 
        
        if location is not None and location != '':    
            all_venues = Theatre.query.filter_by(locaton=location)
        else:
            all_venues = Theatre.query.all()
        serialized_venues = []
        if(len(list(all_venues))<=0):
            response = jsonify({
            "venues": serialized_venues
            })
            
            response.status_code = 200
            return response

        for v in all_venues:
            
                c = {
                "id": v.id,
                "name": v.name,
            }
                f = []
                for d in v.movies:
                    if datetime.now() < d.startTime:
                        if is_start_present and is_end_present:
                            if is_timeframe_within_range(d.startTime,d.endTime,start,end):
                                movie_rating = MovieRatings.query.filter_by(movie_name=d.name).first()
                                rating = movie_rating.rating if movie_rating else None
                                movie = {
                                    "movie_id": d.id,
                                    "movie_name": d.name,
                                    "image": d.image,
                                    "tags": d.tags,
                                    "description": d.description,
                                    "start": d.startTime,
                                    "end": d.endTime,
                                    "seats": d.totalSeats - d.seatsSold,
                                }
                                if rating is None:
                                    f.append(movie)
                                else:
                                    movie["rating"] = rating
                                    f.append(movie)
                        else:
                                movie_rating = MovieRatings.query.filter_by(movie_name=d.name).first()
                                rating = movie_rating.rating if movie_rating else None

                                movie = {
                                    "movie_id": d.id,
                                    "movie_name": d.name,
                                    "image": d.image,
                                    "tags": d.tags,
                                    "description": d.description,
                                    "start": d.startTime,
                                    "end": d.endTime,
                                    "seats": d.totalSeats - d.seatsSold,
                                }
                                if rating is None:
                                    f.append(movie)
                                else:
                                    movie["rating"] = rating
                                    f.append(movie)


                       

                c["movies"] = f
                if len(f) > 0:
                        serialized_venues.append(c)
        response = jsonify({
            "venues": serialized_venues
        })
        response.status_code = 200
        return response


class UserCheck(Resource):
    @jwt_required()
    def get(self):
        role = get_jwt().get("role")
        if role != "user":
            return abort(401, message="unauthorized access")
        identity = get_jwt_identity()
        admin = User.query.filter_by(username=identity)
        if not admin:
            return abort(401, message="admin name not found in the database")
        reponse = jsonify({
            "message": "success"
        })
        reponse.status_code = 200
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

        access_token = create_access_token(identity=username, additional_claims={"role": "user"})

        response = jsonify({'message': 'You have been logged in successfully!',
                            'accessToken': access_token,
                            'username': username,
                            })
        response.status_code = 200

        return response


class getBookings(Resource):
    @jwt_required()
    def get(self):
        role = get_jwt().get("role")
        if role != "user":
            return abort(401, message="unauthorized access")
        identity = get_jwt_identity()
        id = User.query.filter_by(username=identity).first().user_id
        bookings = Booking.query.filter_by(userid=int(id))
        bookings_arr = []
        index = 0
        bookings_map = {}
        re = 0
        for v in bookings:
            z = v.movie.id
            a = v.movie.name
            b = v.movie.theatre_name
            c = v.movie.startTime
            d = v.movie.endTime
            f = v.numberSeats
            rating = None
            can_rate = True
            for rate in v.user.ratings:
                if rate.movie == a:
                    can_rate = False
                    rating = rate.rating
            if bookings_map.get(f"{v.movie.name}{v.movie.theatre_name}{v.movie.startTime}") is None:
                bookings_arr.append({
                    "id": z,
                    "movie": a,
                    "venue": b,
                    "start": c,
                    "end": d,
                    "can_rate": can_rate,
                    "rating": rating,
                    "noseats": f
                })
            else:
                bookings_arr[bookings_map.get(f"{v.movie.name}{v.movie.theatre_name}{v.movie.startTime}")][
                    "noseats"] += f
            bookings_map[f"{v.movie.name}{v.movie.theatre_name}{v.movie.startTime}"] = index
            index += 1
        if len(bookings_arr) <= 0:
            resp = jsonify({
                "message": "no bookings"
            })
            resp.status_code = 200
            return resp
        else:
            resp = jsonify(bookings_arr)
            resp.status_code = 200
            return resp


class Rate(Resource):
    @jwt_required()
    def post(self, movie_id):
        role = get_jwt().get("role")
        if role != "user":
            return abort(401, message="unauthorized access")
        identity = get_jwt_identity()
        user_id = User.query.filter_by(username=identity).first().user_id
        if not user_id:
            return abort(401, message="user doesnt exist")
        movie = Movie.query.filter_by(id=movie_id).first()
        if not movie:
            return abort(404, message="movie doesnt exists")
        rating = request.json["rating"]
        if not rating or rating is None:
            abort(401, message="rating is empty")
        prev_rate = UserRating.query.filter_by(userid=user_id, movie=movie.name).first()
        if prev_rate:
            return abort(401, message="already rated")
        user_rating = UserRating(userid=user_id, movie=movie.name, rating=rating)
        db.session.add(user_rating)
        db.session.commit()
        movie_to_rate = MovieRatings.query.filter_by(movie_name=movie.name).first()
        rating_count = UserRating.query.filter_by(userid=user_id, movie=movie.name).count()
        sum_rating = db.session.query(func.sum(UserRating.rating)).filter(UserRating.userid == user_id,
                                                                          UserRating.movie == movie.name).scalar()
        float_rating = float(sum_rating / rating_count)
        movie_to_rate.rating = float_rating
        mov = movie_to_rate.movie_name
        try:
            db.session.commit()
            resp = jsonify({
                "message": "done",
                "rate": float_rating,
                "moive": mov
            })
            resp.status_code = 200
            return resp
        except:
            resp = jsonify({
                "err": "e"
            })
            resp.status_code = 400
            return resp


class getUser(Resource):
    @jwt_required()
    def get(self):
        role = get_jwt().get("role")
        if role != "user":
            return abort(401, message="unauthorized access")
        identity = get_jwt_identity()
        user = User.query.filter_by(username=identity).first()
        if not user:
            return abort(401, message="user doesnt exist")
        serialized_user = []
        serialized_user.append(user.username)
        serialized_user.append(user.email)
        if (user.profile_image):
            serialized_user.append(user.profile_image)
        resp = jsonify(serialized_user)
        resp.status_code = 200
        return resp


class SearchMovie(Resource):
    def get(self, search):
        all_venues = Theatre.query.all()
        serialized_venues = []
        for v in all_venues:
            c = {
                "id": v.id,
                "name": v.name,
            }
            if v.movies:
                f = []
                for d in v.movies:
                    if search.upper() in d.name.upper()  or search.lower() in d.tags.lower().split(
                            ','):
                        if datetime.now() < d.startTime:
                            f.append({
                                "movie_id": d.id,
                                "movie_name": d.name,
                                "image": d.image,
                                "tags": d.tags,
                                "description": d.description,
                                "start": d.startTime,
                                "end": d.endTime,
                                "seats": d.totalSeats - d.seatsSold
                            })

                c["movies"] = f
            if len(c["movies"]) > 0:
                serialized_venues.append(c)
        response = jsonify({
            "venues": serialized_venues
        })
        response.status_code = 200
        return response


class ChangePass(Resource):
    @jwt_required()
    def post(self):
        role = get_jwt().get("role")
        if role != "user":
            return abort(401, message="unauthorized access")
        identity = get_jwt_identity()
        user = User.query.filter_by(username=identity).first()
        if not user:
            return abort(401, message="user doesnt exist")
        password = request.json["oldpassword"]
        new_pass = request.json["password"]
        if password is None or new_pass is None:
            return abort(401, message="please provide all fields")
        if not check_password_hash(user.password, password):
            return abort(401, message='Wrong Password')
        user.password = generate_password_hash(new_pass)
        db.session.commit()
        resp = jsonify({
            "message": "success"
        })
        resp.status_code = 200



class GetUservenueData(Resource):
    @jwt_required()
    def get(self, id):
        role = get_jwt().get("role")
        if role != "user":
            return abort(401, message="Unauthorized")
        venue = Theatre.query.filter_by(id=id).first()
        if not venue:
            return abort(404, message="venue doesnt exist")
        name = venue.name
        place = venue.place
        location = venue.locaton
        capacity = venue.capacity
        resp = jsonify({
            "name": name,
            "place": place,
            "location": location,
            "capacity": capacity
        })
        resp.status_code = 200
        return resp
