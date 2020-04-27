from django import forms
from .models import Post

class findpost(forms.ModelForm):
    find_word = forms.CharField(max_length=100)


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = [
            'title',
            'content',
            'expire_date',
            'tags',
        ]