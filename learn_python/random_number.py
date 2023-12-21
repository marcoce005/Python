import random

n = random.randint(0, 10)           ## estrarre a un numero random tra due variabili
print (n)

x = random.random()     ## estrae qualsiasi numero
print (x)

gioco = ['carta', 'forbice', 'sasso']       ## sceglie tra le possibilità date
y = random.choice(gioco)
print (y)

carte = [1, 2, 3, 4, 5, 6, 7, 8, 9, "J", "Q", "K", "A"]     ## mischia la lista
random.shuffle(carte)
print (carte)