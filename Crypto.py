import requests

url = 'https://api.coingecko.com/api/v3/simple/price?ids=bitcoin,ethereum,solana,dogecoin&vs_currencies=brl'

while True:
    dados = requests.get(url).json()

    selector = int(input(f"\nGostaria de saber a cotação de qual moeda?\n" 
                 "\t1- Bitcoin\n"
                 "\t2- Ethereum\n"
                 "\t3- Solana\n"
                 "\t4- Dogecoin\n"
                 "\t0 - Sair\n\t\t"))

    if not selector:
        break

    match selector:
        case 1:
            print(f"1 Bitcoin está valendo: R$ {dados['bitcoin']['brl']:.2f}\n")
        case 2:
            print(f"1 Ethereum está valendo: R$ {dados['ethereum']['brl']:.2f}\n")
        case 3:
            print(f"1 Solana está valendo: R$ {dados['solana']['brl']:.2f}\n")
        case 4:
            print(f"1 Dogecoin está valendo: R$ {dados['dogecoin']['brl']:.2f}\n")
        case _:
            print("*** Selecione uma opção válida ***")
             
print("Até mais!")