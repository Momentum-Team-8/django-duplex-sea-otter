from snippets.forms import SnippetForm
from django.shortcuts import render, redirect, get_object_or_404
from .models import Snippet


def list_snippets(request):
    snippets = Snippet.objects.all()
    return render(request,  "snippets/list_snippets.html",
                {"snippets": snippets})

# Create your views here.
def add_snippet(request):
    if request.method == 'GET':
        form = SnippetForm()
    else:
        form = SnippetForm(data=request.POST)
        if form.is_valid():
            ### redirect to the book_list 
            return redirect(to='list_snippets')
    return render(request, "snippets/add_snippet.html", {"form": form})

def edit_snippet(request, pk):
    snippet = get_object_or_404(Snippet, pk=pk)
    if request.method == 'GET':
        form = SnippetForm(instance=snippet)
    else:
        form = SnippetForm(data=request.POST, instance=snippet)
        if form.is_valid():
            form.save()
            return redirect(to='list_snippets')

    return render(request, "snippets/edit_snippet.html", {
        "form": form,
        "snippet": snippet
    })
