# -*- coding: utf-8 -*-

import pytest
from bank_process.account import Account
from bank_process.transaction import Transaction

__author__ = "thiagohk"
__copyright__ = "thiagohk"
__license__ = "mit"


def test_should_apply_fee():
    assert Account(1, 10).should_apply_fee() == False
    assert Account(1, 0).should_apply_fee() == False
    assert Account(1, -1).should_apply_fee() == True
    # assert fib(1) == 1
    # assert fib(2) == 1
    # assert fib(7) == 13
    # with pytest.raises(AssertionError):
    #     fib(-10)


def test_check_and_apply_fee():
    account = Account(1, 10)
    account.check_and_apply_fee(Transaction(1,10))
    assert account.balance == 10

    account = Account(1, 10)
    account.check_and_apply_fee(Transaction(1,15))
    assert account.balance == 10

    account = Account(1, 10)
    account.check_and_apply_fee(Transaction(1,-11))
    assert account.balance == 10

    account = Account(1, 0)
    account.check_and_apply_fee(Transaction(1,0))
    assert account.balance == 0

    account = Account(1, -1)
    account.check_and_apply_fee(Transaction(1,0))
    assert account.balance == -1

    account = Account(1, -1)
    account.check_and_apply_fee(Transaction(1,10))
    assert account.balance == -1

    account = Account(1, -1)
    account.check_and_apply_fee(Transaction(1,-10))
    assert account.balance == -6


def test_apply_transaction():
    account = Account(1, 10)
    account.apply_transaction(Transaction(1,10))
    assert account.balance == 20

    account = Account(1, 10)
    account.apply_transaction(Transaction(1,15))
    assert account.balance == 25

    account = Account(1, 10)
    account.apply_transaction(Transaction(1,-11))
    assert account.balance == -6

    account = Account(1, 0)
    account.apply_transaction(Transaction(1,0))
    assert account.balance == 0

    account = Account(1, -1)
    account.apply_transaction(Transaction(1,0))
    assert account.balance == -1

    account = Account(1, -1)
    account.apply_transaction(Transaction(1,10))
    assert account.balance == 9

    account = Account(1, -1)
    account.apply_transaction(Transaction(1,-10))
    assert account.balance == -16