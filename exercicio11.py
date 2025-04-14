import random

#Definindo o ataque
ataque_jogador = random.randint(1, 51)
ataque_inimigo = random.randint(1, 51)

#Definindo a defesa
defesa_jogador = random.randint(1, 51)
defesa_inimigo = random.randint(1, 51)

#Fazendo com que o ataque não seja menor que a defesa
while ataque_jogador < defesa_inimigo:
    ataque_jogador = random.randint(1, 51)

while ataque_inimigo < defesa_jogador:
    ataque_inimigo = random.randint(1, 51)

#Definindo o valor da cura
cura = 20

#Resultado do ataque
resultado_ataque = 0

#Definindo a quantidade de vida
vida = random.randint(200, 1001)

#Atribuindo o valor da vida para os dois jogadores
vida_jogador = vida
vida_inimigo = vida

#Definindo o turno
turno = 0

#Opção
opcao = ''


print(f"""
=== DUELO DE HERÓIS ===
=== Você            ===
HP: {vida_jogador}
ATQ: {ataque_jogador}          DEF: {defesa_jogador}

=== Inimigo         ===
HP: {vida_inimigo}
ATQ: {ataque_inimigo}          DEF: {defesa_inimigo}
""")

while vida_jogador > 0 and vida_inimigo > 0:
    turno += 1
    print(f'--- Turno {turno} ---')
    print(f'Seu HP: {vida_jogador} | Inimigo HP: {vida_inimigo}')

    opcao = int(input("Sua vez: [1] Atacar ou [2] Curar?"))

    escolha_inimigo = random.choice(["atacar", "curar"])

    match opcao:
        case 1:
            #Ataque de jogador contra inimigo
            resultado_ataque = ataque_jogador - defesa_inimigo
            vida_inimigo = vida_inimigo - resultado_ataque

            print(f"Você ataca! Inimigo perde {resultado_ataque} HP.")

            if escolha_inimigo == "atacar":
                resultado_ataque = ataque_inimigo - defesa_jogador
                vida_jogador = vida_jogador - resultado_ataque
                print(f'Inimigo ataca! Você perde {resultado_ataque} HP.\n')
            else:
                if vida_inimigo + cura > vida:
                    vida_inimigo = vida
                else:
                    vida_inimigo = vida_inimigo + cura
                print(f'inimigo cura! Vida dele está {vida_inimigo} HP.\n')

        case 2:
            if vida_jogador + cura > vida:
                vida_jogador = vida
            else:
                vida_jogador = vida_jogador + cura
            print(f"Você curou! Sua vida agora é: {vida_jogador}")

            if escolha_inimigo == "atacar":
                resultado_ataque = ataque_inimigo - defesa_jogador
                vida_jogador = vida_jogador - resultado_ataque
                print(f'Inimigo ataca! Você perde {resultado_ataque} HP.\n')
            else:
                if vida_inimigo + cura > vida:
                    vida_inimigo= vida
                else:
                    vida_inimigo = vida_inimigo + cura
                print(f'inimigo cura! Vida dele está {vida_inimigo} HP.\n')

        case _:
            print("Inválido")

if vida_jogador > vida_inimigo:
    print(f'Você venceu!')
else:
    print(f'Você perdeu!')