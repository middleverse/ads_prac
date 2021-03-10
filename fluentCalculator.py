# -----------------------------------------------------------------
# CALCULATOR 
# -----------------------------------------------------------------

class Calculator():
    # NOTE: This class does allow for .plus().one().one(), which would evaluate to be 2
    def __init__(self):
        '''
        Calculate an operation between two Integers
        '''
        self.first, self.second, self.operation, self.result = None, None, None, None

    def new(self):
        '''
        Reset all variables. Called before any method. 
        '''
        self.first, self.second, self.operation, self.result = None, None, None, None
        return self

    def plus(self, *args):
        '''
        Bind to add
        '''
        self.operation = self.add
        return self

    def minus(self, *args):
        '''
        Bind to subtract
        '''
        self.operation = self.subtract
        return self

    def divided_by(self, *args):
        '''
        Bind to divide
        '''
        self.operation = self.divide
        return self

    def times(self, *args):
        '''
        Bind to multiply
        '''
        self.operation = self.multiply
        return self
    
    def add(self):
        return (self.first + self.second)
    
    def subtract(self):
        return (self.first - self.second)

    def multiply(self):
        return (self.first * self.second)

    def divide(self):
        # if denominator is 0, just return 0 (assumption)
        if self.second == 0:
            return 0
        return (self.first / self.second)


# -----------------------------------------------------------------
# HELPER LIBRARY
# -----------------------------------------------------------------

digits = {
    'zero'  : 0,
    'one'   : 1,
    'two'   : 2,
    'three' : 3,
    'four'  : 4,
    'five'  : 5,
    'six'   : 6,
    'seven' : 7,
    'eight' : 8,
    'nine'  : 9
}

# helper function to bind given string to a class method
def make_digit_callable(name):
    # closure
    def _method(self):
        # method called on first digit
        if self.first is None:
            self.first = digits[name] 
        # method called on second digit
        else:
            if self.operation is None:
                print('Incorrect Syntax (operator missing).')
                return None
            self.second = digits[name]
            return self.operation()
        return self
    return _method

# Create methods associated with each digit (0-9)
for name in digits:
    _method = make_digit_callable(name)
    setattr(Calculator, name, _method) # bind 'name' to _method

# ===============================================================