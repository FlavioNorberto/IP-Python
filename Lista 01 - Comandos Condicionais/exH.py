string_fase1= str(input())

timer = 0
perigo = 0

lingotes = 0
portal = 0
camas = 0
troia = 0
vivo = 1
ovo = 0
perolas = 0

print('Byte: Au! Vou conseguir esse ovo!!')

#FASE 1:
if vivo == 1:
    timer += len(string_fase1) * 5
    if string_fase1.isupper():
       perigo += 30
    else:
       perigo += 10

    if 'monstros' in string_fase1.lower():
           perigo += 25
           timer += 20
           print('Você não pode dormir agora, há monstros por perto.')
           if '4' in string_fase1.lower():
              perigo *= 2
              print('Byte desbloqueou a conquista: [Caçador de Monstros]')
    if 'ferro' in string_fase1.lower():
            perigo -= 15
            timer += 5
            print('Byte desbloqueou a conquista: [A Idade do Ferro]')
    if 'diamante' in string_fase1.lower():
            if 'ferro' in string_fase1.lower():
               perigo -= 40
               print('Byte desbloqueou a conquista: [Diamantes!]')
            else:
               timer += 15
    if 'ouro' in string_fase1.lower():
            if 'ferro' in string_fase1.lower():
               timer += 10
               lingotes= 1      
            else:
               timer += 5
    if 'estrutura' in string_fase1.lower():
        estrutura = str(input())

        if 'vila' in estrutura.lower():
            timer += 10
            print('Byte desbloqueou a conquista: [Negócio Fechado!]')
            camas= 1
        if 'portal' in estrutura.lower():
            portal = 1
        if 'templo' in estrutura.lower():
            perigo += 100
        if 'mansao' in estrutura.lower():
            if perigo > 100:
                print('Byte desbloqueou a conquista: [À beira da Morte]')
            perigo -= 150
            timer += 40
        if 'camara' in estrutura.lower():
              timer += 60
              perigo += 50
              print('Byte desbloqueou a conquista: [Minecraft: Jogos Vorazes]')
   
    if perigo < 0:
        perigo = 0
    elif perigo > 100:
       vivo = 0

    if vivo == 1:
       print(f'Byte: Ufa, finalmente acabei, demorei apenas {timer} minutos, vamos ao Nether!')

#FASE 2:
if vivo == 1:
    # Portal:
    if portal == 0:
        # Coletar as obsidians
        timer += 5
        print('Byte desbloqueou a conquista: [Entrando numa fria]')
        portal = 1

    # Entrar no Nether
    if portal == 1:
         perigo += 30
         print('Byte desbloqueou a conquista: [O buraco é mais embaixo]')

         n1= float(input())
         n2= float(input())
         soma= n1 + n2

         if soma == int(soma):
              #pegou as perolas
              perolas = 1
         elif soma != int(soma) and lingotes == 0:
              perigo += 20
              timer += 30
              perolas = 1
         elif soma != int(soma) and lingotes == 1:
              perigo += 10
              perolas = 1
              print('Byte desbloqueou a conquista: [Meu precioso!]')

    resultado_blaze = str(input())

    if resultado_blaze.isnumeric():
        numero = int(resultado_blaze)
        if numero >= 1 and numero <= 12:
            timer += 20
        elif numero > 12:
            timer += 10
        else:
            timer += 30
            perigo += 40
    else:
        timer += 30
        perigo += 40

    if perigo < 0:
        perigo = 0
    if perigo > 100:
        vivo = 0

#FASE 3:
if vivo == 1:

    perigo -= 20

    x = int(input())
    z = int(input())

    #distancia = int(((100 - x) ** 2 + (200 - z) ** 2) ** 1/2)
    distancia = ((100 - x)**2 + (200 - z)**2)
    distancia1 = int(distancia**0.5)

    timer += (distancia1 * 2)

    print(f'Byte: Estou a {distancia1} blocos da Stronghold!')

    if perigo < 0:
         perigo = 0

#chegada ao the end:
    perigo += 30


    if timer > 300:
    # Byte falha na missão
       print('Troia desbloqueou a conquista: [Liberte o End]')
       print('Byte desbloqueou a conquista: [É o fim?]')
       ovo = 0
       troia = 1


    elif camas == 1:
         print('Byte desbloqueou a conquista: [É o fim?]')
         perigo -= 30
         ovo = 1
         print('Byte: Como eu amo o [Design Intencional do Jogo]!')
    elif timer >= 180 and timer <= 300:
         troia = 1
         perigo += 10
         print('Troia desbloqueou a conquista: [É o fim?]')
         print('Byte desbloqueou a conquista: [É o fim?]')

         n_flechas = int(input())
         n_alvos = int(input())

         if n_alvos == 1:
            if n_flechas == 1:
                print('Byte: Uma flecha, Uma chance.')
            else:
                print('Byte: Troia já destruiu todos os cristais, agora é só o Dragão...')


         if  n_flechas % n_alvos == 0 and n_flechas // n_alvos > 0:
            timer += 10
            # troia = 0
            ovo = 1
            print('Byte desbloqueou a conquista: [Liberte o End]')
         else:
            timer += 20
            # troia = 1
            ovo = 0
            print('Byte: Droga! Não tenha flechas suficientes, Troia vai ganhar...')
    elif timer < 300: 
            print('Byte desbloqueou a conquista: [É o fim?]')
            troia = 0
            timer += 5
            ovo = 1
            print('Byte desbloqueou a conquista: [Liberte o End]')
   
    if perigo < 0:
        perigo = 0

    if perigo > 100:
        vivo = 0
        ovo = 0


#RESULTADO FINAL:
if vivo == 0:
    print('Byte foi morto.')

if ovo == 1:
    print('Byte desbloqueou a conquista: [A nova geração]')
    print('Byte: Aauauau! O ovo é meu! que rolem os créditos!')
else:
    print('Byte: auu.... Não consegui pegar o ovo...')

#RELATÓRIO:
print()

if perigo == 100 or troia == 1:
    classificação = 'Odisseia de Byte.'
elif perigo < 30:
    classificação = 'Passeio no Parque.'
elif perigo >= 30 and perigo < 70:
    classificação = 'Jornada Complicada.'
elif perigo >= 70 and perigo < 100:
    classificação = 'Aventura Perigosa.'
elif perigo > 100:
    classificação = 'Letal.'

print(f'🚨Avaliação de nível de perigo: {classificação}')

print()

horas = timer// 60
minutos_finais= timer % 60

print(f'Timer: {horas} h e {minutos_finais} minutos')