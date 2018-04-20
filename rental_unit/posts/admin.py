from django.contrib import admin
from .models import State, City, Post, Type

# Register your models here.
admin.site.register(State)
admin.site.register(City)
admin.site.register(Post)
admin.site.register(Type)