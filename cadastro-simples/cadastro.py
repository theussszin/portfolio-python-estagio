cadastros = []

while True:
    nome = input("Nome (ou 'sair' para encerrar): ")
    if nome.lower() == "sair":
        break

    idade = input("Idade: ")
    cadastros.append({"nome": nome, "idade": idade})

print("\nPessoas cadastradas:")
for pessoa in cadastros:
    print(pessoa["nome"], "-", pessoa["idade"], "anos")
