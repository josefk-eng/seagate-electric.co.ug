from django.forms import ModelForm, TextInput, Textarea, EmailInput
from .models import ContactMessage, UserEmail
from countable_field.widgets import CountableWidget


class ContactMessageForm(ModelForm):
    class Meta:
        model = ContactMessage
        fields = "__all__"
        widgets = {
            'subject': TextInput(
                attrs={
                    'class': 'form-control',
                    'id': 'subject',
                    'name': 'subject'
                }
            ),
            'message': CountableWidget(
                attrs={
                    'class': 'form-control',
                    'name': 'message',
                    'row': '10',
                    'data-count': 'characters',
                    'data-min-count': 0,
                    'data-max-count': 1000,
                    'data-count-direction': 'down'
                }
            ),
            'name': TextInput(
                attrs={
                    'class': 'form-control',
                    'name': 'name',
                    'id': 'name'
                }
            ),
            'email': EmailInput(
                attrs={
                    'class': 'form-control',
                    'name': 'email',
                    'id': 'email'
                }
            )
        }


class EmailForm(ModelForm):
    class Meta:
        model = UserEmail
        fields = "__all__"
        widgets = {
            'email': EmailInput(
                attrs={
                    'name': 'email',
                    'type':'email',
                }
            )
        }
