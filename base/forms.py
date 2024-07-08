from django import forms
from .models import TravelPost, Comment
from django.core.exceptions import ValidationError

class TravelPostForm(forms.ModelForm):
    # name = forms.CharField(widget=forms.TextInput(attrs={"size": 40, "placeholder": "Enter travel post name here...", 'class': 'test'}))
    # text = forms.CharField(widget=forms.Textarea(attrs={"rows": 20, "placeholder": "Enter travel post text here..."}))
    # image = forms.ImageField(label='Image', widget = forms.ClearableFileInput(attrs = {'class': 'form-control mb-2', 'placeholder': 'IMAGE'}))
    new_tags = forms.CharField(label = "", required = False, widget=forms.TextInput(attrs={"size": 30, "placeholder": "Enter new tag here..."}))
    class Meta:
        model = TravelPost
        fields = ('name', 'text', 'image', 'tags')
        widgets = {
            "name": forms.TextInput(attrs={"size": 40, "placeholder": "Enter travel post name here..."}),
            "text": forms.Textarea(attrs={"rows": 20, "placeholder": "Enter travel post text here..."}),
            "image": forms.ClearableFileInput(attrs={'class': 'form-control mb-2', 'placeholder': 'IMAGE'}),
            "tags": forms.CheckboxSelectMultiple(),
            }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # self.fields['name'].widget.attrs.update({'class': 'test'})      # when we have many fields and we want to update attributes of each field in the same way, use for loop
        self.fields['image'].label = 'Image __'
        # for name, field in self.fields.items():
        #     field.widget.attrs.update({'class': 'test'})



    # can clean data like below https://docs.djangoproject.com/en/4.2/ref/forms/validation/
    def clean_new_tags(self):
        data = self.cleaned_data["new_tags"]
        if "#" not in data and data != '':
            raise ValidationError("You have forgotten about #")
        return data


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('text', 'vote_post')