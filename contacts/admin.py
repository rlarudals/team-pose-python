from django.contrib import admin
from . import models

class ContactFileInline(admin.TabularInline):
    model = models.contactFileModel

@admin.register(models.ContactModel)
class ContactModelAdmin(admin.ModelAdmin):

    inlines = (ContactFileInline,)