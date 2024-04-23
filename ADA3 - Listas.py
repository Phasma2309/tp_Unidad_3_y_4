POSTRES = {
    "Tarta de manzana": ["manzana", "harina", "azúcar", "canela"],
    "Helado de vainilla": ["leche", "nata", "azúcar", "vainilla"],
    "Brownie de chocolate": ["chocolate", "mantequilla", "harina", "azúcar", "huevo"]
}

def print_ingredients(postre):
    if postre in POSTRES:
        print(f"Ingredientes de {postre}: {POSTRES[postre]}")
    else:
        print(f"No se encontró el postre {postre}")

def add_ingredients(postre, nuevos_ingredientes):
    if postre in POSTRES:
        POSTRES[postre].extend(nuevos_ingredientes)
        print(f"Se añadieron los ingredientes a {postre}: {POSTRES[postre]}")
    else:
        print(f"No se encontró el postre {postre}")

def remove_ingredients(postre, ingredientes_a_eliminar):
    if postre in POSTRES:
        for ingrediente in ingredientes_a_eliminar:
            if ingrediente in POSTRES[postre]:
                POSTRES[postre].remove(ingrediente)
                print(f"Se eliminó {ingrediente} de los ingredientes de {postre}")
            else:
                print(f"{ingrediente} no se encontró en los ingredientes de {postre}")
    else:
        print(f"No se encontró el postre {postre}")

def alta_postre(postre, ingredientes):
    if postre not in POSTRES:
        POSTRES[postre] = ingredientes
        print(f"Se dio de alta el postre {postre} con ingredientes: {ingredientes}")
    else:
        print(f"El postre {postre} ya existe")

def baja_postre(postre):
    if postre in POSTRES:
        del POSTRES[postre]
        print(f"Se dio de baja el postre {postre}")
    else:
        print(f"No se encontró el postre {postre}")

def eliminar_repetidos():
    for postre, ingredientes in POSTRES.items():
        POSTRES[postre] = list(set(ingredientes))

# Prueba de las funciones
print_ingredients("Helado de vainilla")
add_ingredients("Helado de vainilla", ["galleta"])
remove_ingredients("Helado de vainilla", ["azúcar", "nata"])
alta_postre("Pastel de zanahoria", ["zanahoria", "nuez", "canela"])
baja_postre("Tarta de manzana")

print("POSTRES actualizados:")
print(POSTRES)

eliminar_repetidos()

print("POSTRES después de eliminar repetidos:")
print(POSTRES)
