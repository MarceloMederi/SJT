import time

def menu():
    print("QUESTIONARIO SJT")
    time.sleep(3)

def questao():
    print("Você tem trabalhado em um projeto que, embora interessante,provou ser demorado e um tanto desafiador.\nAlgumas dessas dificuldades surgiram devido a um membro inexperiente da equipe que precisava de \napoio extra para realizar seu potencial. ")
    time.sleep(8)
    print("")
    print("Embora esta situação tenha apresentado muitos obstáculos, vocês dois conseguiram superá-los juntos e progredir. \nApesar de uma quantidade substancial de trabalho a ser feito no atual projeto, \nseu superior então pede que você lidere outro projeto envolvendo funcionários de outro departamento \ncom os quais você não está familiarizado.")
    print("")
    time.sleep(8)

def opcao():
    print("Vejamos algumas sugestões para o caso")
    print("")
    time.sleep(3)
    print("[1]- Explique honestamente ao gerente que o atual projeto e colega de trabalho inexperiente precisam de suporte até a conclusão. \nVocê prefere não abandonar o indivíduo e arriscar o projeto falhando.")
    time.sleep(4)
    print("")
    print("[2]- Assuma o segundo projeto e trabalhar horas extras para garantir que atenção suficiente possa ser dedicada a cada um. Assim, \no colega menos experiente não será abandonado e há menos chance do primeiro projeto vai falhar.")
    time.sleep(4)
    print("")
    print("[3]- Informe o gerente que você adoraria contratar outro projeto com garantias de que ambos serão entregues com sucesso. \nVocê também diz ao gerente que o colega de trabalho terá mais autonomia, mas que você estará no escritório para oferecer orientação, se necessário.")
    time.sleep(4)
    print("")
    print("[4]- Concordo com o segundo projeto e entrar em contato com o colega de trabalho inexperiente enquanto eles trabalham no primeiro projeto. \nDesta forma, você será capaz de manter um olho no primeiro projeto enquanto você gerencia o segundo.")
    time.sleep(4)

def notas():
    peso1 = 33
    peso2 = 18
    peso3 = 4
    peso4 =45

notas()
menu()
print("")
questao()
print("")
opcao()

escolha = 0


while (escolha != "1" "2" "3" "4"):
    print("")
    alternativa = int(input("Com base em sua análise quais das opções abaixo você escolheria?"))
    time.sleep(2)
    if alternativa == 1:
        print("Guardado a sua resposta.")
        break
    elif alternativa == 2:
        print("Guardado a sua resposta.")
        break
    elif alternativa == 3:
        print("Guardado a sua resposta.")
        break
    elif alternativa == 4:
        print("Guardado a sua resposta.")
    else:
        print("O NUMERO ESCOLHIDO NÃO ATENDE AS OPÇOES DO CASO.\nESCOLHA NOVAMENTE")

print("")
time.sleep(2)
print("Obrigado por Responder!")
    