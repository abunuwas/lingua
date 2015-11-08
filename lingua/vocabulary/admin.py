from django.contrib import admin

from .models import VocabTables, Words, Meanings

class VocabTablesAdmin(admin.ModelAdmin):
	fieldsets = [
		('Title of the vocabulary table', {
			'fields': ['table_title']
			}),
		('Date information', {
			'fields': ['pub_date', 'last_modified'], 
			'classes': ['collapse']
			}),
		]

	list_display = ('table_title', 'pub_date', 'last_modified')
	list_filter = ['pub_date']
	search_fields = ['table_title']

class MeaningsAdmin(admin.ModelAdmin):
	fieldsets = [
		('Meanings', {
			'fields': ['meaning']
			}),
		('Word', {
			'fields': ['word']
			}),
	]



admin.site.register(VocabTables, VocabTablesAdmin)
admin.site.register(Words)
admin.site.register(Meanings, MeaningsAdmin)
