from flask_restful import Resource, abort, reqparse
from flask import request, jsonify, json
from flask_jwt_extended import create_access_token, create_refresh_token, jwt_required,get_jwt,get_jwt_identity
from models import Admin, db, Theatre, Movie
from werkzeug.security import check_password_hash, generate_password_hash
import datetime
import os
from config import UPLOAD_FOLDER

datetime = datetime.datetime

class AdminCheck(Resource):
    @jwt_required()
    def get(self):
        role = get_jwt().get("role")

        if role!="admin":
            return abort(401,message="unauthorized for this route")

        identity = get_jwt_identity()
        admin = Admin.query.filter_by(username=identity)
        if not admin:
            return abort(401,message="admin name not found in the database")


        reponse = jsonify({
            "message":"success"
        })
        reponse.status_code=200
        return reponse

class EditVenue(Resource):
    @jwt_required()
    def post(self,id):
        role = get_jwt().get("role")
        if role != "admin":
            return abort(401,message="Unauthorized")
        venue = Theatre.query.filter_by(id=int(id)).first()
        if not venue:
            return abort(404,message="the Venue doesnt exist")
        name = request.json["name"]
        capacity = request.json["capacity"]
        place = request.json["place"]
        location = request.json["location"]
        if (not name):
            return abort(422, message="name is empty")
        if (not place):
            return abort(422, message="place is empty")
        if (not location):
            return abort(422,message="location is empty")
        if (not capacity):
            return abort(422, message="capacity is empty")
        venue.name=name
        venue.place=place
        venue.capacity=capacity
        venue.locaton=location
        if venue.movies:
            for v in venue.movies:
                v.totalSeats= capacity
        db.session.commit()
        resp = jsonify({
            "message":"sucess"
        })
        resp.status_code=200
        return resp


class DeleteVenue(Resource):
    @jwt_required()
    def delete(self,id):
        role = get_jwt().get("role")
        if role != "admin":
            return abort(401,message="Unauthorized")
        venue = Theatre.query.filter_by(id=int(id)).first()
        if not venue:
            return abort(404,message="the Venue doesnt exist")
        try:
            for v in venue.movies:
                db.session.delete(v)
            db.session.delete(venue)
            db.session.commit()
            resp = jsonify({
                "message":"sucess"
            })
            resp.status_code=200
            return resp
        except Exception as e:
             
            resp = jsonify({
                "message":"some server error"
            })
            resp.status_code=501
            return resp
    
class GetVenueData(Resource):
    @jwt_required()
    def get(self,id):
        role = get_jwt().get("role")
        if role != "admin":
            return abort(401,message="Unauthorized")
        venue = Theatre.query.filter_by(id=int(id)).first()
        if not venue:
            return abort(404,message="venue doesnt exist")
        name = venue.name
        place = venue.place
        location = venue.locaton
        capacity= venue.capacity
        resp = jsonify({
            "name":name,
            "place":place,
            "location":location,
            "capacity":capacity
        })
        resp.status_code=200
        return resp






class AdminLogin(Resource):
    def post(self):
        username = request.json['username']
        password = request.json['password']

        admin = Admin.query.filter_by(username=username).first()
        if not admin:
            return abort(401, message="Username is incorrect")

        pass_match = check_password_hash(admin.password, password)
        if not pass_match:
            return abort(401, message="Password incorrect")
        else:
            accessToken = create_access_token(identity=username,additional_claims={"role":"admin"})
            refresh_token = create_refresh_token(identity=username,additional_claims={"role":"admin"})

            response = jsonify({
                'message': 'Admin logged in successfully!',
                "accessToken": accessToken,
                "refresh_token": refresh_token,
                "username": username,
            })
            response.status_code = 200
            return response


class CreateShow(Resource):
    @jwt_required()
    def post(self, id):
        role = get_jwt().get("role")
        if role != "admin":
            return abort(401,message="Unauthorized")
        theatre_exists = Theatre.query.filter_by(id=id).first()
        if not theatre_exists:
            return abort(404,message="theatre doesnt exists")
        if request.content_type == 'application/json':
            args = request.json
            showName = args["showName"]
            rating = args["rating"]
            startTime = args["startTime"]
            endTime = args["endTime"]
            tags = args["tags"]
            ticketPrice = args["ticketPrice"]

            if showName is None or showName == '':
                return abort(401,message="showname is empty")
            if rating is None or rating == '':
                return abort(401,message="rating is empty")
            if ticketPrice is None or ticketPrice == '':
                return abort(401,message="ticketprice is empty")
            if tags is None or tags == '':
                return abort(401,message="tags is empty")
            if startTime is None or startTime == '':
                return abort(401,message="startime is empty")
            if endTime is None or endTime == '':
                return abort(401,message="endtime is empty")
            is_movie = Movie.query.filter_by(name=showName).first()
            if is_movie:
                abort(401,message = "movie already exists")

            start =datetime.strptime(startTime, "%Y-%m-%dT%H:%M")
            end = datetime.strptime(endTime,"%Y-%m-%dT%H:%M")
            show = Movie(name=showName,rating=rating,tags=tags.join(","),ticketPrice=ticketPrice,startTime=start,endTime=end)
            show.theatreId=int(id)
            capacity = Theatre.query.filter_by(id=id).first().capacity
            show.totalSeats =capacity
            show.seatsSold =0
            try:
                db.session.add(show)
                db.session.commit()
                resp= jsonify({
                    "message":"show added sucess"
                })
                resp.status_code=201
                return resp
            except Exception as e:
                resp= jsonify({
                    "error":e.name
                })
                resp.status_code=500
                return resp



        args = request.form
        showName = args["showName"]
        rating = args["rating"]
        startTime = args["startTime"]
        endTime = args["endTime"]
        tags = args["tags"]
        ticketPrice = args["ticketPrice"]
        image = request.files["image"]
        if showName is None or showName == '':
            return abort(401,message="showname is empty")
        if rating is None or rating == '':
            return abort(401,message="rating is empty")
        if ticketPrice is None or ticketPrice == '':
            return abort(401,message="ticketprice is empty")
        if tags is None or tags == '':
            return abort(401,message="tags is empty")
        if startTime is None or startTime == '':
            return abort(401,message="startime is empty")
        if endTime is None or endTime == '':
            return abort(401,message="endtime is empty")
        is_movie = Movie.query.filter_by(name=showName).first()
        if is_movie:
                abort(401,message = "movie already exists")
        start =datetime.strptime(startTime, "%Y-%m-%dT%H:%M")
        end = datetime.strptime(endTime,"%Y-%m-%dT%H:%M")
        image.save(f"{UPLOAD_FOLDER+'/'+image.filename}")


        show = Movie(name=showName,rating=rating,tags=tags.join(","),ticketPrice=ticketPrice,startTime=start,endTime=end,image=f"{UPLOAD_FOLDER+'/'+image.filename}")
        show.theatreId=int(id)
        capacity = Theatre.query.filter_by(id=id).first().capacity
        show.totalSeats =capacity
        show.seatsSold =0
        image.save(f"{UPLOAD_FOLDER+'/'+image.filename}")
        try:
            db.session.add(show)
            db.session.commit()
            resp= jsonify({
                "message":"show added sucess"
            })
            resp.status_code=201
            return resp
        except Exception as e:
            resp= jsonify({
                "error":"e"
            })
            resp.status_code=500


class EditShow(Resource):
    @jwt_required()
    def post(self, id,movie_id):
        role = get_jwt().get("role")
        if role != "admin":
            return abort(401,message="Unauthorized")
        theatre_exists = Theatre.query.filter_by(id=id).first()
        if not theatre_exists:
            return abort(404,message="theatre doesnt exists")
        movie = Movie.query.filter_by(id=movie_id).first()
        if not movie:
            return abort(404,message="movie doesnt exists")
        if request.content_type == 'application/json':
            args = request.json
            showName = args["showName"]
            rating = args["rating"]
            startTime = args["startTime"]
            endTime = args["endTime"]
            tags = args["tags"]
            ticketPrice = args["ticketPrice"]

            if showName is None or showName == '':
                return abort(401,message="showname is empty")
            if rating is None or rating == '':
                return abort(401,message="rating is empty")
            if ticketPrice is None or ticketPrice == '':
                return abort(401,message="ticketprice is empty")
            if tags is None or tags == '':
                return abort(401,message="tags is empty")
            if startTime is None or startTime == '':
                return abort(401,message="startime is empty")
            if endTime is None or endTime == '':
                return abort(401,message="endtime is empty")
            start =datetime.strptime(startTime, "%Y-%m-%dT%H:%M")
            end = datetime.strptime(endTime,"%Y-%m-%dT%H:%M")

            
            movie.tags = tags
            movie.endTime = end
            movie.startTime = start
            movie.rating = rating
            movie.name = showName
            try:
                db.session.commit()
                resp= jsonify({
                    "message":"show update sucess"
                })
                resp.status_code=201
                return resp
            except Exception as e:
                resp= jsonify({
                    "error":e.name
                })
                resp.status_code=500
                return resp



        args = request.form
        showName = args["showName"]
        rating = args["rating"]
        startTime = args["startTime"]
        endTime = args["endTime"]
        tags = args["tags"]
        ticketPrice = args["ticketPrice"]
        image = request.files["image"]
        if showName is None or showName == '':
            return abort(401,message="showname is empty")
        if rating is None or rating == '':
            return abort(401,message="rating is empty")
        if ticketPrice is None or ticketPrice == '':
            return abort(401,message="ticketprice is empty")
        if tags is None or tags == '':
            return abort(401,message="tags is empty")
        if startTime is None or startTime == '':
            return abort(401,message="startime is empty")
        if endTime is None or endTime == '':
            return abort(401,message="endtime is empty")
        start =datetime.strptime(startTime, "%Y-%m-%dT%H:%M")
        end = datetime.strptime(endTime,"%Y-%m-%dT%H:%M")
    
        image.save(f"{UPLOAD_FOLDER+'/'+image.filename}")
        if(os.path.exists(movie.image)):
            os.remove(movie.image)
        movie.tags = tags
        movie.endTime = end
        movie.startTime = start
        movie.rating = rating
        movie.name = showName
        movie.image=f"{UPLOAD_FOLDER+'/'+image.filename}"
        image.save(f"{UPLOAD_FOLDER+'/'+image.filename}")

        try:
            db.session.commit()
            resp= jsonify({
                "message":"show added sucess"
            })
            resp.status_code=201
            return resp
        except Exception as e:
            resp= jsonify({
                "error":e.name
            })
            resp.status_code=500


class GetVenues(Resource):
    @jwt_required()
    def get(self):

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
                    f.append({
                        "movie_id":d.id,
                        "movie_name":d.name
                    })
                c["movies"] = f
            serialized_venues.append(c)
        response = jsonify({
            "venues":serialized_venues
        })
        response.status_code=200
        return response

class CreateVenue(Resource):
    @jwt_required()
    def post(self):
        name = request.json["name"]
        capacity = request.json["capacity"]
        place = request.json["place"]
        location = request.json["location"]
        if (not name):
            return abort(422, message="name is empty")
        if (not place):
            return abort(422, message="place is empty")
        if (not location):
            return abort(422,message="location is empty")
        if (not capacity):
            return abort(422, message="capacity is empty")
        check_venue = Theatre.query.filter_by(name=name).first()
        if check_venue:
            return abort(400,message="Venue is already present")
        venue = Theatre(name=name, place=place, locaton=location, capacity=capacity)

        db.session.add(venue)
        db.session.commit()
        resp= jsonify({
            "message": "venue added success"
        })
        resp.status_code=201
        return resp

