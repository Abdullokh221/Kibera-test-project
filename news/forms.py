from django import forms
from .models import New
 
 
# creating a form
class NewsForm(forms.ModelForm):
 
    # create meta class
    class Meta:
        # specify model to be used
        model = New
 
        # specify fields to be used
        fields = [
            "title",
            "description",
            "author",
        ]