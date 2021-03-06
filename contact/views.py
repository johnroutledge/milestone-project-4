from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse
from django.shortcuts import render, redirect, reverse
from django.conf import settings
from django.contrib import messages
from django.template.loader import render_to_string

from profiles.models import UserProfile

from .forms import ContactForm


def contact(request):
    """View to return our contact page with the contact form"""
    if request.method == 'GET':
        if request.user.is_authenticated:
            try:
                profile = UserProfile.objects.get(user=request.user)
                contact_form = ContactForm(initial={
                    'email': profile.user.email,
                }
                )
            except UserProfile.DoesNotExist:
                contact_form = ContactForm()
        else:
            contact_form = ContactForm()
    else:
        contact_form = ContactForm(request.POST)
        if contact_form.is_valid():
            first_name = contact_form.cleaned_data['first_name']
            last_name = contact_form.cleaned_data['last_name']
            email = contact_form.cleaned_data['email']
            subject = contact_form.cleaned_data['subject']
            message = contact_form.cleaned_data['message']
            html_msg = render_to_string(
                'emails/contact_email.html',
                {
                    'first_name': first_name,
                    'last_name': last_name,
                    'subject': subject,
                    'message': message,
                    'email': email
                })
            try:
                send_mail(subject, message, settings.EMAIL_HOST_USER, [
                    email, settings.EMAIL_HOST_USER],
                    html_message=html_msg, fail_silently=False)

            except BadHeaderError:
                return HttpResponse('Invalid header found.')
            return redirect(reverse('home'),
                            messages.success(request, 'Thank you for \
                                            your message, a copy of which\
                                            has been emailed to you. We will\
                                            get in touch with you as soon\
                                            as possible.'))

    template = 'contact/contact.html'
    context = {
        'contact_form': contact_form,
    }

    return render(request, template, context)
