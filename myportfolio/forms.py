
from django import forms
from captcha.fields import CaptchaField
from django import forms
from captcha.fields import CaptchaField
from django import forms

class ContactForm(forms.Form):
    name = forms.CharField(max_length=100, required=True)
    email = forms.EmailField(required=True)
    message = forms.CharField(widget=forms.Textarea, required=True)
    
    
# class ContactForm(forms.Form):
#     name = forms.CharField(
#         max_length=100,
#         widget=forms.TextInput(attrs={'placeholder': 'Your Name', 'required': 'required', 'class': 'mt-1 block w-full px-4 py-3 bg-[#0b0c10] border border-[#45a29e] rounded-lg shadow-sm focus:outline-none focus:ring-[#45a29e] focus:border-[#45a29e] placeholder-gray-500 transition-all duration-300'})
#     )
#
#     email = forms.EmailField(
#         widget=forms.EmailInput(attrs={'placeholder': 'Your Email', 'required': 'required', 'class': 'mt-1 block w-full px-4 py-3 bg-[#0b0c10] border border-[#45a29e] rounded-lg shadow-sm focus:outline-none focus:ring-[#45a29e] focus:border-[#45a29e] placeholder-gray-500 transition-all duration-300'})
#     )
#     subject = forms.CharField(
#         max_length=150,
#         required=False,
#         widget=forms.TextInput(attrs={'placeholder': 'Subject (optional)', 'class': 'mt-1 block w-full px-4 py-3 bg-[#0b0c10] border border-[#45a29e] rounded-lg shadow-sm focus:outline-none focus:ring-[#45a29e] focus:border-[#45a29e] placeholder-gray-500 transition-all duration-300'})
#     )
#     message = forms.CharField(
#         widget=forms.Textarea(attrs={'placeholder': 'Your Message', 'required': 'required', 'rows': 5, 'class': 'mt-1 block w-full px-4 py-3 bg-[#0b0c10] border border-[#45a29e] rounded-lg shadow-sm focus:outline-none focus:ring-[#45a29e] focus:border-[#45a29e] placeholder-gray-500 resize-none transition-all duration-300'})
#     )
#     captcha = CaptchaField(
#         label="",
#         widget=forms.TextInput(attrs={'placeholder': 'Enter text from image', 'class': 'mt-1 block w-full px-4 py-3 bg-[#0b0c10] border border-[#45a29e] rounded-lg shadow-sm focus:outline-none focus:ring-[#45a29e] focus:border-[#45a29e] placeholder-gray-500 transition-all duration-300'})
#     )



# from django import forms
# from captcha.fields import CaptchaField
# from captcha.widgets import CaptchaTextInput

# class ContactForm(forms.Form):
#     name = forms.CharField(
#         max_length=100,
#         widget=forms.TextInput(attrs={'placeholder': 'Your Name', 'required': 'required', 'class': 'mt-1 block w-full px-4 py-3 bg-[#0b0c10] border border-[#45a29e] rounded-lg shadow-sm focus:outline-none focus:ring-[#45a29e] focus:border-[#45a29e] placeholder-gray-500 transition-all duration-300'})
#     )
#     email = forms.EmailField(
#         widget=forms.EmailInput(attrs={'placeholder': 'Your Email', 'required': 'required', 'class': 'mt-1 block w-full px-4 py-3 bg-[#0b0c10] border border-[#45a29e] rounded-lg shadow-sm focus:outline-none focus:ring-[#45a29e] focus:border-[#45a29e] placeholder-gray-500 transition-all duration-300'})
#     )
#     subject = forms.CharField(
#         max_length=150,
#         required=False,
#         widget=forms.TextInput(attrs={'placeholder': 'Subject (optional)', 'class': 'mt-1 block w-full px-4 py-3 bg-[#0b0c10] border border-[#45a29e] rounded-lg shadow-sm focus:outline-none focus:ring-[#45a29e] focus:border-[#45a29e] placeholder-gray-500 transition-all duration-300'})
#     )
#     message = forms.CharField(
#         widget=forms.Textarea(attrs={'placeholder': 'Your Message', 'required': 'required', 'rows': 5, 'class': 'mt-1 block w-full px-4 py-3 bg-[#0b0c10] border border-[#45a29e] rounded-lg shadow-sm focus:outline-none focus:ring-[#45a29e] focus:border-[#45a29e] placeholder-gray-500 resize-none transition-all duration-300'})
#     )
#     captcha = CaptchaField(
#         widget=CaptchaTextInput(attrs={'placeholder': 'Enter text from image', 'required': 'required', 'class': 'mt-1 block w-full px-4 py-3 bg-[#0b0c10] border border-[#45a29e] rounded-lg shadow-sm focus:outline-none focus:ring-[#45a29e] focus:border-[#45a29e] placeholder-gray-500 transition-all duration-300'})
#     )
# from django import forms
# from captcha.fields import CaptchaField

# class ContactForm(forms.Form):
#     name = forms.CharField(
#         max_length=100,
#         widget=forms.TextInput(attrs={'placeholder': 'Your Name', 'class': 'mt-1 block w-full px-4 py-3 bg-[#0b0c10] border border-[#45a29e] rounded-lg shadow-sm focus:outline-none focus:ring-[#45a29e] focus:border-[#45a29e] placeholder-gray-500 transition-all duration-300'})
#     )
#     email = forms.EmailField(
#         widget=forms.EmailInput(attrs={'placeholder': 'Your Email', 'class': 'mt-1 block w-full px-4 py-3 bg-[#0b0c10] border border-[#45a29e] rounded-lg shadow-sm focus:outline-none focus:ring-[#45a29e] focus:border-[#45a29e] placeholder-gray-500 transition-all duration-300'})
#     )
#     message = forms.CharField(
#         widget=forms.Textarea(attrs={'placeholder': 'Your Message', 'rows': 5, 'class': 'mt-1 block w-full px-4 py-3 bg-[#0b0c10] border border-[#45a29e] rounded-lg shadow-sm focus:outline-none focus:ring-[#45a29e] focus:border-[#45a29e] placeholder-gray-500 resize-none transition-all duration-300'})
#     )
#     captcha = CaptchaField()

# from django import forms
# from captcha.fields import CaptchaField

# class ContactForm(forms.Form):
#     name = forms.CharField(
#         max_length=100,
#         widget=forms.TextInput(attrs={'placeholder': 'Your Name', 'class': 'mt-1 block w-full px-4 py-3 bg-[#0b0c10] border border-[#45a29e] rounded-lg shadow-sm focus:outline-none focus:ring-[#45a29e] focus:border-[#45a29e] placeholder-gray-500 transition-all duration-300'})
#     )
#     email = forms.EmailField(
#         widget=forms.EmailInput(attrs={'placeholder': 'Your Email', 'class': 'mt-1 block w-full px-4 py-3 bg-[#0b0c10] border border-[#45a29e] rounded-lg shadow-sm focus:outline-none focus:ring-[#45a29e] focus:border-[#45a29e] placeholder-gray-500 transition-all duration-300'})
#     )
#     message = forms.CharField(
#         widget=forms.Textarea(attrs={'placeholder': 'Your Message', 'rows': 5, 'class': 'mt-1 block w-full px-4 py-3 bg-[#0b0c10] border border-[#45a29e] rounded-lg shadow-sm focus:outline-none focus:ring-[#45a29e] focus:border-[#45a29e] placeholder-gray-500 resize-none transition-all duration-300'})
#     )
#     captcha = CaptchaField()




# from django import forms
# from captcha.fields import CaptchaField

# class ContactForm(forms.Form):
#     name = forms.CharField(
#         max_length=100,
#         widget=forms.TextInput(attrs={'placeholder': 'Your Name', 'class': 'mt-1 block w-full px-4 py-3 bg-[#0b0c10] border border-[#45a29e] rounded-lg shadow-sm focus:outline-none focus:ring-[#45a29e] focus:border-[#45a29e] placeholder-gray-500 transition-all duration-300'})
#     )
#     email = forms.EmailField(
#         widget=forms.EmailInput(attrs={'placeholder': 'Your Email', 'class': 'mt-1 block w-full px-4 py-3 bg-[#0b0c10] border border-[#45a29e] rounded-lg shadow-sm focus:outline-none focus:ring-[#45a29e] focus:border-[#45a29e] placeholder-gray-500 transition-all duration-300'})
#     )
#     message = forms.CharField(
#         widget=forms.Textarea(attrs={'placeholder': 'Your Message', 'rows': 5, 'class': 'mt-1 block w-full px-4 py-3 bg-[#0b0c10] border border-[#45a29e] rounded-lg shadow-sm focus:outline-none focus:ring-[#45a29e] focus:border-[#45a29e] placeholder-gray-500 resize-none transition-all duration-300'})
#     )
    
#     captcha = CaptchaField()
#     # captcha = CaptchaField(
    #     widget=forms.TextInput(attrs={'class': 'captcha-input-field'}))
    # captcha = CaptchaField(
    #     widget=forms.TextInput(attrs={
    #         'class': 'captcha-input-field',
    #         'placeholder': ' '  # This is the key to making the label float
    #     }))

# from django import forms
# from captcha.fields import CaptchaField

# class ContactForm(forms.Form):
#     # Other fields...
#     captcha = CaptchaField(
#         widget=forms.TextInput(attrs={'class': 'captcha-input-field'})
#     )