
from django import forms
from django.forms import formset_factory

class TitleForm(forms.Form):
	title = forms.CharField(label="vocab-title", max_length=500)

class WordForm(forms.Form):
	#title = forms.CharField(label="vocab-title", max_length=500)
	word = forms.CharField(label="word", max_length=500)
	meaning = forms.CharField(label="meaning", max_length=500)

VocabularyFormSet = formset_factory(WordForm, extra=2)