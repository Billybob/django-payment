# Copyright (C) 2008 Helpdesk
# Author: Alexander Brausewetter
# vim: set ft=python.django :

"""django-payment admin configuration"""

__version__ = "$Id: $"

from django.contrib import admin
from models import *

class CurrencyAdmin(admin.ModelAdmin):
    list_display = ('code', 'translated_name', 'decimals', 'symbol')
    list_display_links = ('code', 'translated_name')
    ordering = ('code',)
    search_fields = ('code', 'name', 'numeric_code', 'symbols')

admin.site.register(Currency, CurrencyAdmin)
