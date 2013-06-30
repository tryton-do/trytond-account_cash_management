# This file is part of account_cash_management module for Tryton.
# The COPYRIGHT file at the top level of this repository contains
# the full copyright notices and license terms.
from trytond.pool import Pool
from .move import *


def register():
    Pool.register(
        Line,
        module='account_cash_management', type_='model')
