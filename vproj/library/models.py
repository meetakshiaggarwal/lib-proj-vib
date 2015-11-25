from django.db import models
from django.core.validators import RegexValidator
# Create your models here.
# class SignUp(models.Model):
# 	email = models.EmailField()
# 	full_name = models.CharField(max_length=120, blank=True, null=True)
# 	timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)
# 	updated = models.DateTimeField(auto_now_add=False, auto_now=True)
	
# 	def __unicode__(self): # __str__ for python 3.3
# 		return self.email

# Book Category
class Category(models.Model):
	category_id = models.AutoField(primary_key=True)
	name = models.CharField(max_length=120, blank=False, null=False)

	def __unicode__(self):
		return self.name

# Authors
class Author(models.Model):
	author_id = models.AutoField(primary_key=True)
	first_name = models.CharField(max_length=100, blank=False, null=False,default='default')
	last_name = models.CharField(max_length=100, blank=False, null=False,default='default')

	class Meta:
		unique_together = (("first_name","last_name"))

	def __unicode__(self):
		return self.first_name +" "+ self.last_name

# Publisher
class Publisher(models.Model):
	publisher_id = models.AutoField(primary_key=True)
	name = models.CharField(max_length=120, blank=False, null=False, unique=True)

	def __unicode__(self):
		return self.name

# Book
class Book(models.Model):
	book_id = models.AutoField(primary_key=True)
	isbn_no = models.IntegerField(null=False)
	name = models.CharField(max_length=200, blank=False, null=False)
	no_of_copies = models.PositiveIntegerField(default=0)
	rating = models.PositiveSmallIntegerField(default=0)

	def __unicode__(self):
		return self.name

# Relation bw Books and Categories
class HasCategory(models.Model):
	book_id = models.ForeignKey('Book')
	category_id = models.ForeignKey('Category')

	class Meta:
		unique_together = (("book_id","category_id"),)

	def __unicode__(self):
		return str(str(self.book_id) + " has category " + str(self.category_id))

# relation bw book authors and publishers
class CompiledBy(models.Model):
	book_id = models.ForeignKey('Book')
	author_id = models.ForeignKey('Author')
	publisher_id = models.ForeignKey('Publisher')

	class Meta:
		unique_together = (("book_id","author_id","publisher_id"),)

	def __unicode__(self):
		return str(str(self.book_id) + " written by " + str(self.author_id) + " published by " + str(self.publisher_id))

# Member
class Member(models.Model):
	member_id = models.AutoField(primary_key=True)
	first_name = models.CharField(max_length=100,null=False,blank=False)
	last_name = models.CharField(max_length=100,null=False,blank=False)
	phone_regex = RegexValidator(regex=r'^\+?1?\d{11,13}$', message="Phone number must be entered in the format: '+919999999'. Up to 13 digits allowed.")
	phone = models.CharField(max_length=13,validators=[phone_regex], blank=True) # validators should be a list
	email = models.EmailField()
	date_of_joining = models.DateField(null=False)
	reference_id = models.ForeignKey('Member',default=0)

	def __unicode__(self):
		return self.first_name +" "+ self.last_name

# a copy of a particular book
class BookCopy(models.Model):
	book_id = models.ForeignKey('Book')
	copy_id = models.PositiveIntegerField(null=False)
	availability = models.BooleanField()
	ETA = models.DateField(auto_now=False,auto_now_add=False,null=True)
	date_of_addition = models.DateField(auto_now=False,auto_now_add=True)
	donor_id = models.ForeignKey('Member')

	class Meta:
		unique_together = ( ("book_id","copy_id"), )

	def __unicode__(self):
		return str(self.book_id) + " " + str(self.copy_id)

class History(models.Model):
	trans_id = models.AutoField(primary_key=True)
	book_id = models.ForeignKey('Book')
	copy_id = models.ForeignKey('BookCopy')
	member_id = models.ForeignKey('Member')
	issue_date = models.DateField(null=False)
	due_date = models.DateField(null=False)
	return_date = models.DateField(null=True)

	class Meta:
		unique_together = (( "book_id","copy_id","member_id","issue_date" ))

	def __unicode__(self):
		return str(self.book_id) +"-" + str(self.copy_id)+ "issued by" + str(self.member_id)

class WaitingList(models.Model):
	wait_id = models.AutoField(primary_key=True)
	book_id = models.ForeignKey('Book')
	member_id = models.ForeignKey('Member')
	waiting_no = models.PositiveIntegerField(null=False)

	class Meta:
		unique_together = ( ("book_id","member_id","waiting_no"), )
	def __unicode__(self):
		return str(self.member_id) + "waiting for " + str(self.book_id) + "with wait no " + waiting_no