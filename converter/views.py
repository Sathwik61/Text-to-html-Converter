from django.shortcuts import render
from .forms import TextForm

def convert_text(request):
    html_content = ""
    if request.method == "POST":
        form = TextForm(request.POST)
        if form.is_valid():
            html_content = form.cleaned_data['content']
    else:
        form = TextForm()

    return render(request, 'converter/index.html', {'form': form, 'html_content': html_content})
