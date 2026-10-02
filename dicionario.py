clientes = [
    {"nome": "ana", "cel": "11878","empresa": "fiat"},
    {"nome": "pedro", "cel": "15337","empresa": "intel"},
    {"nome": "maria", "cel": "56734","empresa": "microsoft"},
    {"nome": "felipe", "cel": "67282","empresa": "intel"},
]
    # FILTRAR EMPRESA:
empresa_digitada = str(input("Qual o nome da empresa: "))

for cliente in clientes:
    if cliente ["empresa"] == empresa_digitada:
        print(cliente)

print("---> ADICIONANDO CLIENTE <---")

nome_cliente = str(input("Qual o nome do cliente que vc quer adicionar: "))

celular = str(input("Qual o celular que vc quer adicionar: "))

empresa = str(input("Qual o nome da empresa que vc quer adicionar: "))

novo_cliente = {
    "nome": nome_cliente,
    "cel": celular,
    "empresa": empresa,
}

clientes.append(novo_cliente)
print(clientes)

print("---> REMOVENDO CLIENTES <---")

nome_cliente = str(input("Qual o nome do cliente que vc quer remover: "))
for cliente in clientes:
    if cliente ["nome"] == nome_cliente:
        clientes.remove(cliente)
        break
print(clientes)