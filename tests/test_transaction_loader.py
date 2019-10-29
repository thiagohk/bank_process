# -*- coding: utf-8 -*-

import pytest
import os
import io
from bank_process.transactions_loader import load_accounts, load_transactions, process_transactions, print_accounts, main


__author__ = "thiagohk"
__copyright__ = "thiagohk"
__license__ = "mit"

ACCOUNTS_TEST_FILENAME = os.path.join(os.path.dirname(__file__), 'accounts_test.csv')
TRANSACTIONS_TEST_FILENAME = os.path.join(os.path.dirname(__file__), 'transactions_test.csv')

def test_load_accounts():
    accounts = load_accounts(ACCOUNTS_TEST_FILENAME)
    assert accounts[1].id == 1
    assert accounts[1].balance == 10
    assert accounts[2].id == 2
    assert accounts[2].balance == 1000
    assert accounts[3].id == 3
    assert accounts[3].balance == 99999999999999
    assert accounts[4].id == 4
    assert accounts[4].balance == -10
    assert accounts[5].id == 5
    assert accounts[5].balance == -99999999999999


def test_load_transactions():
    transactions = load_transactions(TRANSACTIONS_TEST_FILENAME)
    assert transactions[0].account_id == 1
    assert transactions[0].amount == 2000
    assert transactions[1].account_id == 2
    assert transactions[1].amount == 4000
    assert transactions[2].account_id == 3
    assert transactions[2].amount == 99999999999999
    assert transactions[3].account_id == 4
    assert transactions[3].amount == -1000
    assert transactions[4].account_id == 5
    assert transactions[4].amount == -99999999999999


def test_process_transactions():
    transactions = load_transactions(TRANSACTIONS_TEST_FILENAME)
    accounts = load_accounts(ACCOUNTS_TEST_FILENAME)
    processed_accounts = process_transactions(accounts, transactions)
    assert processed_accounts[1].balance == 2010
    assert processed_accounts[2].balance == 5000
    assert processed_accounts[3].balance == 199999999999998
    assert processed_accounts[4].balance == -1015
    assert processed_accounts[5].balance == -200000000000003

def test_print_accounts():
    accounts = load_accounts(ACCOUNTS_TEST_FILENAME)
    stringOutput = io.StringIO()
    print_accounts(accounts, stringOutput)
    assert "1,10\r\n2,1000\r\n3,99999999999999\r\n4,-10\r\n5,-99999999999999\r\n" == stringOutput.getvalue()
    
def test_main():
    stringOutput = io.StringIO()
    main([ACCOUNTS_TEST_FILENAME, TRANSACTIONS_TEST_FILENAME], stringOutput)
    assert "1,2010\r\n2,5000\r\n3,199999999999998\r\n4,-1015\r\n5,-200000000000003\r\n" == stringOutput.getvalue()

