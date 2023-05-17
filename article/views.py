from django.shortcuts import render
from .forms import SendMailMessageForm


from django.core.mail import send_mail
from django.conf import settings

# Formun işlendiği view işlevinde
def my_view(request):
    if request.method == 'POST':
        form = SendMailMessageForm(request.POST)
        if form.is_valid():
            form.save()

            # Yanıt e-postasını gönder
            subject = 'Thank you for your message'
            message = 'We have received your message and will get back to you shortly.'
            from_email = settings.DEFAULT_FROM_EMAIL
            recipient_list = [form.cleaned_data['mail_address']]
            send_mail(subject, message, from_email, recipient_list)

    else:
        form = SendMailMessageForm()

    context = {
        'form': form,
    }
    return render(request, 'contact.html', context)
