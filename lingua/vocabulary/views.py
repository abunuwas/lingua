from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.template import RequestContext, loader
from django.utils import timezone

import re

from .models import VocabTables, Words, Meanings
from .forms import VocabularyFormSet, TitleForm


def index(request):
	latest_vocab_tables = VocabTables.objects.order_by('-pub_date')
	context = {'latest_vocab_tables': latest_vocab_tables}
	template = 'vocabulary/index.html'
	return render(request, template, context)


def createTable(request):
	
	if request.method == 'POST':
		title_form = TitleForm(request.POST)
		if title_form.is_valid():
			title = title_form.cleaned_data

		formset = VocabularyFormSet(request.POST)
		if formset.is_valid():
			vocabTable = VocabTables(table_title=title['title'], pub_date=timezone.now(),
				last_modified=timezone.now())
			vocabTable.save()
			for form in formset:
				cd = form.cleaned_data
				word_text = cd['word']
				meaning_text = cd['meaning']
				newWord = Words(vocabTable=vocabTable, word=word_text)
				newWord.save()
				newMeaning = Meanings(word=newWord, meaning=meaning_text)
				newMeaning.save()
				vocabTableId = vocabTable.id
			return HttpResponseRedirect('/vocabulary/' + str(vocabTableId))

	else:
		title = TitleForm()
		formset = VocabularyFormSet()
	return render(request, 'vocabulary/create_table.html', {'title': title, 'formset': formset})
	

def editTable(request, table_id):
	response = "You're editing the vocablary table %s."
	return HttpResponse(response % table_id)

def viewTable(request, table_id):
	try:
		vocab_table = VocabTables.objects.get(pk=table_id)
	except VocabTables.DoesNotExist:
		raise Http404("That table doesn't exist yet!")
	context = {'vocab_table': vocab_table}
	template = 'vocabulary/view_table.html'
	return render(request, template, context)

"""
IMPORTANT ISSUES:
Right now I'm using id values to identify the tables that must be displayed. I 
don't think this is a very safe procedure, since it would allow anybody to access
any table. Even if they must provide first some credentials to make sure they can
access the content, I think at some point I need to return as a value for the URL
an encoded (like a sha256) value of the id number of the list. And then of course
credentials would also be needed. That way, people don't know how many talbes are
in the database, in which order they were created, and cannot just access random
tables with random numbers. 
The safe values for every table can be generated at any point, taking the id of the
table, its title and the name of the creator as arguments for the function that
creates the safe key. 
Which users can access which tables should be stored in the database, in a table
that connects users' id with tables' id. When a user is looking for a table,
if the match is found, they're allowed access to the table. If a match is not 
found or the table doesn't exist, probably because they're trying to access
random material with random numbers, they'll be given an error message. 
"""