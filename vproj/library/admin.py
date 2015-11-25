from django.contrib import admin

# Register your models here.

from .forms import CategoryForm
from .forms import AuthorForm
from .forms import PublisherForm
from .forms import BookForm
from .forms import HasCategoryForm
from .forms import CompiledByForm
from .forms import MemberForm
from .forms import BookCopyForm
from .forms import HistoryForm
from .forms import WaitingListForm
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

class CategoryAdmin(admin.ModelAdmin):
	list_display = ["__unicode__", "category_id"]
	form = CategoryForm

class AuthorAdmin(admin.ModelAdmin):
	list_display = ["__unicode__", "author_id"]
	form = AuthorForm

class PublisherAdmin(admin.ModelAdmin):
	list_display = ["__unicode__", "publisher_id"]
	form = PublisherForm

class BookAdmin(admin.ModelAdmin):
	list_display = ["book_id","__unicode__", "isbn_no","rating", "no_of_copies"]
	form = BookForm

class HasCategoryAdmin(admin.ModelAdmin):
	list_display = ["__unicode__"]
	form = HasCategoryForm

class CompiledByAdmin(admin.ModelAdmin):
	list_display = ["book_id","author_id","publisher_id"]
	form = CompiledByForm

class MemberAdmin(admin.ModelAdmin):
	# list_display = ["first_name","last_name","phone","email","date_of_joining","reference_id"]
	form = MemberForm

class BookCopyAdmin(admin.ModelAdmin):
	form = BookCopyForm

class HistoryAdmin(admin.ModelAdmin):
	form = HistoryForm

class WaitingListAdmin(admin.ModelAdmin):
	form = WaitingListForm

# admin.site.register(SignUp,SignUpAdmin)
admin.site.register(Category,CategoryAdmin)
admin.site.register(Author, AuthorAdmin)
admin.site.register(Publisher,PublisherAdmin)
admin.site.register(Book,BookAdmin)
admin.site.register(HasCategory,HasCategoryAdmin)
admin.site.register(CompiledBy,CompiledByAdmin)
admin.site.register(Member, MemberAdmin)
admin.site.register(BookCopy,BookCopyAdmin)
admin.site.register(History,HistoryAdmin)
admin.site.register(WaitingList,WaitingListAdmin)
