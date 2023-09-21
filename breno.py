import json

with open("example.json", "r") as file:
    data = json.load(file)


def SetCampo(banco, objeto):
    campos = []

    for campo in data[banco][objeto]:
        campos.append(campo)

    print("Campos disponiveis: " + ", ".join(campos))

    mode = input("Selecione um modo, v para visualizar ou e para editar: ")
    campo = input(
        "Escolha os campos para "
        + ("editar" if mode == "e" else "visualizar")
        + " (Separe por ,): "
    ).split(",")

    all_exists = True
    for id, cam in enumerate(campo):
        campo[id] = cam.strip()
        all_exists = all_exists and cam in data[banco][objeto]

        if all_exists:
            if mode == "e":
                for cam in campo:
                    newValue = input("Selecione um valor para " + cam + ": ").split(",")

                    if len(newValue) == 1:
                        newValue = newValue[0]

                        data[banco][objeto][cam] = newValue
                    else:
                        for cam in campo:
                            print(
                                "Campo "
                                + cam
                                + ": "
                                + json.dumps(data[banco][objeto][cam])
                            )
        else:
            SetCampo(banco, objeto)


def GetObject(banco):
    print("Objetos disponiveis: " + str(len(data[banco])))

    objeto = int(input("Escolha um dentre estes objetos: ")) - 1

    if len(data[banco]) >= objeto:
        SetCampo(banco, objeto)
    else:
        GetObject(banco)


def GetBanco():
    bancos = []

    for banco in data:
        bancos.append(banco)

    print("Bancos disponiveis: " + ", ".join(bancos))

    banco = input("Esconha um dentre estes bancos: ")

    if banco in data:
        GetObject(banco)
    else:
        GetBanco()


GetBanco()
with open("example.json", "w") as file:
    json.dump(data, file, indent=4)
