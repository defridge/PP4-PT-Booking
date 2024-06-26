from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib import messages
from django.http import HttpResponseForbidden
from .forms import BookingForm
from .models import Booking
from django.utils import timezone


@login_required
def create_booking(request):
    """
    View to render the booking form
    and redirct users to booking
    success if form is valid
    """
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
    """
    View to render manage bookings page
    """
    bookings = Booking.objects.filter(user=request.user)
    return render(
        request, 'bookings/manage_bookings.html', {'bookings': bookings})


@login_required
def booking_success(request):
    """
    View to render booking success page
    """
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
    return render(
        request, 'bookings/delete_booking.html', {'booking': booking})


def custom_login_required_view(view_func):
    def wrapper(request, *args, **kwargs):
        if not request.user.is_authenticated:
            messages.info(request, 'Please sign in to access this page.')
            return HttpResponseForbidden()
        return view_func(request, *args, **kwargs)
    return wrapper


create_booking = custom_login_required_view(create_booking)
manage_bookings = custom_login_required_view(manage_bookings)
edit_booking = custom_login_required_view(edit_booking)
delete_booking = custom_login_required_view(delete_booking)


# Check if user is staff
def is_staff(user):
    return user.is_staff


@login_required
@user_passes_test(is_staff)
def manage_client_bookings(request):
    today = timezone.now().date()
    bookings = Booking.objects.filter(date__gte=today).order_by('date', 'time')
    if not request.user.is_staff:
        return HttpResponseForbidden()
    return render(
        request, 'bookings/manage_client_bookings.html',
        {'bookings': bookings})


@login_required
@user_passes_test(is_staff)
def edit_client_booking(request, booking_id):
    booking = get_object_or_404(Booking, id=booking_id)
    if request.method == 'POST':
        form = BookingForm(request.POST, instance=booking)
        if form.is_valid():
            form.save()
            return redirect('manage_client_bookings')
    else:
        form = BookingForm(instance=booking)
    return render(request, 'bookings/edit_client_booking.html', {'form': form})


@login_required
@user_passes_test(is_staff)
def delete_client_booking(request, booking_id):
    booking = get_object_or_404(Booking, id=booking_id)
    if request.method == 'POST':
        booking.delete()
        return redirect('manage_client_bookings')
    return render(
        request, 'bookings/delete_client_booking.html', {'booking': booking})
