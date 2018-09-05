import threading


class BankAccount(object):

    def __init__(self):
        self.balance = 0
        self.actived = True
        self._value_lock = threading.Lock()

    def get_balance(self):
        with self._value_lock:
            if self.actived:
                return self.balance
            else:
                raise ValueError("Account has been closed;")

    def open(self):
        with self._value_lock:
            self.actived = True

    def deposit(self, amount):
        with self._value_lock:
            if self.actived:
                if amount < 0:
                    raise ValueError("amount should not be negative")
                self.balance += amount
            else:
                raise ValueError("Account has been closed;")

    def withdraw(self, amount):
        with self._value_lock:
            if self.actived:
                if amount > self.balance:
                    raise ValueError("balance is not enough.")
                elif amount < 0:
                    raise ValueError("cann't withdraw negative amount.")
                self.balance -= amount
            else:
                raise ValueError("Account has been closed;")

    def close(self):
        with self._value_lock:
            self.actived = False
