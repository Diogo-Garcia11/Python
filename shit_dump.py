print("Hello,World!")
print( 11 + 10 + 1000)
print( 1.5 + 2.5 + 1 + 0.5)
print(True)
print(False)


print("Python" + 'é' + """legal""" + '''!''')
diogo = 11
diogo2= 12
print( diogo + diogo2)

print (f'diogo + diogo2 = {diogo} {diogo2}')

print (3//2)

saldo = 300

saque = 300

if saldo <= saque and saldo >= saque:
    
    print(True)
    
else:
    
    print(False)
    

print(saldo is saque)


print(saldo is 1000)
print(saldo is not 300)
print(saldo is 300)

print(300 is 300)

N1=6
N2=5
N3=5

def media(Nota1,Nota2,Nota3):
    
    media1 = (float(Nota1) + float(Nota2) + float(Nota3)) / 3
    
    if (media1 >= 5):
        
        if(float(Nota1)>5):
            print("boa ta aprendendo")
    else:
        print("boa garotao")
        
    return media1 

print(media(N1,N2,N3))


def sacar(valor):
    
    saldo = 200
    if saldo >= valor:
        
        print("boa garotao")  
        
                
sacar(100)


string = "bunda"
tamanho = len(string)

print(f'tamanho da sua bunda {tamanho}')  

Maior_idade = 18

idade= 18

if idade >= Maior_idade:
    print("Maior de idade")
if idade < Maior_idade:
    print("Menor de idade")    


Status = "Sucesso" if saldo == saque else "Falha"

print(f'{Status} na sua transação')

numero= 1

for numero in range(numero, 11):
    
    if numero % 2 == 0:
        
        print(f'{numero} é par')
    
    else:
        
        print(f'{numero} é impar')
    

while numero < 11:
    if numero % 2 == 0:
        print(f'{numero} é par')
    else:
        print(f'{numero} é impar')
    numero += 1
