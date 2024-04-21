import random


numero =[random.randrange(1,10)]
print (numero)
numeros =[random.randrange(1,10) for i in range(10)]

print (numeros)

for i in range(10):
    print(', '.join (str(random.randrange(1,10)) for i in range(10)))
        

for i in range(10):
    print(', '.join (str(random.randrange(1,10)) for i in range(random.randrange(1,10))))

while True:
    for i in range(10):
        print(', '.join (str(random.randrange(0,2)) for i in range(random.randrange(1,10))))


while True:
    for i in range(10):
        print(', '.join (str(random.randrange(1,10)) for i in range(10)))

for i in range(10):
    print(random.choice('abcdefghijklmnopqrstuvwxyz'))

for i in range(10):
    print(', '.join(str(random.choice('abcdefghijklmnopqrstuvwxyz')) for i in range(10)))


while True:
    for i in range(10):
        print(random.choice('abcdefghijklmnopqrstuvwxyz'))