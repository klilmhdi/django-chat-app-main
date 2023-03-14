from django.db import models
from datetime import datetime
from django.forms import forms, ChoiceField, CharField
from django.forms.widgets import RadioSelect
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit


# Create your models here.
class Room(models.Model):
    name = models.CharField(max_length=1000)



class EncryptionForm(forms.Form):
    algorithm = ChoiceField(choices=[(
        "Hill Cipher", "Hill Cipher"), ("2Des Cipher", "2Des Cipher")], required=True, widget=RadioSelect)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_class = 'blueForms'
        self.helper.form_method = 'get'
        self.helper.form_action = ''
        self.helper.add_input(Submit('submit', 'Enter'))

class Message(models.Model):
    value = models.CharField(max_length=1000000)
    date = models.DateTimeField(default=datetime.now, blank=True)
    user = models.CharField(max_length=1000000)
    room = models.CharField(max_length=1000000)
    # ciphername = models.CharField(max_length=10000000)
    # ciphermessage = models.CharField(max_length=1000000)



