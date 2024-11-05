exercicios = [ ("P001", "Supino articulado inclinado"),
("P002", "Supino declinado com halteres"),
("P003", "Fly"),
("C001", "Barra graviton"),
("C002", "Fly inverso"),
("C003", "Remada curvada supinada"),
("T001", "Triceps máquina"),
("T002", "Triceps testa com barra"),
("T003", "Tricpes inverso"),
("B001", "Biceps barra W"),
("B002", "Biceps alternado polia baixa"),
("B003", "Rosca neutra com halteres"),
("A001", "Abdominal obliquo banco lombar"),
("A002", "Abdominal paralela joelho estendido"),
("A003", "Abdominal canivete"),
("A004", "Abdominal morcego"),
("A005", "Lombar banco"),
("O001", "Desenvolvimento Arnold"),
("O002", "Elevação frontal com corda"),
("O003", "Remada alta na polia baixa"),
("I001", "Agachamento Smith"),
("I002", "Leg horizontal"),
("I003", "Cadeira extensora"),
("I004", "Flexora vertical"),
("I005", "Cadeira flexora"),
("I006", "Panturrilha máquina") ]

alunos = [ ("enzo", "Enzo da Silva", "12345"),
("vale", "Valentina", "abacaxi"),
("ramon", "Seu Madruga", "b71<3") ]

treinos = { "enzo" : [("P001",3,8,"A"), ("P002",3,8,"A"), ("P003",3,8,"A"),
("T001",3,8,"A"), ("T002",3,8,"A"), ("T003",3,8,"A"),
("A001",4,15,"A"), ("A002",4,15,"A"), ("C001",3,8,"B"),
("C002",3,8,"B"), ("C003",3,8,"B"), ("B001",3,8,"B"),
("B002",3,8,"B"), ("B003",3,8,"B"), ("A001",3,8,"B"),
("A002",4,15,"B"), ("A003",4,15,"B"), ("O001",4,15,"C"),
("O002",3,8,"C"), ("O003",3,8,"C"), ("P001",3,8,"C"),
("P002",3,8,"C"), ("P003",3,8,"C"), ("P004",3,8,"C"),
("P005",3,8,"C"), ("P006",3,8,"C") ],
"vale" : [("P001",3,8,"A"), ("T001",3,8,"A"), ("A001",3,8,"A"),
("C001",3,8,"B"), ("B001",3,8,"B"), ("A001",3,8,"B"),
("A003",3,8,"C"), ("O001",3,8,"C"), ("P006",3,8,"C") ] }

def retorna_nome(login:str, alunos:list) -> str:
    for (log, nome, _) in alunos:
        if log == login:
            return nome

def q1(exercicios:list, alunos:list, treinos:dict, login:str, grupo:str) -> None:
    nome = retorna_nome(login,alunos)
    print(f"Aluno: {nome}\nGrupo: {grupo}\n")
    for (cod, qtd_series, n_repet, gp) in treinos[login]:
        if gp == grupo:
            for (cod_exerc, exerc) in exercicios:
                if cod == cod_exerc:
                    print(f"{exerc} - {qtd_series} de {n_repet}")

def q2(exercicios:list, treinos:dict, login:str):
    l = []
    for (cod,_,_,_) in treinos[login]:
        l.append(cod)
    for (cod_exe, nome_exe) in exercicios:
        if cod_exe not in l:
            print(nome_exe)
