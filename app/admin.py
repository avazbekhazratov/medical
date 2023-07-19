from django.contrib import admin
from .models import Xona, Xamshira, Doktor, Bemor


class DoktorAdmin(admin.ModelAdmin):
    list_display = ("ism", "familiya", "telegram_nik", "mutahasisligi")
    search_fields = ("ism", "familiya", "mutahasisligi")


class XonaAdmin(admin.ModelAdmin):
    list_display = ("odam_soni", "narxi")
    search_fields = ("narxi",)


class XamshiraAdmin(admin.ModelAdmin):
    list_display = ("ism", "familiya", "telegram_nik")
    search_fields = ("ism", "familiya")


class BemorAdmin(admin.ModelAdmin):
    list_display = ("ism", "familiya", "phone", "xona")
    search_fields = ("ism", "familiya", "phone", "xona")


admin.site.register(Xona, XonaAdmin)
admin.site.register(Doktor, DoktorAdmin)
admin.site.register(Xamshira, XamshiraAdmin)
admin.site.register(Bemor, BemorAdmin)
