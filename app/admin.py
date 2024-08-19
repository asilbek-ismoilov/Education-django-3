from django.contrib import admin
from .models import Contact, Instructors, Courses, Comments

admin.site.register((Instructors, Courses, Comments))
@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'subject', 'message']

