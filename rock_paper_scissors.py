from random import randint
import time

a = 0
c = 0
d = 1
print('-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-')
print('§§§§§§§§§§§ JOKENPÔ §§§§§§§§§§§')
print('-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-')

time.sleep(1)
print('CARREGANDO JOGO...')
time.sleep(2)

while c == 0:
    b = randint(1, 3) #print(b)
    if c == 0:

        while True:
            try:
                a = int(input('(1) PEDRA\n(2) PAPEL\n(3) TESOURA\n Digite: '))
                if a in [1, 2, 3]:
                    break
                else:
                    print('DIGITE APENAS NÚMEROS ENTRE 1 e 3') 
            except ValueError:
                print('OPÇÃO INVÁLIDA / DIGITE APENAS NÚMEROS')

        time.sleep(0.5)
        print('JO')
        time.sleep(0.5)
        print('KEN')
        time.sleep(0.5)
        print('PÔ!')
        time.sleep(1)

        if b == 1:
            print('-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-')
            print('O computador jogou PEDRA!')
            if a == 1:
                print('Você jogou PEDRA!\nEMPATE')
                print('-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-')
            elif a == 2:
                print('Você jogou PAPEL!\nPARABÉNS VOCÊ VENCEU')
                print('-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-')
                c = 1
            else:
                print('Você jogou TESOURA!\nPERDEU')
                print('-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-')        
        
        elif b == 2:
            print('-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-')
            print('O computador jogou PAPEL!')
            if a == 2:
                print('Você jogou PAPEL!\nEMPATE')
                print('-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-')
            elif a == 3:
                print('Você jogou TESOURA!\nPARABÉNS VOCÊ VENCEU')
                print('-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-')
                c = 1
            else:
                print('Você jogou PEDRA!\nPERDEU')
                print('-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-')

        elif b == 3:
            print('-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-')
            print('O computador jogou TESOURA!')
            if a == 3:
                print('Você jogou TESOURA!\nEMPATE')
                print('-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-')
            elif a == 1:
                print('Você jogou PEDRA!\nPARABÉNS VOCÊ VENCEU')
                print('-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-')
                c = 1
            else:
                print('Você jogou PAPEL!\nPERDEU')
                print('-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-')
        else:
            print('ERROR: Erro inesperado, rode ou programa novamente ou reinicie')

    #d = input('APERTE ENTER PARA SAIR DO JOGO')