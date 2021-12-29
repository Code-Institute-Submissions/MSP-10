from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from models import .

class Registerform(forms.Form):
    