from django.shortcuts import HttpResponse
from django.shortcuts import render
from django.core.mail import send_mail
from django.conf import settings
from django.shortcuts import render


def Homepage(request):
    return render(request,"index.html")
def portfolio(request):
    return render(request,"portfolio.html")
def about(request):
    return render(request,"about.html")

# def Contact(request):
#     if request.method == "POST":
#         name = request.POST.get("name")
#         email = request.POST.get("email")
#         message = request.POST.get("message")

#         # Send email
#         send_mail(
#             subject=f"New Contact Form Submission from {name}",
#             message=message + f"\n\nSender Email: {email}",
#             from_email=settings.EMAIL_HOST_USER,  # your email
#             recipient_list=[settings.EMAIL_HOST_USER],  # where you receive mails
#             fail_silently=False,
#         )

#         return render(request, "Contact.html", {"success": True})

#     return render(request, "Contact.html")
# from .forms import ContactForm
# def Contact(request):
#     if request.method == "POST":
#         form = ContactForm(request.POST)
#         if form.is_valid():
#             name = form.cleaned_data['name']
#             email = form.cleaned_data['email']
#             message = form.cleaned_data['message']

#             # Send email
#             send_mail(
#                 subject=f"New Contact Form Submission from {name}",
#                 message=message + f"\n\nSender Email: {email}",
#                 from_email=settings.EMAIL_HOST_USER,
#                 recipient_list=[settings.EMAIL_HOST_USER],
#                 fail_silently=False,
#             )
#             return render(request, "Contact.html", {"success": True})
#     else:
#         form = ContactForm()

#     return render(request, "Contact.html", {'form': form})

# from django.shortcuts import render
# from django.core.mail import send_mail
# from django.conf import settings
# from .forms import ContactForm


# def portfolio(request):
#     if request.method == "POST":
#         form = ContactForm(request.POST)
#         if form.is_valid():
#             name = form.cleaned_data['name']
#             email = form.cleaned_data['email']
#             message = form.cleaned_data['message']

#             # Email content
#             subject = f"New Contact Form Submission from {name}"
#             body = f"""
#             You have received a new message:

#             From: {name}
#             Email: {email}

#             Message:
#             {message}
#             """

#             send_mail(
#                 subject=subject,
#                 message=body,
#                 from_email=settings.EMAIL_HOST_USER,
#                 recipient_list=[settings.EMAIL_HOST_USER],
#                 fail_silently=False,
#             )

#             # 👉 Render fresh/empty form with success message
#             return render(request, "portfolio.html", {
#                 "form": ContactForm(),   # empty form
#                 "success": True
#             })
#         else:
#             return render(request, "portfolio.html", {
#                 "form": form,           # keep filled values + errors
#                 "errors": form.errors
#             })

#     return render(request, "portfolio.html", {
#         "form": ContactForm()
#     })


from django.shortcuts import render, redirect
from django.core.mail import send_mail
from django.conf import settings
from .forms import ContactForm

def portfolio(request):
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            message = form.cleaned_data['message']

            subject = f"New Contact Form Submission from {name}"
            body = f"""
            You have received a new message:

            From: {name}
            Email: {email}

            Message:
            {message}
            """

            send_mail(
                subject=subject,
                message=body,
                from_email=settings.EMAIL_HOST_USER,
                recipient_list=[settings.EMAIL_HOST_USER],
                fail_silently=False,
            )

            # ✅ Redirect after success (PRG pattern)
            return redirect("/portfolio/?success=1")

        else:
            # Return with errors
            return render(request, "portfolio.html", {
                "errors": form.errors
            })

    # ✅ Check if success param is in URL
    success = request.GET.get("success") == "1"
    return render(request, "portfolio.html", {"success": success})

from django.http import JsonResponse
import json

def chatbot_view(request):
    if request.method == "POST":
        data = json.loads(request.body)
        user_msg = data.get("message", "")

        # Simple rule-based reply (you can replace with AI/OpenAI)
        if "hello" in user_msg.lower():
            reply = "👋 Hi there! How can I help you?"
        elif "bye" in user_msg.lower():
            reply = "👋 Goodbye! Have a great day!"
        else:
            reply = f"🤖 You said: {user_msg}"

        return JsonResponse({"reply": reply})

    return JsonResponse({"reply": "Send me a message!"})
