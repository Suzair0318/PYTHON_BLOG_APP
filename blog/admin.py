from django.contrib import admin
from blog.models import BlogModel , BlogComment
# Register your models here.

admin.site.register( (BlogModel , BlogComment))