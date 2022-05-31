from django.contrib import admin
from .models import Subject, Courses, Module
# Register your models here.

@admin.register(Subject)
class SubjectAdmin(admin.ModelAdmin):
    list_display = ['title', 'slug']
    prepopulated_fields = {'slug': ('title',)}

class ModuleInline(admin.StackedInline):
    model = Module

@admin.register(Courses)
class CoursesAdmin(admin.ModelAdmin):
    list_display = ['title',  'created']
    list_filter = ['created', ]
    search_fields = ['title', 'overview']
    prepopulated_fields = {'slug': ('title',)}
    inlines = [ModuleInline]
