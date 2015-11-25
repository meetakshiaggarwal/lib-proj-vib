"""vproj URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import include, url
from django.conf.urls.static import static
from django.contrib import admin
from django.conf import settings


urlpatterns = [
	url(r'^$','library.views.home', name='home'),
    url(r'^dashboard/$','library.views.dashboard', name='dashboard'),
    url(r'^add_book/$','library.views.book', name='add_book'),
    url(r'^add_book_copy/$','library.views.book_copy', name='add_book_copy'),
    url(r'^view_books/$','library.views.view_books',name='view_books'),
    url(r'^add_member/$','library.views.member',name='add_member'),
    url(r'^view_members/$','library.views.view_members',name='view_members'),
	url(r'^add_category/$','library.views.category', name='category'),
    url(r'^view_categories/$','library.views.view_categories',name='view_categories'),
    url(r'^add_author/$','library.views.author', name='author'),
    url(r'^view_authors/$','library.views.view_authors', name='view_authors'),
    url(r'^add_publisher/$','library.views.publisher', name='publisher'),
    url(r'^view_publishers/$','library.views.view_publishers',name='view_publishers'),

    url(r'^add_has_category/$','library.views.has_category',name='add_has_category'),
    url(r'^view_book_categories/$','library.views.view_book_categories',name='view_book_categories'),

    url(r'^add_compiled_by/$','library.views.compiled_by',name='add_compiled_by'),
    url(r'^view_compiled_by/$','library.views.view_compiled_by',name='view_compiled_by'),

    url(r'^add_history/$','library.views.history',name='add_history'),
    url(r'^view_history/$','library.views.view_history',name='view_history'),

    url(r'^issue_book/$','library.views.issue_book',name='issue_book'),

    url(r'^login/$','library.views.login'),
    url(r'^logout/$','library.views.logout'),
    url(r'^view/$','library.views.view'),
    url(r'^admin/', include(admin.site.urls)),
    url('', include('social.apps.django_app.urls', namespace='social')),
    url('', include('django.contrib.auth.urls', namespace='auth')),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root = settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)