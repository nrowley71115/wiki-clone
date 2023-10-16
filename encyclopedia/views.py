from django import forms
from django.shortcuts import render

from . import util

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
        