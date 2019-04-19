# -*- coding: utf-8 -*-
"""
Created on Wed Apr 17 18:44:00 2019

@author: dorad
"""
#Combate
vida_veterano = 100
vida_aluno = 100 #se ele ja tiver ganhado vidas durante o jogo, colocar aqui o valor, caso contrario, 0

while vida_veterano or vida_aluno > 0:
    import random
    x = random.randint(1,2)
    if x == 1:
        vida_veterano -= 10
        print ("Voce socou o veterano!")
    else:
        vida_aluno -= 10 
        print ("Você tomou dano!") #fazer voltar para o saguao de entrada
        