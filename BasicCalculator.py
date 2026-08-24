'''
BasicCalculator class: 
    Operations Central
'''
class BasicCalculator:
    def __init__(self, n1, n2):
        self.set(n1, n2)

    def set(self, n1, n2):
        self.n1 = n1
        self.n2 = n2
    
    def addition(self):
        return self.n1+self.n2

    def subtraction(self):
        return self.n1-self.n2
        
    def multiplication(self):
        return self.n1*self.n2

    def division(self):
        return self.n1/self.n2

    def exponential(self):
        return self.n1**self.n2

'''
Menu class:
    Simple Selection Menu
'''
class Menu:
    def display(self):
        print("\n*** Bem-vindo(a) a BasicCalculator!***\n"
                  "\t1 - Soma\n"
                  "\t2 - Subtração\n"
                  "\t3 - Multiplicação\n"
                  "\t4 - Divisão\n"
                  "\t5 - Elevar\n"
                  "\t0 - Sair\n"
            )

    @staticmethod
    def selection(key, calculator):
        match key:
            case 1:
                return calculator.addition()
            case 2:
                return calculator.subtraction()
            case 3:
                return calculator.multiplication()
            case 4:
                return calculator.division()
            case 5:
                return calculator.exponential()           

result: float = 0
BC = BasicCalculator(0, 0) 
menu = Menu()        

while True:
    menu.display()
    menuKey = int(input("Selecione uma operação: "))

    if not menuKey:
        break
    elif menuKey > 5 or menuKey < 0: 
        print("Valor de seleção inválido")
        continue

    number1 = int(input("Informe o 1° Valor: "))
    number2 = int(input("Informe o 2° Valor: "))
    BC.set(number1, number2)

    result = menu.selection(menuKey, BC)

    if result is None:
        break
    
    print(f"\t*** O resultado da operação é: {result}***\n")

print("Desligando...")
