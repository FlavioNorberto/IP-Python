login = str(input())
senha = str(input())

pontos = 0
faltam = 1 - pontos

print('Byte irá julgar a sua senha.')

# Checando requisitos básicos
if len(senha) >= 8 and any(c.isalpha() for c in senha) and any(c.isnumeric() for c in senha) and " " not in senha:
    print("Vamos fazer a contagem dos pontos.")

    # Pontos por tamanho da senha
    if len(senha) > 11:
        pontos = len(senha) - 11

    if len(senha) > 14:
        print('Que senha grande! Não seria difícil esquecer dela.')

    # Pontos por uso de letras maiúsculas e minúsculas
    if any(c.isupper() for c in senha) and any(c.islower() for c in senha):
        pontos += 5

    # Checando caracteres especiais
    if "@" in senha:
        pontos += 1

    if "_" in senha:
        pontos += 1

    if "&" in senha:
        pontos += 1

    if "%" in senha:
        pontos += 1

    if "#" in senha:
        pontos += 1

    # Checando se o loguin ta dentro da senha. O .lower transforma tudo para minúsculo para poder comparar
    if login.lower() in senha.lower():
        pontos -= 10
        print('Olha o que eu encontrei aqui, não deixarei isso passar tão fácil.')

    # Recontagem de quantos pontos faltam
    faltam = 1 - pontos

    # Contagem de pontos
    if pontos < 1:
        print('Infelizmente terá que mudar sua senha, é para o seu bem.')
        print(f'Melhore sua senha em {faltam} ponto(s) e ela será suficiente.')
    elif pontos > 0 and pontos < 11:
        print('Pode manter a sua senha, ela parece adequada.')
    elif pontos > 10:
        print('Parabéns! Nem o maior hacker do mundo encontraria uma senha assim.')

else:
    print("Essa senha nem chega perto do que eu aceito. Tente de novo.")

# Uma coisa importante: isalpha() e isnumeric() verificam se a string inteira é composta por letras/números, por isso tava dando erro quando eu fazia (senha.isnumeric() and senha.isalpha()), eu estou exigindo que a senha seja numérica E alfabética ao mesmo tempo. Isso é impossível para uma string comum. Agora any(...) permite verificar se existe pelo menos um caractere desse tipo. Esse c é só uma variável que representa cada caractere da senha, um por vez.