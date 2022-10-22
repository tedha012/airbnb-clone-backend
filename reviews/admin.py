from django.contrib import admin
from reviews.models import Review


@admin.register(Review)
class RegisterAdmin(admin.ModelAdmin):

    list_display = (
        "__str__",
        "payload",
    )
    list_filter = ("rating",)
