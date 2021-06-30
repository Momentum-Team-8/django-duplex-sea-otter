"""django_snippet URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.contrib import admin
from django.urls import include, path
from django.conf.urls.static import static


from snippets import views as snippets_views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', snippets_views.list_snippets, name='list_snippets'),
    path('favorites/', snippets_views.list_favorites, name='list_favorites'),
    path("accounts/", include("registration.backends.simple.urls")),
    # add
    path('snippets/snippet/add/', snippets_views.add_snippet, name='add_snippet'),
    path("snippets/<int:pk>", snippets_views.show_snippet, name="show_snippet"),
    path(
        "snippets/<int:snippet_pk>/favorite",
        snippets_views.toggle_favorite,
        name="toggle_favorite",
    ),
    path("categ/<slug:slug>", snippets_views.show_categ, name="show_categ"),
    path('categories/', snippets_views.list_category, name='list_categories'),
    path('snippets/snippets/profile', snippets_views.profile, name="profile"),

    # edit
    path('snippets/<int:pk>/edit/',
         snippets_views.edit_snippet, name='edit_snippet'),

    path('collection/<int:pk>/delete',
         snippets_views.delete_snippets, name='delete_snippets'),

    path('search_bar/', snippets_views.search_bar, name='search_bar'),

] + static(settings.STATIC_URL, docuement_root=settings.STATIC_ROOT)
