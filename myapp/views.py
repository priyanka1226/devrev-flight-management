from datetime import datetime
from django.contrib import messages
from django.shortcuts import render
from decimal import Decimal

from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from .models import User, Flight, Book
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from .forms import UserLoginForm, UserRegisterForm
from django.contrib.auth.decorators import login_required
from decimal import Decimal


def home(request):
    if request.user.is_authenticated:
        return render(request, 'myapp/home.html')
    else:
        return render(request, 'myapp/signin.html')


@login_required(login_url='signin')
def findflight(request):
    context = {}
    if request.method == 'POST':
        source_r = request.POST.get('source')
        dest_r = request.POST.get('destination')
        date_r = request.POST.get('date')
        date_r = datetime.strptime(date_r,"%Y-%m-%d").date()
        year = date_r.strftime("%Y")
        month = date_r.strftime("%m")
        day = date_r.strftime("%d")
        flight_list = Flight.objects.filter(source=source_r, dest=dest_r, date__year=year, date__month=month, date__day=day)
        if flight_list:
            return render(request, 'myapp/list.html', locals())
        else:
            context['data'] = request.POST
            context["error"] = "No available Flight Schedule for entered Route and Date"
            return render(request, 'myapp/findflight.html', context)
    else:
        return render(request, 'myapp/findflight.html')


@login_required(login_url='signin')
def bookings(request):
    context = {}
    if request.method == 'POST':
        id_r = request.POST.get('flight_id')
        seats_r = int(request.POST.get('no_seats'))
        flight = Flight.objects.get(id=id_r)
        if flight:
            if flight.remaining_seats > int(seats_r):
                name_r = flight.flight_name
                cost = int(seats_r) * flight.price
                source_r = flight.source
                dest_r = flight.dest
                nos_r = Decimal(flight.no_of_seats)
                price_r = flight.price
                date_r = flight.date
                time_r = flight.time
                username_r = request.user.username
                email_r = request.user.email
                userid_r = request.user.id
                rem_r = flight.remaining_seats - seats_r
                Flight.objects.filter(id=id_r).update(remaining_seats=rem_r)
                book = Book.objects.create(name=username_r, email=email_r, userid=userid_r, flight_name=name_r,
                                           source=source_r, flight_id=id_r,
                                           dest=dest_r, price=price_r, no_of_seats=seats_r, date=date_r, time=time_r,
                                           status='BOOKED')
                print('------------book id-----------', book.id)
                # book.save()
                return render(request, 'myapp/bookings.html', locals())
            else:
                context["error"] = "Sorry select fewer number of seats"
                return render(request, 'myapp/findflight.html', context)

    else:
        return render(request, 'myapp/findflight.html')


@login_required(login_url='signin')
def cancellings(request):
    context = {}
    if request.method == 'POST':
        id_r = request.POST.get('flight_id')
        #seats_r = int(request.POST.get('no_seats'))

        try:
            book = Book.objects.get(id=id_r)
            flight = Flight.objects.get(id=book.flight_id)
            rem_r = flight.remaining_seats + book.no_of_seats
            Flight.objects.filter(id=book.flight_id).update(remaining_seats=rem_r)
            #nos_r = book.no_of_seats - seats_r
            Book.objects.filter(id=id_r).update(status='CANCELLED')
            messages.success(request, "Booked Flight has been cancelled successfully.")
            return redirect(seebookings)
        except Book.DoesNotExist:
            context["error"] = "Sorry You have not booked that flight"
            return render(request, 'myapp/error.html', context)
    else:
        return render(request, 'myapp/findflight.html')


@login_required(login_url='signin')
def seebookings(request,new={}):
    context = {}
    id_r = request.user.id
    book_list = Book.objects.filter(userid=id_r)
    if book_list:
        return render(request, 'myapp/booklist.html', locals())
    else:
        context["error"] = "Sorry no flights booked"
        return render(request, 'myapp/findflight.html', context)


def signup(request):
    context = {}
    if request.method == 'POST':
        name_r = request.POST.get('name')
        email_r = request.POST.get('email')
        password_r = request.POST.get('password')
        user = User.objects.create_user(name_r, email_r, password_r, )
        if user:
            login(request, user)
            return render(request, 'myapp/thank.html')
        else:
            context["error"] = "Provide valid credentials"
            return render(request, 'myapp/signup.html', context)
    else:
        return render(request, 'myapp/signup.html', context)


def signin(request):
    context = {}
    if request.method == 'POST':
        name_r = request.POST.get('name')
        password_r = request.POST.get('password')
        user = authenticate(request, username=name_r, password=password_r)
        if user:
            login(request, user)
            # username = request.session['username']
            context["user"] = name_r
            context["id"] = request.user.id
            return render(request, 'myapp/success.html', context)
            # return HttpResponseRedirect('success')
        else:
            context["error"] = "Provide valid credentials"
            return render(request, 'myapp/signin.html', context)
    else:
        context["error"] = "You are not logged in"
        return render(request, 'myapp/signin.html', context)


def signout(request):
    context = {}
    logout(request)
    context['error'] = "You have been logged out"
    return render(request, 'myapp/signin.html', context)


def success(request):
    context = {}
    context['user'] = request.user
    return render(request, 'myapp/success.html', context)
