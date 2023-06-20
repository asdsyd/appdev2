import csv
from flask import render_template
from celery.schedules import crontab
from celerytasks import celerytask
from models import Theatre, UserRating, db,User,Booking
from mailer import mail
from flask_mail import Message
from datetime import date,timedelta
import datetime

datetime=datetime.datetime


@celerytask.on_after_finalize.connect
def setup_periodic_task(sender,**kargs):
    sender.add_periodic_task(crontab(minute=0, hour='19', day_of_week='*'),daily.s(),name="daily reminder")
    sender.add_periodic_task(crontab(minute=0, hour=0, day_of_month=1),monthly.s(),name="monthly reminder")
    sender.add_periodic_task(crontab(hour=1),puchi.s(),name="printer")

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
    print("printer")
    return "i am a printer"


@celerytask.task()
def csv_exporter(id,email):
        venue = Theatre.query.filter_by(id=id).first()
        serial_venue = []
        for mov in venue.movies:
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
            serial_venue.append(on_movie)
            
        try:
            with open('export.csv','w+') as csvs:
                csvwriter = csv.writer(csvs)
                csvwriter.writerow(["Theatre name",venue.name])
                csvwriter.writerow(["Theatre capacity",venue.capacity])
                csvwriter.writerow(["Theatre location",venue.locaton])
                csvwriter.writerow(["Theatre place",venue.place])
                csvwriter.writerow(["movies:-"])
                csvwriter.writerow([])
                csvwriter.writerow(["movie name","movie bookings"])
                for c in serial_venue:
                        csvwriter.writerow([c["name"],c["bookings"]])
            msg = Message("csv gen is completed",sender=["aaaa@gmail.com"],recipients=[email])
            msg.body = f"the csv for theatre {venue.name} and id  {id} is done now u can export it"
            mail.send(msg)
            return "done"
        except Exception as e:
            return "error"


