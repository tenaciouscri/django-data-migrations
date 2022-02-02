from django.contrib import admin

from .models import AddressBook


class AddressBookAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "telephone_number",
        "postcode",
    )


admin.site.register(AddressBook, AddressBookAdmin)
