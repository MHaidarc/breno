import json

with open("example.json", "r") as file:
    data = json.load(file)
    print("Lista atual:", data)

lista_numero = input("Digite o número da lista que deseja editar: ")
banco = data["banco"]

if lista_numero in banco:
    campo = input("Digite o nome do campo que deseja editar: ")

    if campo in banco[lista_numero]:
        novo_valor = input(f"Digite o novo valor para o campo '{campo}': ")

        banco[lista_numero][campo] = novo_valor
        print("Lista atualizada:")
        print(data)

        with open("example.json", "w") as file:
            json.dump(data, file, indent=4)
    else:
        print(f"Campo '{campo}' não encontrado na lista {lista_numero}.")
else:
    print(f"Lista {lista_numero} não encontrada.")
