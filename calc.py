class Calculator:

    def __init__(self):
        pass

    def multiply(self, x, y):
        return x * y
    
    def divide(self, x, y):
        return x / y
    
    def add(self, x, y):
        return int(x) + int(y)
    
    def subtract(self, x, y):
        return x - y


def main():
    c = Calculator()

    problem = input("Problem: " )

    addition_operator_location = problem.find('+')
    subtraction_operator_location = problem.find('-')
    division_operator_location = problem.find('/')
    multiplication_operator_location = problem.find('*')
    

    first_number = problem[0:addition_operator_location]
    second_number = problem[addition_operator_location:]
    print(addition_operator_location)
    second_number_cleaner = second_number.translate({ord('+'): None})
    second_number_cleanest = second_number_cleaner.translate({ord(' '): None})
    print(first_number)
    print(second_number_cleanest)
    print(c.add(first_number, second_number_cleanest))
    


    '''
    x = input("Number 1: ")
    y = input("Number 2: ")

    if problem == '*':
        c.multiply(x, y)
    '''
main()