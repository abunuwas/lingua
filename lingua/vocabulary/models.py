from django.db import models

class VocabTables(models.Model):
	table_title = models.CharField(max_length=500)
	pub_date = models.DateTimeField('date published')
	last_modified = models.DateTimeField('last modified')

	def __str__(self):
		return self.table_title

class Words(models.Model):
	vocabTable = models.ForeignKey(VocabTables)
	word = models.CharField(max_length=500)

	def __str__(self):
		return self.word


class Meanings(models.Model):
	word = models.ForeignKey(Words)
	meaning = models.CharField(max_length=500)

	def __str__(self):
		return self.meaning
