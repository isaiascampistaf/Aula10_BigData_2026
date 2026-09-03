# O pescador João, que atua na região costeira de Santa Catarina, procurou sua empresa de tecnologia para resolver uma necessidade que ele enfrenta no dia a dia. 
# De acordo com o regulamento de pesca do estado, a quantidade máxima permitida de peixes por dia é de 100 quilos. 
# Quando esse limite é ultrapassado, o pescador deve pagar uma multa de R$ 4,00 por quilo excedente. 

# João precisa de um programa simples, que ele possa usar no celular para informar o peso total de peixes pescados no dia, e assim verificar se haverá multa ou não. 
# Caso ultrapasse o limite, o sistema deve calcular o valor da multa automaticamente. 

# Requisito: 
# Crie um algoritmo que: 
# Receba o peso total de peixes pescados no dia 
# Verifique se houve excesso 
# Calcule e retorne o valor da multa, se houver 
# Mostre a mensagem correspondente na tela
try:

    def programa(p):
        qtd = p - 100
        multa = qtd * 4
        return multa , qtd



    peso = float(input('Peso total: '))

# except ValueError:
    # print("\nInforme o valor corretamente")

except Exception as e:
    print(f"\nInforme o valor corretamente:  {e}")

except KeyboardInterrupt:
    print("\nPrograma Finalizado pelo usuário")


else:
    if peso > 100:
        multa , excedente = programa(peso)
        print(f'Você terá que pagar uma multa de: R$ {multa:.2f}\nPois Excedeu {excedente} quilos')
    else:
        print(f'Não excedeu o limite: {peso}kg / 100kg')



