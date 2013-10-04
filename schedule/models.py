from django.db import models
from django.contrib.auth.models import User
from django.contrib import admin

class Users(models.Model):
	id = models.AutoField(primary_key=True)
	username = models.CharField(max_length=32)
	password = models.CharField(max_length=32)
	email = models.CharField(max_length=254)
	join_date = models.DateTimeField('date joined')
	
class Instructors(models.Model):
	pass
	
class Students(models.Model):
	pass
	
class Administarators(models.Model):
	pass
	
	
class Entry(models.Model):
	title = models.CharField(max_length=40)
	snippet = models.CharField(max_length=150, blank=True)
	body = models.TextField(max_length=10000, blank=True)
	created = models.DateTimeField(auto_now_add=True)  #auto_now__add fills with current datetime
	date = models.DateField(blank=True)
	creator = models.ForeignKey(Users, blank=True, null=True)
	remind = models.BooleanField(default=False)
	
	def __unicode__(self):
		if self.title:
			return unicode(self.creator) + u" - " + self.title
		else:
			return unicode(self.creator) + u" - " + self.snippet[:40]
	
	def short(self):
		if self.snippet:
			return "<i>%s</i> - %s" % (self.title, self.snippet)
		else:
			return self.title
	
	short.allow_tags = True
	
	class Meta:
		verbose_name_plural = "entries"

### Admin

class EntryAdmin(admin.ModelAdmin):
	list_display = ["creator", "date", "title", "snippet"]
	list_filter = ["creator"]
	
admin.site.register(Entry,EntryAdmin)