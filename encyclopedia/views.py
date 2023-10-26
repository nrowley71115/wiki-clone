from django import forms
from django.shortcuts import render

from . import util

class NewPageForm(forms.Form):
    title = forms.CharField(label="Title")
    content = forms.CharField(label="Content", widget=forms.Textarea)

def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })

# open wiki entry
def entry(request, title):
    if title in util.list_entries():
        return render(request, "encyclopedia/entry.html", {
            "entry": util.get_entry(title),
            "title": title
        })
    else:
        return render(request, "encyclopedia/error.html", {
            "error": "404 Page not found"
        })
    
# search wiki entry
def search(request):
    if request.method == "POST":
        search_str = request.POST.get('q')
        # Check for exact match
        if search_str in util.list_entries():
            return render(request, "encyclopedia/entry.html", {
                "entry": util.get_entry(search_str),
                "title": search_str
            })
        # Check for sub-search_string matches
        else:
            sub_str = []
            for entry in util.list_entries():
                if search_str.lower() in entry.lower():
                    sub_str.append(entry)
            return render(request, "encyclopedia/search.html", {
                "entries": sub_str,
                "str_search": search_str,
              })
    # if request is not POST
    else:
        # redirect to index page
        return render(request, "encyclopedia/index.html", {
            "entries": util.list_entries()
        })

# create new wiiki entry
def new_page(request):
    # if request is POST
    if request.method == "POST":
        # get form data
        title = request.POST.get('title')
        content = request.POST.get('content')
        print(f'Title: {title}, Content: {content}')
        # validate title doesn't already exist
        if title in util.list_entries():
            return render(request, "encyclopedia/error.html", {
                "error": "Page already exists"
            })
        # validate title or content is not empty
        if content == '' or title == '':
            return render(request, "encyclopedia/error.html", {
                "error": "Content cannot be empty"
            })
        # TODO translate to markdown
        # TODO save to entries directory
        # TODO redirect to new page
        pass
    # if request is not POST
    else:
        # open new_page.html
        return render(request, "encyclopedia/new_page.html", {
            "form": NewPageForm()
        })