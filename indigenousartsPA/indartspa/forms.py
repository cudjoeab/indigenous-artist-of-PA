from django.forms import CharField, PasswordInput, Form, ModelForm 

from indartspa.models import Submission
from indartspa.forms import SubmissionForm

class SubmissionForm(ModelForm):
    class Meta:
        model = Submission
        fields = ['artist_name', 
                'artwork_title', 
                'email', 
                'website', 
                'description', 
                'category']