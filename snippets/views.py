from django.shortcuts import render
from .models import Snippet
# Create your views here.


def list_snippets(request):
    snippets = Snippet.objects.all()
    return render(request,  "snippets/list_snippets.html",
                {"snippets": snippets})
