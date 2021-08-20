from django.forms import ModelForm
from .models import Messages, Emails


class Messages(ModelForm):
    class Meta:
        model = Messages
        fields = '__all__'


class Emails(ModelForm):
    class Meta:
        model = Emails
        fields = '__all__'

