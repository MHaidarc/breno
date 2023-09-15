import json

# Aqui está o JSON corrigido
with open("example.json", "r") as file:
    data = json.load(file)
# Pergunta ao usuário qual lista ele deseja editar
lista_numero = input("Digite o número da lista que deseja editar (1 ou 2): ")

# Verifica se o número da lista é válido
if lista_numero in data:
    # Pergunta ao usuário qual valor da lista ele deseja editar
    campo = input("Digite o nome do campo que deseja editar: ")

    # Verifica se o campo existe na lista selecionada
    if campo in data[lista_numero]:
        novo_valor = input(f"Digite o novo valor para o campo '{campo}': ")

        # Atualiza o valor na lista
        data[lista_numero][campo] = novo_valor
        print("Lista atualizada:")
        print(data)

        # Salva as alterações de volta no arquivo JSON
        with open("example.json", "w") as file:
            json.dump(data, file, indent=4)
    else:
        print(f"Campo '{campo}' não encontrado na lista {lista_numero}.")
else:
    print(f"Lista {lista_numero} não encontrada.")
