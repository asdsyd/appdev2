from flask_restful import Resource, abort, reqparse
from flask import request, jsonify, json
from flask_jwt_extended import create_access_token, create_refresh_token, jwt_required
from models import Admin, db, Theatre, Movie
from werkzeug.security import check_password_hash, generate_password_hash


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
            accessToken = create_access_token(identity=username)
            refresh_token = create_refresh_token(identity=username)

            response = jsonify({
                'message': 'Admin logged in successfully!',
                "accessToken": accessToken,
                "refresh_token": refresh_token,
                "username": username,
            })
            response.status_code = 200
            return response


# class CreateShow(Resource):
    # @jwt_required()
#     def post(self, venue):
#         req = reqparse.RequestParser()
#         req.add_argument("showName", type=str, required=True, help="Show Name is required")
#         req.add_argument("rating", type=int, required=True, help="Rating is required")
#         req.add_argument("startTime", type=str, required=True, help="Start time is required")
#         req.add_argument("endTime", type=str, required=True, help="End time is required")
#         req.add_argument("tags", type=str, required=True, help="Tag(s) is/are required")
#         req.add_argument("ticketPrice", type=str, required=True, help="Ticket Price is required")
#         args = req.parse_args()
#
#         showName = args["showName"]
#         rating = args["rating"]
#         startTime = args["startTime"]
#         endTime = args["endTime"]
#         tags = args["tags"]
#         ticketPrice = args["ticketPrice"]
#         show =  Movie(showshowName,rating,tags,ticketPrice,startTime,endTime)
#         try:
#             db.session.add(show)
#             db.session.commit()
#             return jsonify({
#                 "message":"show added sucess"
#             }), 201
#         except:
#             return jsonify({
#                 "error":"ERROR COULDN'T PROCESS REQUEST"
#             })

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
        venue = Theatre(name=name, place=place, locaton=location, capacity=capacity)

        db.session.add(venue)
        db.session.commit()
        resp= jsonify({
            "message": "venue added success"
        })
        resp.status_code=201
        return resp

