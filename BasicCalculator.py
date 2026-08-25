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
Record class:
    Keep track of operations history
'''
class Record:
    def __init__(self):
        self.history = []

    def add_entry(self, n1, symbol, n2, result):
        self.history.append({
            "n1": n1,
            "operation": symbol,
            "n2": n2,
            "result": result
        })

        print(f"\n\t*** {n1} {symbol} {n2} = {result} ***\n")

    def display_summary(self):
        print("\n\t--- RESUMO DE TODAS AS OPERAÇÕES ---")
        for i, item in enumerate(self.history):
            print(f"\t\t{i+1}° - {item['n1']} {item['operation']} {item['n2']} = {item['result']}")
        print("\t------------------------------------\n")

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
                return calculator.addition(), "+"
            case 2:
                return calculator.subtraction(), "-"
            case 3:
                return calculator.multiplication(), "*"
            case 4:
                return calculator.division(), "/"
            case 5:
                return calculator.exponential(), "^"          

BC = BasicCalculator(0, 0) 
menu = Menu()        
record = Record()

while True:
    menu.display()

    try:
        menuKey = int(input("Selecione uma operação: "))
    except ValueError:
        print("\n[ERRO] Por favor, digite apenas o número da opção desejada!")
        continue

    if not menuKey:
        break
    elif menuKey > 5 or menuKey < 0: 
        print("\n[ERRO] Valor de seleção inválido")
        continue

    try:
        number1 = int(input("Informe o 1° Valor: "))
        number2 = int(input("Informe o 2° Valor: "))
    except ValueError:
        print("\n[ERRO] Você inseriu um caractere inválido. "
              "Digite apenas números inteiros.")
        continue

    BC.set(number1, number2)

    try: 
        result, symbol = menu.selection(menuKey, BC)
    except ZeroDivisionError:
        print("\n[ERRO] Impossível dividir por zero! Tente novamente.")
        continue

    record.add_entry(number1, symbol, number2, result)

record.display_summary()
print("Até mais...")
