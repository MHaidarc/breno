import json

with open("example.json", "r") as file:
    data = json.load(file)

lista_numero = input("Digite o número da lista que deseja editar (1 ou 2): ")

if lista_numero in data:
    campo = input("Digite o nome do campo que deseja editar: ")

    if campo in data[lista_numero]:
        novo_valor = input(f"Digite o novo valor para o campo '{campo}': ")

        data[lista_numero][campo] = novo_valor
        print("Lista atualizada:")
        print(data)

        with open("example.json", "w") as file:
            json.dump(data, file, indent=4)
    else:
        print(f"Campo '{campo}' não encontrado na lista {lista_numero}.")
else:
    print(f"Lista {lista_numero} não encontrada.")
