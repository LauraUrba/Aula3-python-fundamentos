class Aluno:
    def __init__(self, nome, idade, nota):
        self.nome = nome
        self.idade = idade
        self.nota = nota

    def situacao(self):
        if self.nota >= 7:
            return "Aprovado"
        elif self.nota >= 5 and self.nota < 7:
            return "Em recuperação"
        else:
            return "Reprovado"

    def exibir_informacoes(self):
        return f"Nome: {self.nome}, Idade: {self.idade}, Nota: {self.nota}, Situação: {self.situacao()}"


def saudacao():
    print("Bem-vindo ao sistema de cadastro de alunos!")


def cadastrar_aluno():
    nome = input("Digite o nome do aluno: ")
    
    # PROTEÇÃO PARA IDADE - Fica repetindo até digitar um número
    while True:
        try:
            idade = int(input("Digite a idade do aluno: "))
            if idade > 0:  # Idade deve ser positiva
                break
            else:
                print(" A idade deve ser maior que zero!")
        except ValueError:
            print(" Por favor, digite apenas NÚMEROS para a idade!")
    
    # PROTEÇÃO PARA NOTA - Fica repetindo até digitar um número válido  
    while True:
        try:
            nota = float(input("Digite a nota do aluno (0 a 10): "))
            if 0 <= nota <= 10:  # Nota deve estar entre 0 e 10
                break
            else:
                print(" A nota deve estar entre 0 e 10!")
        except ValueError:
            print(" Por favor, digite apenas NÚMEROS para a nota!")
    
    return {"nome": nome, "idade": idade, "nota": nota}


def calcular_media(lista):
    if not lista:
        return 0
    return sum(aluno["nota"] for aluno in lista) / len(lista)


def contar_aprovados(lista):
    return sum(1 for aluno in lista if aluno["nota"] >= 7)


def listar_alunos_abc(lista):
    nomes = sorted(aluno["nome"] for aluno in lista)
    print("Alunos em ordem alfabética:")
    for nome in nomes:
        print(nome)


def mostrar_situacoes(lista):
    for aluno in lista:
        nota = aluno["nota"]
        if nota >= 7:
            status = "Aprovado"
        elif nota >= 5:
            status = "Em recuperação"
        else:
            status = "Reprovado"
        print(f"{aluno['nome']}: {status}")


def salvar_arquivo(lista):
    with open("alunos.txt", "w") as f:
        for aluno in lista:
            f.write(f"{aluno['nome']},{aluno['idade']},{aluno['nota']}\n")


def ler_arquivo():
    lista = []
    try:
        with open("alunos.txt", "r") as f:
            for linha in f:
                nome, idade, nota = linha.strip().split(",")
                lista.append(
                    {"nome": nome, "idade": int(idade), "nota": float(nota)})
    except FileNotFoundError:
        print("Arquivo não encontrado.")
    return lista


def demonstrar_classes(lista):
    print("\nDemonstração com Programação Orientada a Objetos:")
    objetos = [Aluno(aluno["nome"], aluno["idade"], aluno["nota"])
               for aluno in lista]
    for obj in objetos:
        print(obj.exibir_informacoes())


def main():
    saudacao()

    while True:
        try:
            qtd = int(input("\nQuantos alunos deseja cadastrar? "))
            if qtd > 0:
                break
            else:
                print("Digite um número maior que zero!")
        except ValueError:
            print("Entrada inválida. Digite um número inteiro.")

    lista_alunos = []
    for i in range(qtd):
        print(f"\nCadastrando aluno {i + 1} de {qtd}")
        aluno = cadastrar_aluno()
        lista_alunos.append(aluno)

    salvar_arquivo(lista_alunos)

    print("\n--- Dados dos Alunos ---")
    mostrar_situacoes(lista_alunos)
    print(f"Média da turma: {calcular_media(lista_alunos):.2f}")
    print(f"Alunos com nota maior ou igual a 7: {contar_aprovados(lista_alunos)}")
    listar_alunos_abc(lista_alunos)

    demonstrar_classes(lista_alunos)

    print("\n--- Conteúdo do Arquivo ---")
    alunos_do_arquivo = ler_arquivo()
    for aluno in alunos_do_arquivo:
        print(f"{aluno['nome']}, {aluno['idade']} anos, Nota: {aluno['nota']}")


if __name__ == "__main__":
    main()