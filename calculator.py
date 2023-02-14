class Calculator:
    def __init__(self):
        print('*************Calculator****************')
        print( '1 - Soma:\n\
2 - Subtraction:\n\
3 - Multiplication\n\
4 - Division\n\
5 - Exit\n')
                
        while True:
            self.operation = input('Digite a operação que deseja fazer: ')
            if self.operation >= '5':
                break
            else:
                self.number1 = int(input('Digite o primeiro número '))
                self.number2 = int(input('Digite o segundo número '))
                print(self.sum()) if self.operation == '1' else print(self.subtraction()) if self.operation == '2' else\
                print(self.multiplication()) if self.operation == '3' else print(self.division()) if self.operation == '4'\
                else 0
            print()

    def sum(self):
        return f'{self.number1} + {self.number2} = {self.number1+self.number2}'
    def subtraction(self):
        return f'{self.number1} - {self.number2} = {self.number1-self.number2}'
    def multiplication(self):
         return f'{self.number1} x {self.number2} = {self.number1*self.number2}'
    def division(self):
         return f'{self.number1} / {self.number2} = {self.number1/self.number2}'

'''if __name__ == '__main__':
    Calculator()'''


Calculator()