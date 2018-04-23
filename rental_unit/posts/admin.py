from django.contrib import admin
from .models import State, City, Post
from .forms import PostForm

# Register your models here.
# admin.site.register(State)
admin.site.register(City)

class StateAdmin(admin.ModelAdmin):
    list_display = ['state_abbrv', 'state'] 
    list_filter = ['state_abbrv', 'state'] 
    search_fields = ['state']

admin.site.register(State, StateAdmin)

class PostAdmin(admin.ModelAdmin):
    form = PostForm

admin.site.register(Post, PostAdmin)