class Ticket:
    alive = 0

    def __init__(self, name):
        self.name = name
        Ticket.alive += 1

    def __del__(self):
        Ticket.alive -= 1
        print(self.name + ' removed')

    @staticmethod
    def get_alive():
        return Ticket.alive


def temp():
    t = Ticket('T3')
    print('Alive inside:', Ticket.get_alive())


a = Ticket('T1')
b = Ticket('T2')
print('Alive:', Ticket.get_alive())
temp()
print('Alive after function:', Ticket.get_alive())
del a
print('Alive:', Ticket.get_alive())
del b
print('Alive:', Ticket.get_alive())
