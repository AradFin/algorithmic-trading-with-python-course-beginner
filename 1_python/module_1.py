class Symbol:
    def __init__(self, name, spread, digits):
        self.name = name
        self.spread = spread
        self.digits = digits
        print('Symbol Class created !')
    
    def print_name(self):
        print(self.name)