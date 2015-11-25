from django import forms

# from .models import SignUp
from .models import Category
from .models import Author
from .models import Publisher
from .models import Book
from .models import HasCategory
from .models import CompiledBy
from .models import Member
from .models import BookCopy
from .models import History
from .models import WaitingList

import datetime
import time

# class SignUpForm(forms.ModelForm):
# 	class Meta:
# 		model = SignUp
# 		fields = ['email','full_name']

# 	def clean_email(self):
# 		email = self.cleaned_data.get('email')
# 		email_base, provider = email.split("@")
# 		domain, extension = provider.split(".")
# 		if not extension == "edu":
# 			raise forms.ValidationError("Please use a .edu mail")
# 		return email

class CategoryForm(forms.ModelForm):
	class Meta:
		model = Category
		fields = ['name']

	def clean_name(self):
		name = self.cleaned_data.get('name')
		if len(name) == 0:
			raise forms.ValidationError("Category name can't be empty")
		return name

class AuthorForm(forms.ModelForm):
	class Meta:
		model = Author
		fields = ['first_name','last_name']

class PublisherForm(forms.ModelForm):
	class Meta:
		model = Publisher
		fields = ['name']

class BookForm(forms.ModelForm):
	class Meta:
		model = Book
		fields = ['name','no_of_copies','isbn_no','rating']

	def clean_no_of_copies(self):
		c = self.cleaned_data.get('no_of_copies')
		if c < 0:
			raise forms.ValidationError("Enter non negative no of copies")
		return c

	def clean_isbn_no(self):
		no = self.cleaned_data.get('isbn_no')
		if no < 0:
			raise forms.ValidationError("Enter non negative isbn no")
		return no

	def clean_rating(self):
		rating = self.cleaned_data.get('rating')
		if rating < 0 & rating > 5:
			raise forms.ValidationError("Enter rating from 1 to 5")
		return rating

class HasCategoryForm(forms.ModelForm):
	class Meta:
		model = HasCategory
		fields = ['book_id','category_id']

class CompiledByForm(forms.ModelForm):
	class Meta:
		model = CompiledBy
		fields = ['book_id','author_id','publisher_id']

class MemberForm(forms.ModelForm):
	class Meta:
		model = Member
		fields = ['first_name','last_name','phone','email','date_of_joining','reference_id']

	def clean_email(self):
		email = self.cleaned_data.get('email')
		domain = email.split('@')[1]
		if domain == 'iitbhu.ac.in':
			domain = 'itbhu.ac.in'
			email = email.split('@')[0] + '@' + domain
		print "entered email " + email
		return email

class BookCopyForm(forms.ModelForm):
	class Meta:
		model = BookCopy
		fields = ['book_id','copy_id','availability','donor_id']

	def clean_availability(self):
		avail = self.cleaned_data.get('availability')
		if not avail:
			raise forms.ValidationError("A new copy cant be issued already! Set correct availability")
		return avail

class HistoryForm(forms.ModelForm):
	class Meta:
		model = History
		fields = ['book_id','copy_id','member_id','issue_date','due_date']

	def clean_issue_date(self):
		issue_date = self.cleaned_data.get('issue_date')
		# TODO add check for date to be after current date
		return issue_date

	def clean_due_date(self):
		due_date = self.cleaned_data.get('due_date')
		# TODO add check for date to be after current date and issue date
		return due_date

class IssueForm(forms.ModelForm):
	class Meta:
		model = History
		fields = ['book_id','copy_id','member_id','issue_date','due_date']

	def clean_copy_id(self):
		copy_id = self.cleaned_data.get('copy_id')
		issued = False
		if not issued:
			return copy_id
		else:
			raise forms.ValidationError("This copy already issued. Select another")

	def clean_member_id(self):
		member_id = self.cleaned_data.get('member_id')
		hasAnotherBook = False
		if not hasAnotherBook:
			return member_id
		else:
			raise forms.ValidationError("Member has already issued a book")

	def clean_issue_date(self):
		issue_date = self.cleaned_data.get('issue_date')
		now = datetime.datetime.now().date()
		if issue_date >= now:
			# validDate
			return issue_date
		else:
			raise forms.ValidationError("Enter issue date after current date")

	def clean_due_date(self):
		due_date = self.cleaned_data.get('due_date')
		issue_date = self.cleaned_data.get('issue_date')
		if issue_date is not None and due_date > issue_date:
			# validDate
			return due_date
		else:
			raise forms.ValidationError("due date must be after issue date")

class WaitingListForm(forms.ModelForm):
	class Meta:
		model = WaitingList
		fields = ['book_id','member_id','waiting_no']

