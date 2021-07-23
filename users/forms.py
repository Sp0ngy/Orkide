from django.contrib.auth.models import User
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.shortcuts import redirect
from django.utils.translation import gettext_lazy as _
from . import validators
from .models import PatientProfile
from crispy_forms.helper import FormHelper
from crispy_forms.layout import *
from crispy_forms.bootstrap import *
from django.urls import reverse_lazy

User = get_user_model()

class RegistrationForm(UserCreationForm):
    """
    Form for registering a new user account.

    Validates that the requested username is not already in use, and
    requires the password to be entered twice to catch typos.

    Subclasses should feel free to add any additional validation they
    need, but should take care when overriding ``save()`` to respect
    the ``commit=False`` argument, as several registration workflows
    will make use of it to create inactive user accounts.

    """
    # Checkbox for Terms of Service
    tos = forms.BooleanField(
        widget=forms.CheckboxInput,
        label=_("I have read and agree to the Terms of Service"),
        error_messages={"required": validators.TOS_REQUIRED},
    )

    class Meta(UserCreationForm.Meta):
        fields = [
            User.USERNAME_FIELD,
            User.get_email_field_name(),
            'first_name',
            "password1",
            "password2",
        ]


    error_css_class = "error"
    required_css_class = "required"

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # activation logic
        email_field = User.get_email_field_name()
        if hasattr(self, "reserved_names"):
            reserved_names = self.reserved_names
        else:
            reserved_names = validators.DEFAULT_RESERVED_NAMES
        username_validators = [
            validators.ReservedNameValidator(reserved_names),
            validators.validate_confusables,
        ]
        self.fields[User.USERNAME_FIELD].validators.extend(username_validators)
        self.fields[email_field].validators.extend(
            (validators.HTML5EmailValidator(), validators.validate_confusables_email)
        )
        self.fields[email_field].required = True

        # form layout !!!Make sure, all required fields are included!!!
        self.helper = FormHelper(self)
        self.helper.form_id = 'register-form'
        self.helper.attrs = {'novalidate': ''}
        self.helper.form_method = 'post'
        self.helper.label_class = 'form-label'
        self.helper.help_text_inline = True
        self.helper.layout = Layout(
            Fieldset("Join Today!",
                Field('username'),
                Field('email'),
                Field('first_name'),
                Field('password1'),
                Field('password2'),
                CustomCheckbox('tos'),

                Submit('submit', 'Register', css_class='btn btn-success'),
                css_class='form-fieldset'
            )
        )

        # hiding help_texts for fields
        for fieldname in self.fields:
            self.fields[fieldname].help_text = None

class CustomCheckbox(Field):
    template = 'html_templates/custom_checkbox.html'

class CustomField(Field):
    template = 'html_templates/custom_field.html'


class UserUpdateForm(forms.ModelForm):
    # Add here, if required = True
    email = forms.EmailField(label='E-mail')
    first_name = forms.CharField(max_length=150, label='First name')
    last_name = forms.CharField(max_length=150, label='Last name')

    class Meta:
        model = User
        fields = ['username',
                  'first_name',
                  'last_name',
                  'email',
                  ]

class PatientProfilUpdateForm(forms.ModelForm):
    date_of_birth = forms.DateField(widget=forms.widgets.DateInput(attrs={'type': 'date'}))
    phone = forms.CharField(max_length=20, label='Phone')

    class Meta:
        model = PatientProfile
        fields = [
            'date_of_birth',
            'phone',
                  ]