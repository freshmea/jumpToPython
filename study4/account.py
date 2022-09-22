
class Account():
    def __init__(self, id, cash=0):
        self.id = id
        self.cash = cash
        self.log = []

    def cash_in(self, money):
        self.cash += money
        self.log.append(money)

    def cash_out(self, money):
        if self.cash > money:
            self.cash -= money
            self.log.append(-money)
        else:
            self.log.append(f'fail{-money}')

    def printlogcash(self):
        print(f"id {self.id} | cash :{self.cash} | log : {self.log}")

class Minus_account(Account):
    def __init__(self, id, cash, limit):
        super().__init__(id, cash)
        self.limit = limit

    def cash_out(self, money):
        if self.cash - money > -self.limit:
            self.cash -= money
            self.log.append(-money)
        else:
            self.log.append(f'fail{-money}')

if __name__ == '__main__':
    clients = []
    for i in range(3):
        clients.append(Account(i, 100))
    for i in range(3):
        clients.append(Minus_account(i, -100, 500))
    for i in range(80, 100, 10):
        clients[0].cash_in(i)
    clients[0].cash_out(160)
    clients[0].cash_out(160)

    for i in range(80, 100, 10):
        clients[3].cash_in(i)
    clients[3].cash_out(160)
    clients[3].cash_out(160)
    clients[3].cash_out(160)
    clients[3].cash_out(160)
    clients[3].cash_out(160)
    for c in clients:
        c.printlogcash()

