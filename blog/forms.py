from django import forms
from .models import BlogArticles

class BlogArticlesForm(forms.ModelForm):
    class Meta:
        model = BlogArticles
        fields = ('title','body')