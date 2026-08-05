from django.shortcuts import render, redirect
from django.http import JsonResponse, HttpResponseBadRequest
from django.core.mail import EmailMessage
from django.views.decorators.http import require_http_methods
from .models import UserRegistration, AlertHistory
import json

def home(request):
    return render(request, 'core/home.html')

def register(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        phone = request.POST.get('phone')
        email1 = request.POST.get('email1')
        email2 = request.POST.get('email2')
        email3 = request.POST.get('email3')
        # Basic validation
        if not name or not email1:
            return render(request, 'core/register.html', {'error': 'Name and primary email are required.'})
        UserRegistration.objects.create(
            name=name, phone=phone, email1=email1, email2=email2, email3=email3
        )
        return redirect('core:home')
    return render(request, 'core/register.html')

def about(request):
    return render(request, 'core/about.html')

def history(request):
    alerts = AlertHistory.objects.select_related('user').order_by('-created_at')
    return render(request, 'core/history.html', {'alerts': alerts})

# GET => render page
def send_alert_page(request):
    users = UserRegistration.objects.order_by('-created_at')
    return render(request, 'core/send_alert.html', {'users': users})

# POST JSON => send email and save history
@require_http_methods(["POST"])
def send_alert_api(request):
    try:
        data = json.loads(request.body)
    except json.JSONDecodeError:
        return HttpResponseBadRequest('Invalid JSON')

    user_id = data.get('user_id')
    message = data.get('message', 'I need help. Please reach out!')
    lat = data.get('lat')
    lng = data.get('lng')

    try:
        user = UserRegistration.objects.get(id=user_id)
    except (UserRegistration.DoesNotExist, TypeError):
        return JsonResponse({'ok': False, 'error': 'User not found'}, status=404)

    location_link = ''
    if lat is not None and lng is not None:
        location_link = f'https://maps.google.com/?q={lat},{lng}'

    # Compose email
    email_body = f"Emergency Alert!\n\nUser: {user.name}\nMessage: {message}\n"
    if location_link:
        email_body += f"Live Location: {location_link}\n"

    recipients = [e for e in [user.email1, user.email2, user.email3] if e]

    if not recipients:
        return JsonResponse({'ok': False, 'error': 'No recipient emails found for user.'}, status=400)

    try:
        email = EmailMessage(subject='Emergency Alert', body=email_body, to=recipients)
        email.send(fail_silently=False)
    except Exception as exc:
        return JsonResponse({'ok': False, 'error': str(exc)}, status=500)

    # Save history
    AlertHistory.objects.create(user=user, message=message, location_link=location_link)

    return JsonResponse({'ok': True})


# Create your views here.
