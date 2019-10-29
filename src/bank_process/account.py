class Account:

    id = None
    balance = None

    def __init__(self, id, balance):
        self.id = id
        self.balance = balance
    
    def apply_transaction(self, transaction):
        self.balance += transaction.amount
        self.check_and_apply_fee(transaction)

    def check_and_apply_fee(self, transaction):
        if (transaction.is_debit() and self.should_apply_fee()):
            self.balance -= 5

    def should_apply_fee(self):
        return self.balance < 0 