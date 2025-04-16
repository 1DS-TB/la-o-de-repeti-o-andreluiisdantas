import random
from logging import critical

#Definindo o ataque
ataque_jogador_1 = random.randint(1, 51)
ataque_jogador_2 = random.randint(1, 51)

#Definindo a defesa
defesa_jogador_1 = random.randint(1, 51)
defesa_jogador_2 = random.randint(1, 51)

#Fazendo com que o ataque não seja menor que a defesa
while ataque_jogador_1 < defesa_jogador_2:
    ataque_jogador_1 = random.randint(1, 51)

while ataque_jogador_2 < defesa_jogador_1:
    ataque_jogador_2 = random.randint(1, 51)

#Definindo o valor da cura
cura = 20

#Resultado do ataque
resultado_ataque = 0

#Definindo a quantidade de vida
vida = random.randint(200, 1001)

#Atribuindo o valor da vida para os dois jogadores
vida_jogador_1 = vida
vida_jogador_2 = vida

#Definindo o turno
turno = 0

# Menu para definir o modo de jogo
menu = int(input(
"""
=== DUELO DE HERÓIS ===
[1] - Singleplayer (vs CPU)
[2] - Multiplayer
[3] - Sair
"""
))

# Modos de jogo
if menu == 1:
    multiplayer = False
elif menu == 2:
    multiplayer = True
else:
    print("Saindo...")
    exit()

print(
f"""
=== DUELO DE HERÓIS ===
=== Jogador 1 ===
HP: {vida_jogador_1}
ATQ: {ataque_jogador_1}          DEF: {defesa_jogador_1}

=== Jogador 2 ===
HP: {vida_jogador_2}
ATQ: {ataque_jogador_2}          DEF: {defesa_jogador_2}
"""
)

while vida_jogador_1 > 0 and vida_jogador_2 > 0:
    turno += 1

    critico = random.randint(1, 10) == 10

    print(
    f"""
    === Turno {turno} ===
    Jogador 1 HP: [{vida_jogador_1}] | Jogador 2 HP: [{vida_jogador_2}]
    """)

    opcao = int(input(
        f'''
        JOGADOR 1
        Sua vez: [1] Atacar ou [2] Curar?
        '''))

    if opcao == 1:

        critico = random.randint(1, 10) == 10

        if critico:
            ataque_jogador_1 = ataque_jogador_1 * 2
            print("Ataque critico")
        else:
            resultado_ataque = ataque_jogador_1 - defesa_jogador_2
            vida_jogador_2 = vida_jogador_2 - resultado_ataque

        print(f"Você ataca! Jogador 2 perde {resultado_ataque} HP.")


    elif opcao == 2:
        if vida_jogador_1 + cura > vida:
            vida_jogador_1 = vida
        else:
            vida_jogador = vida_jogador_1 + cura
        print(f"Você curou! Vida jogador 1: {vida_jogador_1}")

    else:
        print("Opção invalida")
        continue

    if multiplayer:
        opcao = int(input(
            f'''
                JOGADOR 2
                Sua vez: [1] Atacar ou [2] Curar?
            
            '''))
    else:
        opcao = random.randint(1, 2)

        critico = random.randint(1, 10) == 10

        if critico:
            ataque_jogador_2 = ataque_jogador_2 * 2
            print("Ataque critico")
        else:
            resultado_ataque = ataque_jogador_1 - defesa_jogador_2
            vida_jogador_2 = vida_jogador_2 - resultado_ataque

        if opcao == 1:
            resultado_ataque = ataque_jogador_2 - defesa_jogador_1
            vida_jogador_1 = vida_jogador_1 - resultado_ataque

            print(f"Você ataca! Jogador 1 perde {resultado_ataque} HP.")

        elif opcao == 2:
            if vida_jogador_2 + cura > vida:
                vida_jogador_2 = vida
            else:
                vida_jogador = vida_jogador_2 + cura
            print(f"Você curou! Vida jogador 2: {vida_jogador_2}")

        else:
            print("Opção invalida")
            continue

if vida_jogador_1 == 0:
    print("Jogador 2 Venceu")
else:
    print("Jogador 1 Venceu")