
passphrase = 'CC74EB'

def survey(p):
    """
    You do not need to understand this code.
    >>> survey(passphrase)
    '3d2eea56786a3d9e503a4c07dd667867ef3d92bfccd68b2aa0900ead'
    """
    import hashlib
    return hashlib.sha224(p.encode('utf-8')).hexdigest()


# Object Oriented Programming

class Fib():
    """A Fibonacci number.

    >>> start = Fib()
    >>> start
    Fib object, value 0
    >>> start.next()
    Fib object, value 1
    >>> start.next().next()
    Fib object, value 1
    >>> start.next().next().next()
    Fib object, value 2
    >>> start.next().next().next().next()
    Fib object, value 3
    >>> start.next().next().next().next().next()
    Fib object, value 5
    >>> start.next().next().next().next().next().next()
    Fib object, value 8
    >>> start.next().next().next().next().next().next() # Ensure start isn't changed
    Fib object, value 8
    """

    def __init__(self, value=0):
        self.value = value

    def next(self):
        if self.value == 0:
            bob = Fib()
            bob.prev_value = 0
            bob.value = 1
            return bob
        else:
            self.prev_value, self.value = self.value, self.prev_value + self.value
            return self

    def __repr__(self):
        return "Fib object, value " + str(self.value)
#DONE!


class VendingMachine:
    """A vending machine that vends some product for some price.

    >>> v = VendingMachine('candy', 10)
    >>> v.vend()
    'Machine is out of stock.'
    >>> v.deposit(15)
    'Machine is out of stock. Here is your $15.'
    >>> v.restock(2)
    'Current candy stock: 2'
    >>> v.vend()
    'You must deposit $10 more.'
    >>> v.deposit(7)
    'Current balance: $7'
    >>> v.vend()
    'You must deposit $3 more.'
    >>> v.deposit(5)
    'Current balance: $12'
    >>> v.vend()
    'Here is your candy and $2 change.'
    >>> v.deposit(10)
    'Current balance: $10'
    >>> v.vend()
    'Here is your candy.'
    >>> v.deposit(15)
    'Machine is out of stock. Here is your $15.'

    >>> w = VendingMachine('soda', 2)
    >>> w.restock(3)
    'Current soda stock: 3'
    >>> w.restock(3)
    'Current soda stock: 6'
    >>> w.deposit(2)
    'Current balance: $2'
    >>> w.vend()
    'Here is your soda.'
    """
    def __init__(self, food, cost):
        self.food = food
        self.cost = cost
        self.stock_amount = 0
        self.deposited_amount = 0

    def vend(self):
        if self.stock_amount <= 0:
            return 'Machine is out of stock.'
        elif self.deposited_amount < self.cost:
            return 'You must deposit ${0} more.'.format(self.cost - self.deposited_amount)
        else:
            if self.deposited_amount == self.cost:
                self.deposited_amount = 0
                self.stock_amount -= 1
                return 'Here is your {0}.'.format(self.food)
            # self.deposited_amount -= self.cost
            temp_amount = self.deposited_amount - self.cost
            self.stock_amount -= 1
            self.deposited_amount = 0
            return 'Here is your {1} and ${0} change.'.format(temp_amount, self.food)

    def deposit(self, price):
        if self.stock_amount == 0:
            return 'Machine is out of stock. Here is your ${0}.'.format(price)
        else:
            self.deposited_amount += price
            return 'Current balance: ${0}'.format(self.deposited_amount)


    def restock(self, stock):
        self.stock_amount += stock
        return 'Current {1} stock: {0}'.format(self.stock_amount, self.food)

v = VendingMachine('candy', 10)
v.restock(2)
v.deposit(7)
print(v.vend())
