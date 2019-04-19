# EP 2019-1: Escape Insper
#
# Alunos: 
# - aluno A: Isadora Stigliani Dalberto, isadorasd@al.insper.edu.br
# - aluno B: Gabriel Lorenzo Chinelatto, gabriellcc@al.insper.edu.br

inventario = []

def carregar_cenarios():
    cenarios = {
        "casa": {
            "titulo": "Casa",
            "descricao": "Voce esta em casa",
            "inventario": print(inventario),
            "opcoes": {
                "inspao": "Ir para o Inspao",
                "cafe": "ir tomar cafe da manha"
            }
        },
        "cafe": {
            "titulo": "Acoooorda seu sonolento",
            "descricao": "Voce esta tomando cafe da manha perto do insper",
            "inventario": print(inventario),
            "opcoes": {
                "casa": "voltar para casa",
                "inspao": "ir para o insper"
            }
        },
        "inspao": {
            "titulo": "Saguao do perigo",
            "descricao": "Voce esta no saguao de entrada do insper",
            "inventario": print(inventario),
            "opcoes": {
                "4 andar": "Tomar o elevador para o 4° andar",
                "biblioteca": "Ir para a biblioteca",
                "entidades": "Ir para a sala das entidades"
            }
        },
        "4 andar": {
            "titulo": "Andar do desespero",
            "descricao": "Voce chegou ao andar do melhor curso do insper",
            "inventario": print(inventario),
            "opcoes": {
                "mario kart": "Ir jogar mario kart com a galera",
                "professor": "Falar com o professor",
                "pizzada": "Ir para a pizzada comer muito e entrosar",
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
            "inventario": print(inventario),
            "opcoes": {
                "inspao": "Voltar para o saguao de entrada",
                "4 andar": "Ir para o quarto andar",
                "entidades": "Ir para a sala das entidades",
                "livro":"ir procurar um livro sobre programacao"
            },
        },
        "mario kart": {
            "titulo": "Cantinho das Corridas",
            "descricao": "Você está no 4° Andar jogando Mario Kart com seus amigos",
            "inventario": print(inventario),
            "opcoes": {
                "4 andar": "Voltar para a entrada do 4° andar",
                "professor": "Falar com o professor que esta na sala ao lado",
                "jogar": "jogar uma partida de mario kart"
            },
        },
        "pizzada": {
            "titulo": "Pizzinha",
            "descricao": "Voce esta na pizzada com seus amigos de engenharia!",
            "inventario": print(inventario),
            "opcoes": {
                "biblioteca": "Ir tentar fazer o EP na biblioteca",
                "4 andar": "Ir até a sala do professor para conversar com ele"
            },
        },
        "entidades": {
            "titulo": "Sofazin delicin",
            "descricao": "Voce esta na sala das entidades no 5° Andar",
            "inventario" : print(inventario),
            "opcoes": {
                "veterano": "Ir reclamar do barulho que o veterano esta fazendo",
                "4 andar": "Voltar para o 4° andar",
                "inspao": "Ir para o saguao de entrada do insper"
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
        print (cenario_atual["titulo"])
        comprimento1 = len(cenario_atual["titulo"])
        print (comprimento1*"-")
        print (cenario_atual["descricao"])
        print (cenario_atual["inventario"])
        print()

        opcoes = cenario_atual['opcoes']
        if len(opcoes) == 0:
            print("Acabaram-se suas opções! Mwo mwo mwooooo...")
            game_over = True
        else:

            print ("Opcoes disponiveis:")
            for x, y in opcoes.items():                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             
                print ("{0}:{1}".format(x, y))
            
            escolha = input("O que você irá escolher?")
            
            if escolha in opcoes:
                nome_cenario_atual = escolha
            elif escolha =='elevador':
                nome_cenario_atual = escolha
            else:
                print("Sua indecisão foi sua ruína!") 
                game_over = True

    print("Você morreu!")


# Programa principal.
if __name__ == "__main__":
    main()
