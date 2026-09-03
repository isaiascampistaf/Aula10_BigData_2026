#Exemplo 01

# preco = float(input('Preço:  '))
# quantidade = int(input("Quantidade:  "))
# total = preco * quantidade

# print(f"Total: {total}")

#erros de usuario   e erros do programador

#Exemplo 02
# try:
#     preco = float(input('Preço:  '))
#     quantidade = int(input("Quantidade:  "))
#     total = preco * quantidade

#     print(f"Total: {total}")

# except ValueError:                               #se der erro, execute aqui
#     print(f'\nErro - Informe apenas números')

#Exemplo 02
# try:
#     total_vendido = float(input('Total R$:  '))
#     qtd = int(input('Quantidade vendida: '))
#     media_vendedor = total_vendido / qtd
#     print(f"Média das vendas: {media_vendedor}")

# except ValueError:
#     print(f'\nErro: Informe apenas números')
# except ZeroDivisionError:
#     print(f"\nErro - A quantidade não pode ser Zero. ")


#Exemplo 03
#Média para 5 vendedores

# for i in range(5):
#     total_vendido = float(input('\nTotal R$:  '))
#     qtd = int(input('Quantidade vendida: '))
#     media_vendedor = total_vendido / qtd
#     print(f"Média das vendas: {media_vendedor}")

for i in range(5):
    try:
        print(f"\nVendedor {i+1}")
        total_vendido = float(input('\nTotal R$:  '))
        qtd = int(input('Quantidade vendida: '))
        media_vendedor = total_vendido / qtd
        print(f"Média das vendas: {media_vendedor}")

    except ValueError:
        print(f'\nErro: Informe apenas números')

    except KeyboardInterrupt:
        print("Programa Finalizado pelo usuário")
        exit()  # Saida do for
        
    except ZeroDivisionError:
        print(f"\nErro - A quantidade não pode ser Zero. ") 
        
           