import csv
import sys
import logging
import argparse
from bank_process.account import Account
from bank_process.transaction import Transaction

from bank_process import __version__

__author__ = "thiagohk"
__copyright__ = "thiagohk"
__license__ = "mit"

_logger = logging.getLogger(__name__)

def load_accounts(accounts_file_name):
    """Load accounts from file

    Args:
      accounts_file_name (str): CSV file name with accounts info 
    
    Returns:
      :<int, Account>:`accounts`: dictionary of accounts
    """
    accounts = {}
    with open(accounts_file_name) as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        for row in csv_reader:
            account = Account(int(row[0]), int(row[1]))
            accounts[account.id] = account
    return accounts

def load_transactions(transactions_file_name):
    """Load transactions from file

    Args:
      transactions_file_name (str): CSV file name with transactions info 
    
    Returns:
      :[Transaction]:`transactions`: array of transactions
    """
    transactions = []
    with open(transactions_file_name) as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        for row in csv_reader:
            transactions.append(Transaction(int(row[0]), int(row[1])))
    return transactions

def print_accounts(accounts, accountsOutput):
    """Prints accounts on the output in CSV format

    Args:
      accounts (<int, Account>): dictionary with key as account id and value as Account
      accountsOutput (outout): Output descriptor to print the results

    """
    accountsWriter = csv.writer(accountsOutput, delimiter=',')
    for account_id in accounts.keys():
        account = accounts[account_id]
        accountsWriter.writerow([account.id,account.balance])

def process_transactions(accounts, transactions):
    """Process transactions in the accounts

    Args:
      accounts (<int, Account>): dictionary with key as account id and value as Account
      transactions ([Transaction]): Array of Transaction

    Returns:
      :<int, Account>:`accounts`: dictionary with processed accounts
    """
    for transaction in transactions:
        if (transaction.account_id in accounts):
            account = accounts[transaction.account_id]
            account.apply_transaction(transaction)
        else:
            _logger.error("Account with id {} not found".format(transaction.account_id ))
    return accounts


def main(sysargv, accountsOutput):
    """Main business logic (setup logging, parse arguments and process files)

    Args:
      sysargv ([str]): command line parameters as list of strings
      accountsOutput (outout): Output descriptor to print the results

    """
    args = parse_args(sysargv)
    setup_logging()
    accounts = load_accounts(args.accounts_file)
    transactions = load_transactions(args.transactions_file)
    accounts = process_transactions(accounts, transactions)
    print_accounts(accounts, accountsOutput)

def run():
    """Call the main method

    """
    main(sys.argv[1:], sys.stdout)

def parse_args(args):
    """Parse command line parameters

    Args:
      args ([str]): command line parameters as list of strings

    Returns:
      :obj:`argparse.Namespace`: command line parameters namespace
    """
    parser = argparse.ArgumentParser(
        description="Load bank accounts and transactions and prints the processed results in CSV format")
    parser.add_argument(
        "--version",
        action="version",
        version="bank_process {ver}".format(ver=__version__))
    parser.add_argument(
        dest="accounts_file",
        help="CSV file with accounts")
    parser.add_argument(
        dest="transactions_file",
        help="CSV file with transactions")
    
    return parser.parse_args(args)

def setup_logging():
    """Setup basic logging

    """
    logformat = "[%(asctime)s] %(levelname)s:%(name)s:%(message)s"
    logging.basicConfig(level="ERROR", filename='transactions_loader.log', filemode='w',
                        format=logformat, datefmt="%Y-%m-%d %H:%M:%S")