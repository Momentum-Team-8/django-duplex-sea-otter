from snippets.models import Snippet
from django.shortcuts import render, redirect, get_object_or_404

# Create your views here.


def delete_snippets(request, pk):
    snippet = get_object_or_404(Snippet, pk=pk)
    if request.method == 'POST':
        snippet.delete()
        return redirect(to='list_snippets')

    return render(request, "snippets/delete_snippets.html",
                  {"snippet": snippet})
