from django.shortcuts import render, redirect
from .forms import BookingForm
from django.contrib.auth.decorators import login_required

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
def booking_success(request):
    return render(request, 'bookings/success.html')
