# This file is part of account_cash_management module for Tryton.
# The COPYRIGHT file at the top level of this repository contains
# the full copyright notices and license terms.
from trytond.model import fields
from trytond.pool import PoolMeta

__all__ = ['Line']
__metaclass__ = PoolMeta


class Line:
    __name__ = 'account.move.line'
    cheque_received = fields.Boolean('Cheque Received')
