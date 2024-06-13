from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import BookingForm
from .models import Booking


@login_required
def create_booking(request):
    if request.method == 'POST':
        form = BookingForm(request.POST)
        if form.is_valid():
            booking = form.save(commit=False)
            booking.user = request.user
            booking.save()
            return redirect('booking_success')
    else:
        form = BookingForm()
    return render(request, 'bookings/create_booking.html', {'form': form})


@login_required
def manage_bookings(request):
    bookings = Booking.objects.filter(user=request.user)
    return render(request, 'bookings/manage_bookings.html', {'bookings': bookings})


@login_required
def booking_success(request):
    return render(request, 'bookings/booking_success.html')


@login_required
def edit_booking(request, booking_id):
    booking = get_object_or_404(Booking, id=booking_id, user=request.user)
    if request.method == 'POST':
        form = BookingForm(request.POST, instance=booking)
        if form.is_valid():
            form.save()
            return redirect('manage_bookings')
    else:
        form = BookingForm(instance=booking)
    return render(request, 'bookings/edit_booking.html', {'form': form})


@login_required
def delete_booking(request, booking_id):
    booking = get_object_or_404(Booking, id=booking_id, user=request.user)
    if request.method == 'POST':
        booking.delete()
        return redirect('manage_bookings')
    return render(request, 'bookings/delete_booking.html', {'booking': booking})


def custom_login_required_view(view_func):
    def wrapper(request, *args, **kwargs):
        if not request.user.is_authenticated:
            messages.info(request, 'Please sign in to access this page.')
            return redirect('account_login')
        return view_func(request, *args, **kwargs)
    return wrapper

create_booking = custom_login_required_view(create_booking)
manage_bookings = custom_login_required_view(manage_bookings)
edit_booking = custom_login_required_view(edit_booking)
delete_booking = custom_login_required_view(delete_booking)