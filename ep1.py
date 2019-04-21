# EP 2019-1: Escape Insper
#
# Alunos: 
# - aluno A: Isadora Stigliani Dalberto, isadorasd@al.insper.edu.br
# - aluno B: Gabriel Lorenzo Chinelatto, gabriellcc@al.insper.edu.br

import random
inventario = []

#colocar um jogo num while, para ele poder jogar só 3 vezes, caso o contrario é jubilado :)

def carregar_cenarios():
    cenarios = {
        "casa": {
            "titulo": "Casa",
            "descricao": "Voce esta em casa",
            "opcoes": {
                "inspao": "Ir para o Inspao",
                "cafe": "ir tomar cafe da manha"
            }
        },
        "cafe": {
            "titulo": "Acoooorda seu sonolento",
            "descricao": "Voce esta tomando cafe da manha perto do insper",
            "opcoes": {
                "casa": "voltar para casa",
                "inspao": "ir para o insper"
            }
        },
        "inspao": {
            "titulo": "Saguao do perigo",
            "descricao": "Voce esta no saguao de entrada do insper",
            "opcoes": {
                "4 andar": "Tomar o elevador para o 4° andar",
                "biblioteca": "Ir para a biblioteca",
                "entidades": "Ir para a sala das entidades",
                "elevador": "Pegar o elevador para ir onde quiser"
            }
        },
        "4 andar": {
            "titulo": "Andar do desespero",
            "descricao": "Voce chegou ao andar do melhor curso do insper",
            "opcoes": {
                "mario kart": "Ir jogar mario kart com a galera",
                "professor": "Falar com o professor",
                "pizzada": "Ir para a pizzada comer muito e entrosar",
                #rever a existencia da pizzada no dicionario
                    #if ingresso not in inventario
                    # tirar o pizzada das opcoes
                "inspao": "Voltar para o saguão de entrada do Insper",
                "elevador":"pegar o elevador para ir pra onde quiser"
            }
        },
        "professor": {
            "titulo": "O monstro do Python",
            "descricao": "Voce foi pedir para o professor adiar o EP. "
                         "O professor revelou que é um monstro disfarçado "
                         "e devorou sua alma.",
            "opcoes": {}
        },
        "biblioteca": {
            "titulo": "Caverna da tranquilidade",
            "descricao": "Voce esta na biblioteca",
            "opcoes": {
                "inspao": "Voltar para o saguao de entrada",
                "4 andar": "Ir para o quarto andar",
                "entidades": "Ir para a sala das entidades",
                "livro":"ir procurar um livro sobre programacao"
#fazer com que o livro apareça em 2/3 das vezes
            },
        },
        "livro": {
            "titulo": "Esperteza pra quem sabe",
            "descricao": "Você foi esperto e encontrou um livro com anotações que irão te salvar!",
            "opcoes": {
                "pegar": "alugar o livro",
                "deixar": "não pegar o livro"
                #inventario.append
            },
        },
        "mario kart": {
            "titulo": "Cantinho das Corridas",
            "descricao": "Você está no 4° Andar jogando Mario Kart com seus amigos",
            "opcoes": {
                "4 andar": "Voltar para a entrada do 4° andar",
                "professor": "Falar com o professor que esta na sala ao lado",
                "jogar": "jogar uma partida de mario kart"
            },
        },
        "pizzada": {
            "titulo": "Pizzinha",
            "descricao": "Voce esta na pizzada com seus amigos de engenharia!",
            "opcoes": {
                "biblioteca": "Ir tentar fazer o EP na biblioteca",
                "4 andar": "Ir até a sala do professor para conversar com ele"
                #so consegue acessar se na lista tiver o ingresso (if opções pizzada...)
                #se n tiver o ingresso volta 4 andar
            },
        },
        "entidades": {
            "titulo": "Sofazin delicin",
            "descricao": "Voce esta na sala das entidades no 5° Andar",
            "opcoes": {
                "veterano": "Ir reclamar do barulho que o veterano esta fazendo",
                "4 andar": "Voltar para o 4° andar",
                "inspao": "Ir para o saguao de entrada do insper"
            },
        },
        "veterano": {
            "titulo": "Desafio",
            "descricao": "Voce esta na sala das entidades no 5° Andar, e um veterano esta fazedo muito barulho, ele aposta com voce um ingresso da pizzada que consegue te vencer num combate",
            "opcoes": {
                "aceitar": "Aceitar o combate",
                "recusar": "Ta com medo?",
                "brigar": "Não aceitar a aposta e resolver na mão"
                #brigar print: voce teve que passar um dia no hospital e perdeu o prazo do EP > perde
                #programa do combate quando aceitar
                #recusar: voltar pra sala das entidades
            },
        },
        "elevador": {
            "titulo": "Quadrado sobe desce",
            "descricao": "O elevador pode te levar para qualquer lugar que voce quiser!",
            "opcoes": {
                #lugar = input("Onde você quer ir?")
                #if lugar == IMPLEMENTAR CODIGO PARA LEVAR PARA A SALA QUE ELE CHAMAR O NOME, 
                #SE ELA NAO EXISTIR ESCREVER "TENTE OUTRO LUGAR!"
            },
        }
    }
    nome_cenario_atual = "casa"
    return cenarios, nome_cenario_atual


def main():
    print("Na hora do sufoco!")
    print("------------------")
    print()
    print("Eis que você deixa o Ep de lado: vou só jogar um pouquinho/assistir Netflix/"
        "embaçar em geral. Amanhã eu começo o EP. Mas isso não deu certo...")
    print()
    print("Amanha é o dia de entregar o EP e você está razoavelmente muito atrasado! Você está "
        "na entrada do Insper, e quer procurar o professor para pedir um "
        "adiamento do EP para a próxima semana (boa sorte...)")
    print()


    cenarios, nome_cenario_atual = carregar_cenarios()

    game_over = False
    while not game_over:
        cenario_atual = cenarios[nome_cenario_atual]

        print()
        print()
        print()
        print()
        print()
        print (cenario_atual["titulo"])
        comprimento1 = len(cenario_atual["titulo"])
        print (comprimento1*"-")
        print (cenario_atual["descricao"])
        print ("O seu inventario é: {0}".format(inventario))
        print()

        opcoes = cenario_atual['opcoes']
        if len(opcoes) == 0:
            print("Acabaram-se suas opções! Mwo mwo mwooooo...")
            game_over = True
        else:

            print ("Opcoes disponiveis:")
            for x, y in opcoes.items():                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             
                print ("{0}:{1}".format(x, y))
                #se o lugar for o elevador, não printar as opções
            
            escolha = input("O que você irá escolher?")
 #problema acessar de qualquer lugar
 #criar sala secreta
           
            if escolha in opcoes:
                nome_cenario_atual = escolha
            elif escolha =='elevador':
                nome_cenario_atual = escolha
            elif escolha == "pegar":
                inventario.append("livro")
                nome_cenario_atual = "biblioteca"
            elif escolha == "deixar":
                nome_cenario_atual = "biblioteca"
#apagar o livro do dicionario
                
#aparição de monstros - G A L O 
                
            elif escolha == 'aceitar':
#ELE NAO TA ACONTECENDO NADA QUANDO ESCOLHEMOS ESSA OPÇÃO
                vida_veterano = 100
                vida_aluno = 100 #se ele ja tiver ganhado vidas durante o jogo, colocar aqui o valor, caso contrario, 0

                while vida_veterano or vida_aluno > 0:
                    x = random.randint(1,2)
                    if x == 1:
                        vida_veterano -= 50
                    else:
                        vida_aluno -= 50 
                if vida_aluno > vida_veterano:
                    print("Voce ganhou!")
                    print("Novo item adquirido no inventario")
                    inventario.append("Ingresso")
                    nome_cenario_atual = 'entidades'
                else:
                    print("Voce perdeu")
                    nome_cenario_atual = 'entidades'
#while limite tentativas de jogo (x3)
            elif escolha == "jogar":
                x = random.randint(1,12)
                if x == 1:
                    print ("Parabens! Você conseguiu ficar em 1° lugar e por isso ganhou um prêmio!")
                    print("Novo item adquirido no inventario")
                    inventario.append("Computador para programar")
                    nome_cenario_atual = "mario kart"
                elif x == 12:
                    print ("Você ficou em último, desistiu do EP e foi pra casa chorar")
                    game_over = True
                else: 
                    print ("bom jogo! que pena que não conseguiu ficar em 1° dessa vez!")
                    nome_cenario_atual = "mario kart"                    
            else:
                print("Sua indecisão foi sua ruína!") 
                game_over = True

    print("Você morreu!")


# Programa principal.
if __name__ == "__main__":
    main()
