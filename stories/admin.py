from django.contrib import admin
from ckeditor.widgets import CKEditorWidget
from .models import Story, Author, Poem
from django.db import models

class PoemAdmin(admin.ModelAdmin):
    formfield_overrides = {
        models.TextField: {'widget': CKEditorWidget()},
    }

class StoryAdmin(admin.ModelAdmin):
    formfield_overrides = {
    models.TextField: {'widget': CKEditorWidget()},
    }

admin.site.register(Story)
admin.site.register(Author)
admin.site.register(Poem)
