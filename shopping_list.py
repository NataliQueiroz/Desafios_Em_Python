def menu():
    product_list = []
    while True:
        print("=========== Bem vindo à lista de compras ===========\n")
        print("1. Adicionar produto")
        print("2. Remover produto")
        print("3. Pesquisar produto")
        print("4. Visualizar lista")
        print("S. Sair do programa\n")
        option = input("Selecione uma opção ou S para sair. \n ")
        if option == "1":
            product_name = input("Digite o nome do seu produto\n")
            unit_measure = input(
                "Qual a unidade de medida? \n" + "ex: Kg, g, mg, L, mL, etc.\n"
            )
            quantity = input("Qual a quantidade desejada? \n")
            description = input("Descreva a forma que você quer o produto: \n")
            product = {
                "product_name": product_name,
                "unit_measure": unit_measure,
                "quantity": quantity,
                "description": description,
            }
            product_list.append(product)
            print("Produto adicionado com sucesso!\n")
        elif option == "2":
            remove = input("Qual o ID do produto que deseja remover? \n")
            question = input(
                "Tem certeza que deseja remover? \n"
                + "Digite S para sim e N para não \n"
            )
            if question.upper() == "S": 
                product_list.pop(int(remove) - 1)
                print("Produto removido!\n")
            elif question.upper() == "N":
                print("Produto não removido")
            else:
                print("Opção Inválida!")
            print(f"Lista de produtos: {product_list}")
        elif option == "3":
            research = input("Digite o produto que deseja procurar \n")
            result = None
            for product in product_list:
                if research.strip().lower() in product["product_name"].strip().lower():
                    result = product
                    continue
            if result is not None:
                print(f"Nome do produto: {result['product_name']}\n")
                print(f"Unidade de medida:{result['unit_measure']}\n")
                print(f"Quantidade:{result['quantity']}\n")
                print(f"Descrição:{result['description']}\n")
            else:
                print("Produto não encontrado.\n")
        elif option == "4":
            for product in product_list:
                print(f"Nome do produto: {product['product_name']}\n")
                print(f"Unidade de medida:{product['unit_measure']}\n")
                print(f"Quantidade:{product['quantity']}\n")
                print(f"Descrição:{product['description']}\n")
        elif option.lower() == "s":
            break
        else:
            print("Opção inválida!\n")
menu()
