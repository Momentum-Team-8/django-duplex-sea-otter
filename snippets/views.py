from snippets.forms import SnippetForm
from django.shortcuts import render, redirect, get_object_or_404
from .models import Snippet

def delete_snippets(request, pk):
    snippet = get_object_or_404(Snippet, pk=pk)
    if request.method == 'POST':
        snippet.delete()
        return redirect(to='list_snippets')

    return render(request, "snippets/delete_snippets.html",
                  {"snippet": snippet})

def search_bar(request):
    if request.method == 'GET':
        search = request.GET.get('search')
        post = Snippet.objects.filter(title__icontains=search)
        return render(request, 'snippets/search_bar.html', {'post': post})

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
            snippet = form.save(commit = False)
            snippet.save()
            ### redirect to the list_snippets
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

def show_snippet(request, pk):
    snippet = get_object_or_404(Snippet, pk=pk)
    return render(request, "snippets/show_snippet.html", {"snippet": snippet})


## favorites
# This view should be login_required
def toggle_favorite(request, snippet_pk):
    # get the user
    user = request.user
    # get the snippet
    snippet = get_object_or_404(Snippet, pk=snippet_pk)
    # check to see if snippet is already favorited by user
    # if it is, remove favorite
    if user.fav_snippets.filter(id=snippet.id).exists():
        snippet.favorited_by.remove(user)
    else:
        snippet.favorited_by.add(user)
        


    return redirect("show_snippet", pk=snippet_pk)


def list_favorites(request): 
    user = request.user
    favos= user.fav_snippets.all()
    return render(request, "snippets/favList_snippet.html",
    {"favos": favos})

