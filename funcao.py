# # # def mensagem(nome="puta"):
# # #     print(f"eae cuzao, {nome}")


# # # # nome = input("diga o nome arrombado: ")
# # # # mensagem(nome)
# # # mensagem()

# # # def calcular_total(numeros):
# # #     return sum(numeros)

# # # list=[]
# # # n1 = int(input("um numero: "))
# # # n2 = int(input("dois numero: "))
# # # n3 = int(input("tres numero: "))
# # # list.append(n1)
# # # list.append(n2)
# # # list.append(n3)
# # # print(calcular_total(list))

# # def antecessor_posterior(numero):
# #     return numero - 1, numero + 1


# # print(antecessor_posterior(19))


# def media(*args):
#     return sum(args) / len(args)

# print(media(1, 2, 3, 4, 5, 6, 7, 8, 9, 10))

# n1= 6
# n2= 6
# n3= 6
# def mediazinha():
#     return(n1 +  n2 + n3)/3

# print(mediazinha())

bunda = 10
# def sub():
#     bunda = 20
#     return bunda - 1

# # print(bunda)
# print(sub())

def soma():
    global bunda
    bunda + 10
    return bunda

print(soma())

salario = 2000

def aumento():
    global salario
    salario += 500
    return salario

print(aumento())