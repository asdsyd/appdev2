from celerytasks import celerytask
from models import db,User,Booking
from mailer import mail
from flask_mail import Message
from datetime import date,timedelta
import datetime

datetime=datetime.datetime


@celerytask.on_after_finalize.connect
def setup_periodic_task(sender,**kargs):
    sender.add_periodic_task(5.0,daily.s(),name="dail reminder")
    sender.add_periodic_task(1.0,puchi.s(),name="printer")

@celerytask.task()
def daily():
    all_users = User.query.all()
    da = date(day=datetime.now().day,year=datetime.now().year,month=datetime.now().month)
    yesterday = da - timedelta(days=1)
    for v in all_users:
        bookings =Booking.query.filter(Booking.userid==v.user_id,Booking.booking_time==yesterday).all()
        if bookings is None or bookings==[]:
            message = Message("daily reminder",sender="norepaly@gamil.com",recipients=[v.email])
            message.body = f"""hello {v.username} this is someone from ticketshow this is your daily reminder to book as you haven't booked anything
            
            so what are you waiting for grab your favourtie shows at reasonable price 
            """
            mail.send(message)

@celerytask.task()
def monthly():



@celerytask.task()
def puchi():
    print("a")
    return "A"


@celerytask.task()
def add(a,b):
    print(a+b)
    return a+b

