from django.contrib import admin
# Register your models here.
from show.models import *

admin.site.register(Product)
admin.site.register(Member)
admin.site.register(Category)

