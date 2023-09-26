# arrays de produtos
produtos = ['máscaras faciais', 'batons', 'esmaltes', 'perfumes', 'loções', 'xampus', 'sabonetes', 'delineadores']

# substituindo produtos
produtos[1] = "rimel"
produtos[4] = "cremes hidratantes"
produtos.pop()

# add produtos a lista
produtos.append("pinças")
produtos.append("esponja")

# lista de produtos e imprimir cada um com a frase
for produto in produtos:
    print(f"Temos {produto} à venda!")