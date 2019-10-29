# -*- coding: utf-8 -*-

import pytest
from bank_process.transaction import Transaction

__author__ = "thiagohk"
__copyright__ = "thiagohk"
__license__ = "mit"


def test_is_debit():
    assert Transaction(1, 1000).is_debit() == False
    assert Transaction(1, 1).is_debit() == False
    assert Transaction(1, 0).is_debit() == False
    assert Transaction(1, -1).is_debit() == True
    assert Transaction(1, -1000).is_debit() == True