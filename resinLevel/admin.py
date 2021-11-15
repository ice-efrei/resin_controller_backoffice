from django.contrib import admin

# Register your models here.
from resinLevel.models import Resin, Printer, Print

admin.site.register(Resin)
admin.site.register(Printer)
admin.site.register(Print)
