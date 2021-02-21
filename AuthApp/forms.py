# import class from django
from django import forms
# import Posts from models.py
from .models import Posts

# create a ModelForm
class PostsForm(forms.ModelForm):
    # specify the name of model to use
    class Meta:
        model = Posts
        fields = "__all__"
