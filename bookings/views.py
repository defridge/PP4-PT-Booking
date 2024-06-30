from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib import messages
from django.utils import timezone
from .forms import BookingForm
from .models import Booking


@login_required
def create_booking(request):
    """
    Render the booking form and handle form submission.

    If the form is valid, create a new booking
    associated with the logged-in user
    and redirect to the booking success page.
    Otherwise, re-render the form with errors.

    Args:
        request (HttpRequest): The HTTP request object.

    Returns:
        HttpResponse: The rendered booking form
        or a redirect to the booking success page.
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
    Render the manage bookings page showing the user's future bookings.

    Args:
        request (HttpRequest): The HTTP request object.

    Returns:
        HttpResponse: The rendered manage bookings page.
    """
    today = timezone.now().date()
    bookings = Booking.objects.filter(user=request.user, date__gte=today)
    return render(
        request, 'bookings/manage_bookings.html', {'bookings': bookings})


@login_required
def booking_success(request):
    """
    Render the booking success page.

    Args:
        request (HttpRequest): The HTTP request object.

    Returns:
        HttpResponse: The rendered booking success page.
    """
    return render(request, 'bookings/booking_success.html')


@login_required
def edit_booking(request, booking_id):
    """
    Render the edit booking form and handle form submission.

    If the form is valid, update the existing
    booking and redirect to manage bookings page.
    Otherwise, re-render the form with errors.

    Args:
        request (HttpRequest): The HTTP request object.
        booking_id (int): The ID of the booking to edit.

    Returns:
        HttpResponse: The rendered edit booking
        form or a redirect to manage bookings page.
    """
    booking = get_object_or_404(Booking, id=booking_id, user=request.user)
    if request.method == 'POST':
        form = BookingForm(
            request.POST, instance=booking, current_booking=booking)
        if form.is_valid():
            form.save()
            return redirect('manage_bookings')
    else:
        form = BookingForm(instance=booking, current_booking=booking)
    return render(request, 'bookings/edit_booking.html', {'form': form})


@login_required
def delete_booking(request, booking_id):
    """
    Render the delete booking confirmation and handle form submission.

    If confirmed, delete the booking and redirect to manage bookings page.

    Args:
        request (HttpRequest): The HTTP request object.
        booking_id (int): The ID of the booking to delete.

    Returns:
        HttpResponse: The rendered delete booking
        confirmation or a redirect to manage bookings page.
    """
    booking = get_object_or_404(Booking, id=booking_id, user=request.user)
    if request.method == 'POST':
        booking.delete()
        return redirect('manage_bookings')
    return render(
        request, 'bookings/delete_booking.html', {'booking': booking})


def custom_login_required_view(view_func):
    """
    Decorator to require login for a view
    and display a message if not authenticated.

    Args:
        view_func (function): The view function to wrap.

    Returns:
        function: The wrapped view function.
    """
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


def is_staff(user):
    """
    Check if a user is a staff member.

    Args:
        user (User): The user to check.

    Returns:
        bool: True if the user is a staff member, False otherwise.
    """
    return user.is_staff


@login_required
@user_passes_test(is_staff)
def manage_client_bookings(request):
    """
    Render the manage client bookings page showing all future bookings.

    Args:
        request (HttpRequest): The HTTP request object.

    Returns:
        HttpResponse: The rendered manage client bookings page.
    """
    today = timezone.now().date()
    bookings = Booking.objects.filter(date__gte=today).order_by('date', 'time')
    return render(
        request, 'bookings/manage_client_bookings.html',
        {'bookings': bookings})


@login_required
@user_passes_test(is_staff)
def edit_client_booking(request, booking_id):
    """
    Render the edit client booking form and handle form submission.

    If the form is valid, update the existing booking
    and redirect to manage client bookings page.
    Otherwise, re-render the form with errors.

    Args:
        request (HttpRequest): The HTTP request object.
        booking_id (int): The ID of the booking to edit.

    Returns:
        HttpResponse: The rendered edit client booking
        form or a redirect to manage client bookings page.
    """
    booking = get_object_or_404(Booking, id=booking_id)
    if request.method == 'POST':
        form = BookingForm(
            request.POST, instance=booking, current_booking=booking)
        if form.is_valid():
            form.save()
            return redirect('manage_client_bookings')
    else:
        form = BookingForm(instance=booking, current_booking=booking)
    return render(request, 'bookings/edit_client_booking.html', {'form': form})


@login_required
@user_passes_test(is_staff)
def delete_client_booking(request, booking_id):
    """
    Render the delete client booking confirmation and handle form submission.

    If confirmed, delete the booking and
    redirect to manage client bookings page.

    Args:
        request (HttpRequest): The HTTP request object.
        booking_id (int): The ID of the booking to delete.

    Returns:
        HttpResponse: The rendered delete client booking
        confirmation or a redirect to manage client bookings page.
    """
    booking = get_object_or_404(Booking, id=booking_id)
    if request.method == 'POST':
        booking.delete()
        return redirect('manage_client_bookings')
    return render(
        request, 'bookings/delete_client_booking.html', {'booking': booking})
