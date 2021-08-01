from quiz_app.settings import BASE_DIR
from django.shortcuts import render
from django.http import HttpResponse
import os
from django.conf import settings
from .forms import ContactForm
from django.core.mail import send_mail


# Create your views here.


def about(request):
    return render(request, 'about.html')


def resume_download(request):
    with open(os.path.join(settings.MEDIA_ROOT, 'resume.pdf'), 'rb') as fh:
        response = HttpResponse(fh.read(), content_type="application/pdf")
        response['Content-Disposition'] = 'attachment; filename=resume.pdf'
        return response

def contact_view(request):
    form = ContactForm()
    if request.method == 'POST':
        form2 = ContactForm(request.POST)
        if form2.is_valid():
            form2.save()
            email_subject = f'New contact {form2.cleaned_data["email"]}: {form2.cleaned_data["subject"]}'
            email_message = form2.cleaned_data['message']
            send_mail(email_subject, email_message, settings.CONTACT_EMAIL, settings.ADMIN_EMAIL)
            messages = 'Your contact information and message was successfully submitted.'
            return render(request, 'contact.html', {'form' : form, 'messages' : messages})
    
    return render(request, 'contact.html', {'form': form})
