# This file is part of the account_cash_management module for Tryton.
# The COPYRIGHT file at the top level of this repository contains the full
# copyright notices and license terms.
import unittest
import trytond.tests.test_tryton
from trytond.tests.test_tryton import ModuleTestCase


class AccountCashManagementTestCase(ModuleTestCase):
    'Test Account Cash Management module'
    module = 'account_cash_management'


def suite():
    suite = trytond.tests.test_tryton.suite()
    suite.addTests(unittest.TestLoader().loadTestsFromTestCase(
        AccountCashManagementTestCase))
    return suite