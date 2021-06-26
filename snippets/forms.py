from django import forms
from django.db.models import fields
from .models import Snippet


class SnippetForm(forms.ModelForm):
    class Meta:
        model = Snippet
        fields = ["title", "language", "author",
                  "description"]
