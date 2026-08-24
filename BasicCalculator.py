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

result: float = 0
BC = BasicCalculator(0, 0) 



while True:
    print("\n*** Bem-vindo(a) a BasicCalculator!***\n"
            "\t1 - Soma\n"
            "\t2 - Subtração\n"
            "\t3 - Multiplicação\n"
            "\t4 - Divisão\n"
            "\t5 - Elevar\n"
            "\t0 - Sair\n"
        )
    menuKey = int(input("Selecione uma operação: "))
    if not menuKey:
        break

    number1 = int(input("1° Valor: "))
    number2 = int(input("2° Valor: "))

    BC.set(number1, number2)
    match menuKey:
        case 1:
            result = BC.addition()
        case 2:
            result = BC.subtraction()
        case 3:
            result = BC.multiplication()
        case 4:
            result = BC.division()
        case 5:
            result = BC.exponential()           
        case _:
           print("Valor de seleção inválido")
           break
          
    print(f"\t*** O resultado da operação é: {result}***\n")

print("Desligando...")
