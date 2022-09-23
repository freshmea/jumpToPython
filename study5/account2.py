from sys import exit

class Account():
    def __init__(self, id, cash=0):
        self._id = id
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
        print(f"id {self._id} | cash :{self.cash} | log : {self.log}")

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
        clients.append(Account("nyunghyup-0001-01-0"+str(i), 100))
    for i in range(3):
        clients.append(Minus_account("nyunghyup-0001-02-0"+str(i), -100, 500))
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
    print(clients[0]._id)       # C++ 에서의 protected 와 같은 기능을 하지는 않는다. 다른 파일에서 접근하지 못하게함.
    exit(0)

