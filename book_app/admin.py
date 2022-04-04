from django.contrib import admin

# Register your models here.
from book_app.models import *

admin.site.register(Category)
admin.site.register(Book)