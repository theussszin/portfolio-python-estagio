import os

pasta = "arquivos"

arquivos = os.listdir(pasta)

for i, arquivo in enumerate(arquivos):
    novo_nome = f"arquivo_{i}.txt"
    os.rename(
        os.path.join(pasta, arquivo),
        os.path.join(pasta, novo_nome)
    )

print("Arquivos renomeados com sucesso!")
