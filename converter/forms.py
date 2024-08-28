from django import forms

class TextForm(forms.Form):
    content = forms.CharField(widget=forms.Textarea(attrs={'class': 'rich-text-editor'}), label='Text Content')
