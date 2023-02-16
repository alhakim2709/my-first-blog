from django import forms

from .models import Post
from django.core.exceptions import ValidationError

class PostForm(forms.Form):
    title = forms.CharField(label="Title", max_length=200, required=True)
    text = forms.CharField(label='Text', widget=forms.Textarea)
    # class Meta:
    #     model = Post
    #     fields = ('title', 'text',)
        
    
    def clean_title(self):
        title = self.cleaned_data['title']
        if not title:
            error = forms.ValidationError("title is required")
            self.add_error("title", error)
            return title
        return title
        