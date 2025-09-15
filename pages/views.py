# your_app/views.py

from django.shortcuts import render, redirect
from django.urls import reverse

# A simple in-memory list to act as our "database" for the guestbook.
# This list will be reset every time the server restarts.
guestbook_messages = []

def home(request):
    name = request.GET.get('name', 'Guest') 
    context = {
        'name': name
    }
    return render(request, 'home.html', context)

def about(request):
    return render(request, 'about.html')

def contact(request):
    # Handle the form submission
    if request.method == 'POST':
        message = request.POST.get('message', '')
        if message:
            # Store the submitted message
            guestbook_messages.append(message)
        # Redirect back to the same page to prevent form re-submission on refresh
        return redirect(reverse('contact'))

    # For a GET request, just display the page with existing messages
    context = {
        'messages': guestbook_messages
    }
    return render(request, 'contact.html', context)