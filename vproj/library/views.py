from django.shortcuts import render_to_response, redirect, render

from .forms import CategoryForm
from .forms import AuthorForm
from .forms import PublisherForm
from .forms import BookForm
from .forms import HasCategoryForm
from .forms import CompiledByForm
from .forms import MemberForm
from .forms import BookCopyForm
from .forms import HistoryForm
from .forms import IssueForm
from .models import Category
from .models import Author
from .models import Publisher
from .models import Book
from .models import HasCategory
from .models import CompiledBy
from .models import Member
from .models import BookCopy
from .models import History

from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout
from django.contrib.auth.decorators import login_required


ADMIN_EMAILS = { 'vaibhav95aggarwal@gmail.com', 'letsread.iitbhu@gmail.com' }

# Create your views here.
@login_required(login_url='/login')
def category(request):
	form = CategoryForm(request.POST or None)

	context = {
		"text": "Enter Book Category Details ",
		"form": form,
	}

	if form.is_valid():
		instance = form.save(commit=False)

		instance.save()
		context = {
			"text": "Thank You"
		}
		return redirect("view_categories")
	return render(request,"category.html",context)

@login_required(login_url='/login')
def author(request):

	form = AuthorForm(request.POST or None)

	context = {
		"text": "Enter Book Author Details ",
		"form": form,
	}

	if form.is_valid():
		instance = form.save(commit = False)
		instance.save()

		context = {
			"text": "Thank You"
		}
		return redirect("view_authors")

	return render(request,"author.html",context)

@login_required(login_url='/login')
def publisher(request):
	form = PublisherForm(request.POST or None)

	context = {
		"text": "Enter Book Publisher Details ",
		"form": form,
	}

	if form.is_valid():
		instance = form.save(commit = False)
		instance.save()

		context = {
			"text": "Thank You"
		}
		return redirect("view_publishers")
	return render(request,"publisher.html",context)

@login_required(login_url='/login')
def book(request):
	form = BookForm(request.POST or None)

	context = {
		"text": "Enter Book Details",
		"form": form,
	}

	if form.is_valid():
		instance = form.save(commit=False)
		instance.save()

		context = {
			"text": "Thank You"	
		}
		return redirect("view_books")
	return render(request, "book.html", context)

@login_required(login_url='/login')
def has_category(request):
	form = HasCategoryForm(request.POST or None)

	context = {
		"text": "Enter values",
		"form": form,
	}

	if form.is_valid():
		instance = form.save(commit=False)
		instance.save()

		context = {
			"text": "Thank You"	
		}
		return redirect("view_book_categories")
	return render(request, "has_category.html",context)

@login_required(login_url='/login')
def compiled_by(request):
	form = CompiledByForm(request.POST or None)

	context = {
		"text": "Enter Values",
		"form": form,
	}

	if form.is_valid():
		instance = form.save(commit=False)
		instance.save()

		context = {
			"text": "Thank You"
		}
		return redirect("view_compiled_by")
	return render(request,"compiled_by.html",context)

@login_required(login_url='/login')
def member(request):
	form = MemberForm(request.POST or None)

	context = {
		"text": "Add a member",
		"form": form,
	}

	if form.is_valid():
		instance = form.save(commit=False)
		instance.save()

		context = {
			"text": "Thank You"
		}
		return redirect("view_members")
	return render(request,"member.html",context)

@login_required(login_url='/login')
def book_copy(request):
	form = BookCopyForm(request.POST or None)
	context = {
		"text": "Add a copy of Book",
		"form": form,
	}

	if form.is_valid():
		instance = form.save(commit=False)
		# print "submitted" + form
		print 'here'
		print instance
		instance.save()

		context = {
			"text": "Thank You"
		}
		return redirect("view_books")
	return render(request,"book_copy.html",context)

@login_required(login_url='/login')
def history(request):
	form = HistoryForm(request.POST or None)
	# print "form" + str(form)
	context = {
		"text": "Change History Details",
		"form": form,
	}

	if form.is_valid():
		instance = form.save(commit=False)
		# print "submitted" + form
		print 'here'
		print instance
		instance.save()

		context = {
			"text": "Thank You"
		}
	return render(request,"history.html",context)

def login(request):
	print request.path
	if not request.user.is_anonymous():
		return checklogin(request)
	return render(request,'login.html')

@login_required(login_url='/login')
def logout(request):
	del request.session['admin']
	auth_logout(request)
	context = {

		}
	return render(request, 'base.html', context)

def checklogin(request):
	if request.user.is_anonymous():
		return render(request, 'login.html')
	else :
		# check if valid mail
		curr_email = request.user.email

		domain = curr_email.split('@')[1]

		if domain == 'itbhu.ac.in' :
			curr_email2 = curr_email.split('@')[0] + '@' + 'iitbhu.ac.in'
		elif domain == 'iitbhu.ac.in':
			curr_email2 = curr_email.split('@')[0] + '@' + 'itbhu.ac.in'

		try:
			valid_user = Member.objects.get(email = curr_email)
			print "valid user " + str(valid_user.email)
		except Member.DoesNotExist:
			print "invalid" + request.user.email
			# google signed in need to sign out
			logout(request)

		if curr_email in ADMIN_EMAILS:
			print "admin"
			request.session['admin'] = True
		else :
			print "not admin"
			request.session['admin'] = False

	return render(request, 'dashboard_base.html')

@login_required(login_url='/login')
def dashboard(request):

	return render(request, 'dashboard_base.html')

def view(request):
	db_category = Category.objects.all()
	db_author = Author.objects.all()
	db_publisher = Publisher.objects.all()
	db_book = Book.objects.all()
	db_has_category = HasCategory.objects.all()
	db_compiled_by = CompiledBy.objects.all()
	db_member = Member.objects.all()

	context = {
		"category": db_category,
		"author": db_author,
		"publisher": db_publisher,
		"book": db_book,
		"has_category": db_has_category,
		"compiled_by": db_compiled_by,
		"member": db_member,
	}

	return render(request, "view.html", context)

@login_required(login_url='/login/')
def view_books(request):
	if request.method == 'POST' :
		# check if book is valid
		bookTobeDeleted = Book.objects.get(book_id = request.POST['del_id'])
		bookTobeDeleted.delete()

	db_book = Book.objects.all()

	context = {
		"book": db_book,
	}

	return render(request, "view_books.html", context)

@login_required(login_url='/login/')
def view_members(request):
	if request.method == 'POST' :
		referer = False
		# check if member is referer
		if not referer:
			memberTobeDeleted = Member.objects.get(member_id = request.POST['del_id'])
			memberTobeDeleted.delete()

	db_member = Member.objects.all()

	context = {
		"member": db_member,
	}

	return render(request, "view_members.html", context)

@login_required(login_url='/login/')
def view_publishers(request):
	if request.method == 'POST' :
		# check if publisher is valid
		publisherTobeDeleted = Publisher.objects.get(publisher_id = request.POST['del_id'])
		publisherTobeDeleted.delete()

	db_publisher = Publisher.objects.all()

	context = {
		"publisher": db_publisher,
	}

	return render(request, "view_publishers.html", context)

@login_required(login_url='/login/')
def view_authors(request):
	if request.method == 'POST' :
		# check if author is valid
		authorTobeDeleted = Author.objects.get(author_id = request.POST['del_id'])
		authorTobeDeleted.delete()

	db_author = Author.objects.all()

	context = {
		"author": db_author,
	}

	return render(request, "view_authors.html", context)

@login_required(login_url='/login/')
def view_categories(request):
	if request.method == 'POST' :
		# check if category is valid
		categoryTobeDeleted = Category.objects.get(category_id = request.POST['del_id'])
		categoryTobeDeleted.delete()

	db_category = Category.objects.all()

	context = {
		"category": db_category,
	}

	return render(request, "view_categories.html", context)

@login_required(login_url='/login/')
def view_book_categories(request):
	if request.method == 'POST' :
		# check if book&category is valid
		bookandCategoryTobeDeleted = HasCategory.objects.get(book_id = request.POST['del_id'].split('@')[0], category_id =request.POST['del_id'].split('@')[1])
		bookandCategoryTobeDeleted.delete()

	db_has_category = HasCategory.objects.all().order_by('book_id')

	context = {
		"has_category": db_has_category,
	}

	return render(request, "view_book_categories.html", context)

@login_required(login_url='/login/')
def view_compiled_by(request):
	if request.method == 'POST' :
		# check if compiledBy id valid
		book = request.POST['del_id'].split('@')[0]
		author = request.POST['del_id'].split('@')[1]
		publisher = request.POST['del_id'].split('@')[2]
		compiledByTobeDeleted = CompiledBy.objects.get(book_id = book, author_id=author,publisher_id=publisher)
		compiledByTobeDeleted.delete()

	db_compiled_by = CompiledBy.objects.all().order_by('book_id')

	context = {
		"compiled_by": db_compiled_by,
	}

	return render(request, "view_compiled_by.html", context)

@login_required(login_url='/login/')
def view_history(request):

	if request.method == 'POST' :
		# check if history is valid
		book = request.POST['del_id'].split('@')[0]
		copy = request.POST['del_id'].split('@')[1]
		member = request.POST['del_id'].split('@')[2]
		issue_date = request.POST['del_id'].split('@')[3]

		historyTobeDeleted = History.objects.get(book_id = book, copy_id= copy ,member_id=member, issue_date=issue_date)
		historyTobeDeleted.delete()

	db_history = History.objects.all().order_by('book_id')

	context = {
		"history": db_history,
	}

	return render(request, "view_history.html", context)

def issue_book(request):
	form = IssueForm(request.POST or None)

	context = {
		"text": "Issue Form ",
		"form": form,
	}

	if form.is_valid():
		instance = form.save(commit=False)
		# TODO decrease count and change availability
		instance.save()
		context = {
			"text": "Thank You"
		}
		return redirect("view_history")

	return render(request,"issue_book.html",context)

def home(request):
	return render(request, "base.html")