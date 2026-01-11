from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import TripBookingForm, ContactForm
from .models import Contact, TripBooking

# HOME PAGE
def home(request):
    return render(request, 'index.html')


# CONTACT PAGE
def contact_view(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            return render(
                request,
                'contact.html',
                {'form': ContactForm(), 'success': True}
            )
    else:
        form = ContactForm()

    return render(request, 'contact.html', {'form': form})


# SERVICES / TRIP BOOKING PAGE
def Services(request):
    if request.method == 'POST':
        form = TripBookingForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your trip has been booked successfully!')
            return redirect('/Services/#book-trip')
    else:
        form = TripBookingForm()

    return render(request, 'Services.html', {'form': form})

from openai import OpenAI, RateLimitError
from django.conf import settings

client = OpenAI(api_key=settings.OPENAI_API_KEY)


def mock_ai_trip(destination, budget, days):
    return (
        f"Trip Plan for {destination} ({days} days)\n\n"
        "- Stay in budget hotels or hostels\n"
        "- Use public transport\n"
        "- Visit 2 major attractions per day\n"
        "- Allocate daily food budget carefully\n\n"
        "Note: This is a demo AI response."
    )


def ai_planner(request):
    if request.method == 'POST':
        destination = request.POST.get('destination')
        budget = request.POST.get('budget')
        days = request.POST.get('days')

        # 🔁 AI TOGGLE
        if settings.AI_ON:
            try:
                prompt = f"""
                Create a detailed trip plan.
                Destination: {destination}
                Budget: {budget} INR
                Duration: {days} days
                """

                response = client.chat.completions.create(
                    model="gpt-4o-mini",
                    messages=[
                        {"role": "system", "content": "You are a travel planner."},
                        {"role": "user", "content": prompt}
                    ],
                    max_tokens=400
                )

                suggestion = response.choices[0].message.content

            except RateLimitError:
                suggestion = mock_ai_trip(destination, budget, days)

        else:
            # ❌ REAL AI OFF → DEMO MODE
            suggestion = mock_ai_trip(destination, budget, days)

        return render(
            request,
            'ai_result.html',
            {
                'destination': destination,
                'budget': budget,
                'days': days,
                'suggestion': suggestion
            }
        )

    return render(request, 'ai_planner.html')
