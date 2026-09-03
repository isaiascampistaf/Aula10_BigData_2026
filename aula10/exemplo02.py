try:                                                            #para não precisar me preocupar com todos os erros do mundo
    total_vendido = float(input('\nTotal R$:  '))           #eu poderia fazer uma lista onde armazenaria os erros ao longo do tempo para ir consertando
    qtd = int(input('Quantidade vendida: '))                
    media_vendedor = total_vendido / qtd

except (ValueError, TypeError):
    print(f'\nErro: Informe apenas números')

except KeyboardInterrupt:
    print("Programa Finalizado pelo usuário")
    exit()  # Saida do for
        
except ZeroDivisionError:
    print(f"\nErro - A quantidade não pode ser Zero. ") 

else:   #SE NÃO DER ERRO
    print(f"Média das vendas: {media_vendedor}")

finally:
    print('\n-- Operação Encerrada --')