# Copyright (C) 2008 Helpdesk
# -*- coding: utf-8 -*-
# Author: Alexander Brausewetter <alex@helpdeskhq.com>
# vim: set fileencoding=utf-8 ft=python.django :

"""django-payment models"""

__version__ = "$Id: $"

from django.db import models
from django.utils.translation import ugettext as _

class Currency(models.Model):
    """A distinct currency as defined by the ISO 4217 currency standard"""

    code = models.CharField(_('3-letter code'), max_length=3, primary_key=True)
    numeric_code = models.PositiveSmallIntegerField(_('numeric code'),
        unique=True)
    name = models.CharField(_('name'), max_length=48)
    decimals = models.PositiveSmallIntegerField(_('decimals'))
    symbol = models.CharField(_('currency symbol'), max_length=5)

    # TODO:
    #
    #  - Reference standard locale for every currency, so we can format locally
    #    even if the page is in a different locale.
    #    128,29 EUR // CHF 38.09 // ¥100 = 100円 (jp) // $28.39 USD // £12,000 GBP
    #
    # locale = models.CharField(max_length=5, blank=True)

    def translated_name(self):
        name = _(self.name)
        return name[0].upper() + name[1:]

    translated_name.short_description = _('name')

    def __unicode__(self):
        return _('%(code)s (%(name)s)') % {'code': self.code,
            'name': _(self.name)}

    class Meta:
        verbose_name = _('currency')
        verbose_name_plural = _('currencies')
        ordering = ('code', 'name')
