# -*- coding: utf-8 -*-
"""
Created on Fri Apr 19 19:09:52 2019

@author: dorad
"""
inventario = []

#Combate

vida_veterano = 100
vida_aluno = 100 #se ele ja tiver ganhado vidas durante o jogo, colocar aqui o valor, caso contrario, 0

while vida_veterano or vida_aluno > 0:
    import random
    x = random.randint(1,2)
    if x == 1:
        vida_veterano -= 50
    else:
        vida_aluno -= 50 
if vida_aluno > vida_veterano:
    print("Voce ganhou!")
    print("Novo item adquirido no inventario")
    inventario.append("Ingresso")
    #voltar para 
else:
    print("Voce perdeu")

#ERRO: QUANDO GANHA NÃO TA TENDO RESPOSTA