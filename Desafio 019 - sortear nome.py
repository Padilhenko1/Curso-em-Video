def sortear (x):
    import random
    lista=[]
    for i in range (1,5):
        lista.append(x)
    lista=random.choice(lista)
    return


for i in range (1,5):
    nome = str(input(f'Nome {i}: '))
sortear(nome)

