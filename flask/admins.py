from flask_restful import Resource, abort, reqparse
from flask import request, jsonify, json
from flask_jwt_extended import create_access_token, create_refresh_token, jwt_required,get_jwt,get_jwt_identity
from models import Admin, db, Theatre, Movie
from werkzeug.security import check_password_hash, generate_password_hash


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

        db.session.commit()
        resp = jsonify({
            "message":"sucess"
        })
        resp.status_code=200
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
        return jsonify({
            "s":startTime,
            "e":endTime
        })

        # show =  Movie(showName=showName,rating=rating,tags=tags.join(","),ticketPrice=ticketPrice)
        # try:
        #     db.session.add(show)
        #     db.session.commit()
        #     return jsonify({
        #         "message":"show added sucess"
        #     }), 201
        # except:
        #     return jsonify({
        #         "error":"ERROR COULDN'T PROCESS REQUEST"
        #     })

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
                        d.id,
                        d.name
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

