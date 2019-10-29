class Transaction:

    account_id = None
    amount = None

    def __init__(self, account_id, amount):
        self.account_id = account_id
        self.amount = amount

    def is_debit(self):
        return self.amount < 0