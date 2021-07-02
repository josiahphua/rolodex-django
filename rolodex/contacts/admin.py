from django.contrib import admin
from contacts.models import Contact

# Register your models here.

class ContactAdmin(admin.ModelAdmin):
    list_display = ("name", "number", "description")

admin.site.register(Contact, ContactAdmin)