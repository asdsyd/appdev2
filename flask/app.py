from flask import Flask,jsonify
from flask_restful import Api,Resource,abort
from flask_migrate import Migrate

from users import UserLogin, UserRegister,UserCheck
# from mail import mail
from models import db
from flask_jwt_extended import JWTManager,jwt_required,create_access_token,get_jwt_identity,get_jwt
from flask_cors import CORS
from admins import AdminLogin, CreateVenue,AdminCheck,GetVenues,GetVenueData,EditVenue
# from workers import celery_app
# from cache import cache


# class ContextTask(celery_app.Task):
#     def __call__(self, *args, **kwargs):
#         with app.app_context():
#             return self.run(*args, **kwargs)
#
app, api,  = None, None

def create_app():

    app = Flask(__name__)
    app.config.from_object('config')

    api = Api(app)
    # mail.init_app(app)
    jwt = JWTManager(app)
    app.app_context().push()

    CORS(app, resources={r'/*': {'origins': '*'}})
    # cache.init_app(app)
    db.init_app(app)
    with app.app_context():
        db.create_all()
    migrate = Migrate(app, db)
    app.app_context().push()

    # celery_app.conf.update(
    #     broker_url = app.config['CELERY_BROKER_URL'],
    #     result_backend = app.config['CELERY_RESULT_BACKEND'],
    #     timezone = app.config['CELERY_TIMEZONE']
    # )
    # celery_app.Task = ContextTask
    app.app_context().push()

    return app, api

app, api = create_app()

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

# api.add_resource(Register, '/register')
api.add_resource(AdminLogin, '/admin/login')
api.add_resource(UserLogin, '/user/login')
api.add_resource(UserCheck,'/check')
api.add_resource(AdminCheck,'/admin/check')
api.add_resource(UserRegister, '/user/register')
api.add_resource(CreateVenue,'/admin/createVenue')
api.add_resource(GetVenues,'/admin/getVenues')
api.add_resource(GetVenueData,'/admin/<int:id>/getVenuedata')
api.add_resource(AdminRefresh,'/admin/refresh')
api.add_resource(UserRefresh,'/user/refresh')
api.add_resource(EditVenue,'/admin/<int:id>/editVenue')

# api.add_resource(CreateVenue,'/admin/createVenue')
# api.add_resource(Refresh, '/refresh')

# api.add_resource(ProfileInfo, '/<username>/info')
# api.add_resource(SearchTheatre, '/search/<query>')


# api.add_resource(UserExport, '/user/export')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000, debug=True)