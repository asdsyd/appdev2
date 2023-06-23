import os
from flask import Flask,jsonify, send_file,send_from_directory,request,render_template
from flask_restful import Api,Resource,abort
from flask_migrate import Migrate
import tasks
from users import UserLogin, UserRegister,UserCheck,GetUserVenues,GetUserShow,BookingShow,getBookings,getUser,Rate,SearchMovie,ChangePass,GetUservenueData,UpdateProfile
from mailer import mail
from flask_mail import Message
from models import Admin, Booking, Theatre, db,User
from flask_jwt_extended import JWTManager,jwt_required,create_access_token,get_jwt_identity,get_jwt
from flask_cors import CORS
from admins import AdminLogin, CreateVenue,AdminCheck,GetVenues,GetVenueData,EditVenue,CreateShow,DeleteVenue,EditShow,DeleteShow,GetShow, AdminRegister
from celerytasks import celerytask
from rediscache import cache
import csv

class ContextTask(celerytask.Task):
    def __call__(self, *args, **kwargs):
        with app.app_context():
            return self.run(*args, **kwargs)

app, api,mailer,celery = None, None,None,None

def create_app():

    app = Flask(__name__)
    app.config.from_object('config')
    api = Api(app)
    mail.init_app(app)
    jwt = JWTManager(app)
    app.app_context().push()

    CORS(app, resources={r'/*': {'origins': '*'}})
    cache.init_app(app)
    db.init_app(app)
    with app.app_context():
        db.create_all()
    migrate = Migrate(app,db,render_as_batch=True)
    app.app_context().push()
    celery = celerytask

    celery.conf.update(
        broker_url = app.config['CELERY_BROKER_URL'],
        result_backend = app.config['CELERY_RESULT_BACKEND'],
        timezone = app.config['CELERY_TIMEZONE']
    )
    celery.Task = ContextTask
    

    return app, api,mail,celery

app, api,mailer,celery = create_app()

class AdminRefresh(Resource):
    @jwt_required(refresh=True)
    def post(self):
        identity =get_jwt_identity()
        role = get_jwt().get("role")
        print(role)
        if role != "admin":
            return jsonify({"msg":"Unauthorzied"}),401
        acess = create_access_token(identity,additional_claims={"role":"admin"})
        resp = jsonify({
            "message":"success",
            "access_token":acess,
            "username":identity
        })
        resp.status_code=200
        return resp

class GetImage(Resource):
    def get(self,image):
        return send_from_directory(app.config["UPLOAD_FOLDER"],image)

class GetProfileImage(Resource):
        def get(self,image):
            return send_from_directory(app.config["USER_UPLOAD_FOLDER"],image)


class UserRefresh(Resource):
    @jwt_required(refresh=True)
    def post(self):
        identity =get_jwt_identity()
        role = get_jwt().get("role")
        if role !="user":
            return jsonify({"msg":"Unauthorzied"}),401
        access = create_access_token(identity,additional_claims={"role":"user"})
        resp = jsonify({
            "access_token":access,
            "username":identity
        })
        resp.status_code=200
        return resp



class csvWriter(Resource):
    @jwt_required()
    def get(self,th_id):
        identity =get_jwt_identity()
        role = get_jwt().get("role")
        print(role)
        if role != "admin":
            return jsonify({"msg":"Unauthorzied"}),401
        email = Admin.query.filter_by(username=identity).first().email
        id = tasks.csv_exporter.apply_async(args=[th_id,email])
        return jsonify({
            "id":id.id
        })
        


class getCsvResult(Resource):
    @jwt_required()
    def get(self,task_id):
        role = get_jwt().get("role")
        if role != "admin":
            return jsonify({"msg":"Unauthorzied"}),401
        result = tasks.csv_exporter.AsyncResult(task_id)

        if result.ready():
            file_path = 'export.csv'
            try:
                return send_file(file_path)
            finally:
                if os.path.exists(file_path):
                    os.remove(file_path)
        else:
            resp = jsonify({"status":"workig"})
            resp.status_code = 102
            return resp

    
        
        


class SendSummary(Resource):
    @jwt_required()
    def get(self):
    
        role = get_jwt().get("role")
        print(role)
        if role != "admin":
            return jsonify({"msg":"Unauthorzied"}),401
        venues = Theatre.query.all()
        serial_venue = []
        for v  in venues:
            venu = {
                "id":v.id,
                "name":v.name,
                "movies":[]
            }
            for mov in v.movies:
                on_movie = {
                    "name":mov.name,
                    "bookings":0
                }
                bookings_movie = Booking.query.filter_by(movie_id=mov.id)
                for bookinggss in bookings_movie:
                    if on_movie.get("bookings"):
                        on_movie["bookings"]+=1
                    else:
                        on_movie["bookings"]=1
                venu["movies"].append(on_movie)
            serial_venue.append(venu)
        resp = jsonify({
            "data":serial_venue
        })
        resp.status_code=200
        return resp




# api.add_resource(Register, '/register')
api.add_resource(AdminLogin, '/admin/login')
api.add_resource(UserLogin, '/user/login')
api.add_resource(UserCheck,'/check')
api.add_resource(AdminCheck,'/admin/check')
api.add_resource(UserRegister, '/user/register')
api.add_resource(CreateVenue,'/admin/createVenue')
api.add_resource(GetVenues,'/admin/getVenues')
api.add_resource(GetVenueData,'/admin/<string:id>/getVenuedata')
api.add_resource(AdminRefresh,'/admin/refresh')
api.add_resource(UserRefresh,'/user/refresh')
api.add_resource(EditVenue,'/admin/<string:id>/editVenue')
api.add_resource(CreateShow,'/admin/<string:id>/CreateShow')
api.add_resource(DeleteVenue,'/admin/<string:id>/deleteVenue')
api.add_resource(GetUserVenues,'/user/getVenues')
api.add_resource(DeleteShow,'/admin/<string:id>/<string:movie_id>/deleteShow')
api.add_resource(GetShow,'/admin/<string:movie_id>/getShow')
api.add_resource(EditShow,'/admin/<string:id>/<string:movie_id>/EditShow')
api.add_resource(GetImage,'/image/<string:image>')
api.add_resource(GetProfileImage,'/profile_image/<string:image>')
api.add_resource(AdminRegister, '/admin/register')
api.add_resource(GetUserShow,'/user/<string:movie_id>/getShow')
api.add_resource(BookingShow,'/user/<string:th_id>/<string:movie_id>/book')
api.add_resource(getBookings,'/user/bookings')
api.add_resource(getUser,'/user/getuser')
api.add_resource(Rate,'/user/<string:movie_id>/rating')
api.add_resource(SearchMovie,"/sear/<string:search>")
api.add_resource(ChangePass,'/user/passchange')
api.add_resource(UpdateProfile,'/user/updateprofile')
api.add_resource(GetUservenueData,'/user/<string:id>/getvenue')
api.add_resource(SendSummary,'/admin/summary')
api.add_resource(csvWriter,'/admin/export/<string:th_id>')
api.add_resource(getCsvResult,'/admin/export/results/<string:task_id>')



if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000, debug=True)