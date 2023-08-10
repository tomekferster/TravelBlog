from django import forms
from .models import TravelPost, Comment

class TravelPostForm(forms.ModelForm):
    name = forms.CharField(widget=forms.TextInput(attrs={"size": 40, "placeholder": "Enter travel post name here..."}))
    text = forms.CharField(widget=forms.Textarea(attrs={"rows": 20, "placeholder": "Enter travel post text here..."}))
    image = forms.ImageField(label='Image', widget = forms.ClearableFileInput(attrs = {'class': 'form-control mb-2', 'placeholder': 'IMAGE'}))
    class Meta:
        model = TravelPost
        fields = ['name', 'text', 'tags', 'image']
        # widgets = {
        #     "name": forms.TextInput(attrs={"size": 40, "placeholder": "Enter travel post name here..."}),
        #     "text": forms.Textarea(attrs={"rows": 20, "placeholder": "Enter travel post text here..."}),
        #     }

    # can clean data like below https://docs.djangoproject.com/en/4.2/ref/forms/validation/
    # def clean_recipients(self):
    #     data = self.cleaned_data["recipients"]
    #     if "fred@example.com" not in data:
    #         raise ValidationError("You have forgotten about Fred!")


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['text', 'vote_post']