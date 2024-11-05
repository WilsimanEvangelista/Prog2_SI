def insert_dict(d:dict, name:str, age:int, tel:str) -> dict:
    d[name] = [age,tel]
    print("Dados inseridos com sucesso!")
    return d

def remove_minors(d:dict) -> None:
    key_remove = [key for key in d if d[key][0] < 18]
    for key in key_remove:
        del d[key]
    print_dict(d)

def print_dict(d:dict) -> None:
    print("Maiores de idade:")
    for key in d:
        print(f"Nome: {key} - Telefone: {d[key][1]}")

def main():
    d = {}
    while len(d) < 10:
        name = input("Digite o nome: ")
        age = int(input("Digite a idade: "))
        tel = input("Digite o telefone: ")

        d = insert_dict(d,name,age,tel)
    remove_minors(d)
if __name__ == "__main__":
    main()