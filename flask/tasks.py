from flask import render_template
from celerytasks import celerytask
from models import UserRating, db,User,Booking
from mailer import mail
from flask_mail import Message
from datetime import date,timedelta
import datetime

datetime=datetime.datetime


@celerytask.on_after_finalize.connect
def setup_periodic_task(sender,**kargs):
    sender.add_periodic_task(5.0,daily.s(),name="daily reminder")
    sender.add_periodic_task(15.0,monthly.s(),name="monthly reminder")
    sender.add_periodic_task(5.0,puchi.s(),name="printer")

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
    return "sent daily reminder to all"

@celerytask.task()
def monthly():
        all_users = User.query.all()
        for x in all_users:
            id = x.user_id
            bookings=[]
            today = datetime.now()
            one_month =  datetime.now()-timedelta(days=30)
            userratings = x.ratings
            usermontlyRatings = []
            all_bookings = Booking.query.filter(Booking.booking_time.between(one_month, today),Booking.userid==id).all()
            for v in all_bookings:
                bookings.append([v.movie.name,v.booking_time,v.numberSeats])
                for ff in userratings:
                    if ff.movie == v.movie.name:
                        usermontlyRatings.append([ff.movie,ff.rating])            
            html = render_template('sender.html',bookings=bookings,ratings=usermontlyRatings,username=x.username)
            msg = Message("infotainment report",recipients=[x.email])
            msg.attach("report.html", "text/html", html)
            mail.send(msg)
        return "sent montly reminder to all users"
        

@celerytask.task()
def puchi():
    print("a")
    return "A"


# @celerytask.task()
# def csv_exporter():


