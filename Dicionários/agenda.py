import os

def print_menu() -> str:
    menu = """
    ----------- Menu -----------
    1 - Cadastrar telefone
    2 - Visualizar agenda

    """
    
    return menu

def insert_contact(d:dict) -> dict:
    name = input("Digite o nome de um contato: ")
    tel = input("Digite o telefone do contato: ")

    d[name] = tel

    print("Contato inserido com sucesso!")
    return d

def print_schedule(d:dict) -> None:
    print("\n--------------- AGENDA ---------------\n")
    for key in d:
        print(f"Nome: {key} - Telefone: {d[key]}")


def main():
    d = {}
    
    while True:
        os.system("cls")
        print(print_menu())
        op = int(input("Digite a opção que deseja: "))

        if op == 1:
            d = insert_contact(d)
        elif op == 2:
            print_schedule(d)
        else:
            print("Digite uma opção válida!")
if __name__ == "__main__":
    main()