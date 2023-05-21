from flask import Flask
from flask_restful import Api,Resource
from flask_migrate import Migrate

from users import UserLogin, UserRegister
# from mail import mail
from models import db
from flask_jwt_extended import JWTManager,jwt_required,create_access_token
from flask_cors import CORS
from admins import AdminLogin, CreateVenue
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

# class Refresh(Resource):
#     @jwt_required(refresh=True)
#     def post(self):



# api.add_resource(Register, '/register')
api.add_resource(AdminLogin, '/admin/login')
api.add_resource(UserLogin, '/user/login')
api.add_resource(UserRegister, '/user/register')
api.add_resource(CreateVenue,'/admin/createVenue')
# api.add_resource(CreateVenue,'/admin/createVenue')
# api.add_resource(Refresh, '/refresh')

# api.add_resource(ProfileInfo, '/<username>/info')
# api.add_resource(SearchTheatre, '/search/<query>')


# api.add_resource(UserExport, '/user/export')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000, debug=True)