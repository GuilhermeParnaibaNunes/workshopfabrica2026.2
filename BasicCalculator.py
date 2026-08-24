'''
BasicCalculator class: 
    Central of Operations
'''
class BasicCalculator:
    def __init__(self, n1, n2):
        self.n1 = n1
        self.n2 = n2
    
    def addition(self, n1, n2):
        return n1+n2

    def subtraction(self, n1, n2):
        return n1-n2
        
    def multiplication(self, n1, n2):
        return n1*n2

    def division(self, n1, n2):
        return n1/n2

    def exponential(self, n1, n2):
        return n1**n2
            
'''
1 - Funcionar
2 - POO
3 - Try catch (validar)
'''

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

    match menuKey:
        case 1:
            result = BC.addition(number1, number2)
        case 2:
            result = BC.subtraction(number1, number2)
        case 3:
            result = BC.multiplication(number1, number2)
        case 4:
            result = BC.division(number1, number2)
        case 5:
            result = BC.exponential(number1, number2)           
        case _:
           print("Valor de seleção inválido")
          
    print(f"\t*** O resultado da operação é: {result}***\n")

print("Desligando...")
