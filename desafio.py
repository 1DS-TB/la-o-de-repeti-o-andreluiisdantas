import random

print("""
==================================
== Bem-vindo ao Duelo de Heróis ==
==================================""")

menu = int(input("""
====== MENU ======

[1] - Singleplayer
[2] - Multiplayer
[3] - Sair
"""))

cura = 0

dano_ataque = 0

turno = 0

vida = random.randint(1, 15)

vida_jogador_1 = vida
vida_jogador_2 = vida
vida_maquina = vida

ataque_jogador_1 = random.randint(1, 5)
ataque_jogador_2 = random.randint(1, 5)
ataque_maquina = random.randint(1, 5)

defesa_jogador_1 = random.randint(1, 5)
defesa_jogador_2 = random.randint(1, 5)
defesa_maquina = random.randint(1, 5)

while ataque_jogador_1 <= defesa_jogador_2:
    ataque_jogador_1 = random.randint(1, 5)

while ataque_jogador_2 <= defesa_jogador_1:
    ataque_jogador_2 = random.randint(1, 5)

while ataque_jogador_1 <= defesa_maquina:
    ataque_jogador_1 = random.randint(1, 5)

while ataque_maquina <= defesa_jogador_1:
    ataque_maquina = random.randint(1, 5)

critico = ['critico', 'dobro_critico']
chance = [1.1, 1]

opcao = 0
acao_maquina = 0

if menu == 1:

    print(f'=== Inicio Partida ===')

    print(f"""
=== DUELO DE HERÓIS ===
===       Você      ===
HP: {vida_jogador_1}
ATQ: {ataque_jogador_1}          DEF: {defesa_jogador_1}

===      Inimigo    ===
HP: {vida_maquina}
ATQ: {ataque_maquina}          DEF: {defesa_maquina}
""")

    while vida_jogador_1 > 0 and vida_maquina > 0:

        turno += 1
        print(f'--- Turno {turno} ---')
        print(f'Seu HP: {vida_jogador_1} | Inimigo HP: {vida_maquina}')


        acao_maquina = random.choice(["atacar", "curar"])

        if vida_jogador_1 < (vida * 0.5):
            print("Você pode dar um ataque critico")
            ataque_critico = int(input("Você quer fazer o ataque critico:\n [1] Sim\n [2] Não"))

            if ataque_critico == 1:
                dano_critico = random.choices(critico, weights=chance, k=1)
                if dano_critico == 'critico':
                    dano_ataque = dano_ataque + (dano_ataque * 0.2)
                else:
                    dano_ataque = dano_ataque * 2
            elif ataque_critico == 2:
                print("Ataque critico não executado")
                continue
            else:
                print("Opção invalida")
        else:
            opcao = int(input("Sua vez: [1] Atacar ou [2] Curar?"))

            match opcao:
                case 1:
                    # Ataque de jogador contra inimigo
                    dano_ataque = ataque_jogador_1 - defesa_maquina
                    vida_maquina = vida_maquina - dano_ataque

                    print(f"Você ataca! Inimigo perde {dano_ataque} HP.")
                case 2:
                    if vida_jogador_1 + cura > vida:
                        vida_jogador_1 = vida
                    else:
                        vida_jogador_1 = vida_jogador_1 + cura
                    print(f"Você curou! Sua vida agora é: {vida_jogador_1}")

                case _:
                    print("Inválido")

            if acao_maquina == "atacar":
                dano_ataque = ataque_maquina - defesa_jogador_1
                vida_jogador_1 = vida_jogador_1 - dano_ataque
                print(f'Inimigo ataca! Você perde {dano_ataque} HP.\n')
            else:
                if vida_maquina + cura > vida:
                    vida_maquina = vida
                else:
                    vida_maquina = vida_maquina + cura
                print(f'inimigo cura! Vida dele está {vida_maquina} HP.\n')


elif menu == 2:

    print(f"""
        === DUELO DE HERÓIS ===
        
        ===     Jogador 1   ===
        HP: {vida_jogador_1}
        ATQ: {ataque_jogador_1}          DEF: {defesa_jogador_1}

        ===     Jogador 2   ===
        HP: {vida_jogador_2}
        ATQ: {ataque_jogador_2}          DEF: {defesa_jogador_2}
        """)


    while vida_jogador_1 > 0 and vida_jogador_2 > 0:

        turno += 1
        print(f'--- Turno {turno} ---')
        print(f'Seu HP: {vida_jogador_1} | Inimigo HP: {vida_jogador_2}')

        print("Jagador 1")
        opcao_jogador1 = int(input("Sua vez: [1] Atacar ou [2] Curar?"))


        if opcao_jogador1 == 1:
            dano_ataque = ataque_jogador_1 - defesa_jogador_2
            vida_jogador_2 = vida_jogador_2 - dano_ataque

            print(f"Jogador 1 ataca! Adversário perde {dano_ataque} HP.")

            print(f'Jogador 1 HP: {vida_jogador_1} | Jogador 2 HP: {vida_jogador_2}\n')


        elif opcao_jogador1 == 2:
            if vida_jogador_1 + cura > vida:
                vida_jogador_1 = vida
            else:
                vida_jogador_1 = vida_jogador_1 + cura
            print(f"Você curou! Sua vida agora é: {vida_jogador_1}")

            print(f'Jogador 1 HP: {vida_jogador_1} | Jogador 2 HP: {vida_jogador_2}\n')
        else:
            print("Opção Inválida! - Perdeu a vez\n")
            continue

        print("Jagador 2")
        opcao_jogador2 = int(input("Sua vez: [1] Atacar ou [2] Curar?"))


        if opcao_jogador2 == 1:
            dano_ataque = ataque_jogador_2 - defesa_jogador_1
            vida_jogador_1 = vida_jogador_1 - dano_ataque

            print(f"Jogador 2 ataca! Adversário perde {dano_ataque} HP.")

            print(f'Jogador 1: {vida_jogador_1} | Jogador 2 HP: {vida_jogador_2}\n')
        elif opcao_jogador2 == 2:
            if vida_jogador_2 + cura > vida:
                vida_jogador_2 = vida
            else:
                vida_jogador_2 = vida_jogador_2 + cura
            print(f"Você curou! Sua vida agora é: {vida_jogador_2}")

            print(f'Jogaodor 2 HP: {vida_jogador_1} | Jogador 2 HP: {vida_jogador_2}\n')
        else:
            print("Opção Inválida! - Perdeu a vez\n")

    if vida_jogador_1 > vida_maquina:
        print(f'Jogador 1 venceu a partida singleplayer!')
    elif vida_maquina > vida_jogador_1:
        print(f'A maquina venceu a partida singleplayer!')

    if vida_jogador_1 > vida_jogador_2:
        print(f'jogador 1 venceu a partida multiplayer!')
    elif vida_jogador_2 > vida_jogador_1:
        print(f'jogador 2 venceu a partida multiplayer!')

elif menu == 3:
    print("Saindo...")

