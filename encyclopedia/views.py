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
            "error": "Page not found"
        })