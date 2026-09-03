#Desenvola um programa que simule um caixa eletronico.
#O sistema deve iniciar com um saldo de 1000 e solicitar ao usuario o valor que deseja sacar
#Após a tentativa de saque, exiba mensagens adequadas informando o resultado da operação e finalize o programa
#Utilize a estrututra de tratamento de erros

# saldo = 1000
# print(f"Saldo atual: R$ {saldo:.2f}")

# try:
#     saque = float(input('\nQuanto deseja sacar?   '))
    
# except ValueError:
#     print(f'\nErro: Informe apenas números')



# except KeyboardInterrupt:
#     print("Programa Finalizado pelo usuário")
#     exit()  
         
# else:
#     if saque > saldo:
#         print('Saldo insuficiente')
#     else:
#         resultado = saldo - saque
#         print(f'\nSaque Realizado de R${saque:.2f}')
#         print(f'\nSaldo atual: {resultado:.2f}')

# finally:
#     print('\n-- Operação Finalizada --')


#Correção
    
# print("""
# ========================================
#             Caixa Eletrônico            
# ========================================
# """)
# try:   #tente executar isto
#     saldo = 1000
#     saque = float(input('Quanto deseja sacar?  '))

# except ValueError:    #se der este err, execute a linha abaixo
#     print("\nInforme o valor corretamente")

# except KeyboardInterrupt:
#     print("\nPrograma Finalizado pelo usuário")

# else:  # Se não der erro, faz isso
    
#     if saque > saldo:
#         print('\nSaldo Insuficiente')

#     elif saque < 2:
#         print(f'\nO valor do saque deve ser a partir de R$ 2,00')

#     else:
#         saldo -= saque
#         print('\nSaque realizado com sucesso')
#         print(f'\nSaldo restante R$ {saldo:.2f}')

# finally:
#     print('\n--Operação Finalizada--')

# print('\n===Sessão Encerrada===')




print("""
========================================
            Caixa Eletrônico            
========================================
""")
try:   #tente executar isto
    saldo = 1000
    saque = float(input('Quanto deseja sacar?  '))

except Exception as e:    #desta forma ele pega o texto q apareceria no terminal e joga para variavel "e" e depois o texto aparece no print
    print(f"\nInforme o valor corretamente:  {e}")

except KeyboardInterrupt:
    print("\nPrograma Finalizado pelo usuário")

else:  # Se não der erro, faz isso
    
    if saque > saldo:
        print('\nSaldo Insuficiente')

    elif saque < 2:
        print(f'\nO valor do saque deve ser a partir de R$ 2,00')

    else:
        saldo -= saque
        print('\nSaque realizado com sucesso')
        print(f'\nSaldo restante R$ {saldo:.2f}')

finally:
    print('\n--Operação Finalizada--')

print('\n===Sessão Encerrada===')