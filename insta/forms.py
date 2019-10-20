from django import forms
from .models import Image,Profile,Comment
from django.contrib.auth.models import User
class NewsLetterForm(forms.Form):
    your_name = forms.CharField(label='First Name',max_length=30)
    email = forms.EmailField(label='Email')

class ImageForm(forms.ModelForm):
    class Meta:
        model = Image
        exclude = ['user', 'pub_date']

class ProfileForm(forms.ModelForm):
    class Meta:
        model=Profile
        fields=['bio','profile_picture'] 
        exclude=['user']  
       
class CommentForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['comment'].widget = forms.TextInput()
        self.fields['comment'].widget.attrs['placeholder'] = 'Add a comment...'

    class Meta:
        model = Comment
        fields = ('comment',)