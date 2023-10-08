from django.shortcuts import render, redirect
from .models import Booking, Seat

def reset_db(request):
    Seat.objects.all().delete()
    Booking.objects.all().delete()

    return redirect('/unstop/book-tickets')

def get_current_seat_status():
    return Seat.objects.all()

def populate_seats():
    if len(Seat.objects.all()) == 80: return
    seats = []
    for i in range(1, 81):
        new_seat = Seat()
        new_seat.seat_number = i
        new_seat.status = 'a'
        seats.append(new_seat)
    Seat.objects.bulk_create(seats)

    for seat in Seat.objects.all():
        print(seat.seat_number, seat.status)


def book_tickets(request):
    total_seats = 80
    template_name = "book_tickets.html"
    context = {}

    if request.method == 'GET':
        context['current_seat_status'] = get_current_seat_status()
        return render(request, template_name, context)
    else:
        # initialize error
        error = None

        # read input
        if request.POST['tickets_booked'] and (request.POST['tickets_booked']).isnumeric():
            tickets_booked = int(request.POST['tickets_booked'])
            
            # input validation
            if tickets_booked > 7 or tickets_booked < 1:
                context['error'] = f'Invalid ticket count {tickets_booked}'
                context['current_seat_status'] = get_current_seat_status()
                return render(request, template_name, context)
            
            # last booking details
            last_booking = Booking.objects.last()

            if not last_booking:
                last_booked_seat_number = 0
            else:
                last_booked_seat_number = last_booking.last_booked_seat_no

            # validate if new booking is possible
            if total_seats - last_booked_seat_number < tickets_booked:
                context['error'] = 'Not enough seats left'
                context['current_seat_status'] = get_current_seat_status()
                return render(request, template_name, context)


            # book requested seats
            # all seats
            populate_seats()

            new_seats = []
            for i in range(last_booked_seat_number+1, last_booked_seat_number+tickets_booked+1):
                seat = Seat.objects.filter(seat_number=i)[0]
                seat.seat_number = i
                seat.status = 'b'
                new_seats.append(seat)
            
            Seat.objects.bulk_update(new_seats, ['status'])

            # create a new booking entry in db
            new_booking = Booking()
            new_booking.last_booked_seat_no = last_booked_seat_number + tickets_booked
            new_booking.save()

            # process ticket booking)
            context['tickets_booked'] = tickets_booked
            context['current_seat_status'] = get_current_seat_status()
            context['error'] = error
        else:
            error = 'please provide a valid ticket count to book tickets'
            context['current_seat_status'] = get_current_seat_status()
            context['error'] = error
        
        return render(request, template_name, context)
