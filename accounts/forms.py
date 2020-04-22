from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError




class SignUpForm(UserCreationForm):
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput)
    password2 = forms.CharField(
        label='Password Confirmation',
        widget=forms.PasswordInput
    )
    
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

    def clean_email(self):   
        email = self.cleaned_data.get('email')
        username = self.cleaned_data.get('username')
        if User.objects.filter(email=email).exclude(username=username):
            raise forms.ValidationError(u'Email addresses must be unique.')
        return email

    def clean_password2(self):
        password1 = self.cleaned_data.get('password1')
        password2 = self.cleaned_data.get('password2')

        if not password1 or not password2:
            raise ValidationError("Password must not be empty")

        if password1 != password2:
            raise ValidationError("Passwords do not match")

        return password2

#/////////cleaning data//////////////
#The clean() method on a Field subclass is responsible for running to_python(), validate(), and run_validators() in the correct order and propagating their errors. If, at any time, any of the methods raise ValidationError, the validation stops and that error is raised. This method returns the clean data, which is then inserted into the cleaned_data dictionary of the form.

#The clean_<fieldname>() method is called on a form subclass – where <fieldname> is replaced with the name of the form field attribute. This method does any cleaning that is specific to that particular attribute, unrelated to the type of field that it is. This method is not passed any parameters. You will need to look up the value of the field in self.cleaned_data and remember that it will be a Python object at this point, not the original string submitted in the form (it will be in cleaned_data because the general field clean() method, above, has already cleaned the data once).

#For example, if you wanted to validate that the contents of a CharField called serialnumber was unique, clean_serialnumber() would be the right place to do this. You don’t need a specific field (it’s a CharField), but you want a formfield-specific piece of validation and, possibly, cleaning/normalizing the data.

#The return value of this method replaces the existing value in cleaned_data, so it must be the field’s value from cleaned_data (even if this method didn’t change it) or a new cleaned value.

#The form subclass’s clean() method can perform validation that requires access to multiple form fields. This is where you might put in checks such as “if field A is supplied, field B must contain a valid email address”. This method can return a completely different dictionary if it wishes, which will be used as the cleaned_data.

#Since the field validation methods have been run by the time clean() is called, you also have access to the form’s errors attribute which contains all the errors raised by cleaning of individual fields.



#/////////Raising multiple errors///////////////
#If you detect multiple errors during a cleaning method and wish to signal all of them to the form submitter, it is possible to pass a list of errors to the ValidationError constructor.

#Using validators¶
#Django’s form (and model) fields support use of utility functions and classes known as validators. A validator is a callable object or function that takes a value and returns nothing if the value is valid or raises a ValidationError if not. These can be passed to a field’s constructor, via the field’s validators argument, or defined on the Field class itself with the default_validators attribute.

#///////link below/////////
#https://docs.djangoproject.com/en/3.0/ref/forms/validation/