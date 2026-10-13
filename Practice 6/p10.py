class Tool:
    def __init__(self, name):
        self.name = name

    def __del__(self):
        print(self.name + ' is going to die')


def make_temp():
    t = Tool('Temp')
    print('Inside function')


print('Start')
t1 = Tool('Hammer')
make_temp()
print('End of function call')