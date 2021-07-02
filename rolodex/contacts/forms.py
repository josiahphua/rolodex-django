from django import forms
from contacts.models import Contact

class ContactForm(forms.ModelForm):

    class Meta:
        model = Contact
        fields = "__all__"
        # no exclude here
        # exclude = ['active']

        widgets = {
            "name" : forms.TextInput(attrs={'class': "form-control"}),
            "number" : forms.TextInput(attrs={'class': "form-control"}),
            "description" : forms.TextInput(attrs={'class': "form-control"})
        }