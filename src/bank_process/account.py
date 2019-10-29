class Account:

    id = None
    balance = None

    def __init__(self, id, balance):
        self.id = id
        self.balance = balance
    
    def apply_transaction(self, transaction):
        """Apply the transaction in the current account

        Args:
        transaction (Transaction): Transaction to be applyed 
        
        """
        self.balance += transaction.amount
        self.check_and_apply_fee(transaction)

    def check_and_apply_fee(self, transaction):
        """Checks if transaction is a debit operation and if the account balance is negative
        and if True apply a 5 fee 

        Args:
            transaction (Transaction): Transaction to be applyed 
        
        """
        if (transaction.is_debit() and self.should_apply_fee()):
            self.balance -= 5

    def should_apply_fee(self):
        """Checks if current account is negative

        Returns:
        :boolean:`should_apply_fee`: True if current account is negative
        
        """
        return self.balance < 0 