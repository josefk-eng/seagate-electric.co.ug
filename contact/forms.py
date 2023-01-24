from django.forms import ModelForm, TextInput, Textarea, EmailInput
from .models import ContactMessage


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
            'message': Textarea(
                attrs={
                    'class': 'form-control',
                    'name': 'message',
                    'row': '10'
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
