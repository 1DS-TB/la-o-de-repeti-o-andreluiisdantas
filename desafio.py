import random

ataque_jogador_1 = random.randint(1, 51)
ataque_jogador_2 = random.randint(1, 51)
defesa_jogador_1 = random.randint(1, 51)
defesa_jogador_2 = random.randint(1, 51)

while ataque_jogador_1 < defesa_jogador_2:
    ataque_jogador_1 = random.randint(1, 51)
while ataque_jogador_2 < defesa_jogador_1:
    ataque_jogador_2 = random.randint(1, 51)

cura = 20

vida = random.randint(200, 1001)
vida_jogador_1 = vida
vida_jogador_2 = vida

turno = 0

forca_turnos_1 = 0
forca_turnos_2 = 0
veneno_turnos_1 = 0
veneno_turnos_2 = 0
regeneracao_turnos_1 = 0
regeneracao_turnos_2 = 0
escudo_ativo_1 = False
escudo_ativo_2 = False

tela_azul_1 = 0
tela_azul_2 = 0
loop_infinito_1 = False
loop_infinito_2 = False
buffer_overflow_1 = False
buffer_overflow_2 = False

usou_cache_1 = False
usou_cache_2 = False

while True:
    menu = int(input(
        """
        === DUELO DE HERÓIS ===
        [1] - Singleplayer (vs CPU)
        [2] - Multiplayer
        [3] - Sair
        [4] - Regras do Jogo
        """
    ))

    if menu == 1:
        multiplayer = False
        break
    elif menu == 2:
        multiplayer = True
        break
    elif menu == 3:
        print("Saindo...")
        exit()
    elif menu == 4:
        print(
            """
            === REGRAS DO JOGO ===
    
            OBJETIVO:
            Reduzir a vida do oponente a 0 utilizando ataques, itens e efeitos especiais.
    
            AÇÕES POR TURNO:
            [1] Atacar - Causa dano baseado no ataque do jogador menos a defesa do oponente.
                         10% de chance de causar o dobro do dano (Crítico).
            [2] Curar - Recupera 20 pontos de vida.
    
            ITENS:
            [3] Poção de Força - Aumenta o ataque (x2) por 2 turnos.
            [4] Poção de Regeneração - Recupera 15 de vida por turno durante 3 turnos.
            [5] Poção de Veneno - Faz o oponente perder 5% do HP máximo por 3 turnos.
            [6] Escudo - Bloqueia completamente o próximo ataque recebido.
    
            STATUS (só podem ser usados uma vez por partida):
            [7] Buffer Overflow - O inimigo perde 5% do HP máximo a cada turno.
            [8] Loop Infinito - O inimigo perde 1 turno.
            [9] Tela Azul - Reduz a defesa do inimigo para 0 por 2 turnos.
            [10] Cache Hit - Recupera 30% do HP máximo (só pode ser usado se estiver com menos de 25% da vida).
    
            MODO DE JOGO:
            - Singleplayer: você joga contra a CPU.
            - Multiplayer: dois jogadores humanos se enfrentam, um por vez.
    
            Boa sorte no duelo!
            """
        )

        input("Pressione Enter para voltar ao menu...")

    else:
        print("Opção inválida.")

print(
    f"""
=== JOGADOR 1 ===
HP: {vida_jogador_1} | ATQ: {ataque_jogador_1} | DEF: {defesa_jogador_1}
=== JOGADOR 2 ===
HP: {vida_jogador_2} | ATQ: {ataque_jogador_2} | DEF: {defesa_jogador_2}
"""
)

while vida_jogador_1 > 0 and vida_jogador_2 > 0:
    turno += 1

    print(f"\n=== TURNO {turno} ===")
    print(f"Jogador 1 HP: [{vida_jogador_1}] | Jogador 2 HP: [{vida_jogador_2}]")

    if veneno_turnos_1 > 0:
        dano_veneno = int(vida * 0.05)
        vida_jogador_1 -= dano_veneno
        print(f"Jogador 1 sofre {dano_veneno} de veneno.")
        veneno_turnos_1 -= 1

    if veneno_turnos_2 > 0:
        dano_veneno = int(vida * 0.05)
        vida_jogador_2 -= dano_veneno
        print(f"Jogador 2 sofre {dano_veneno} de veneno.")
        veneno_turnos_2 -= 1

    if buffer_overflow_1:
        dano_overflow = int(vida * 0.05)
        vida_jogador_1 -= dano_overflow
        print(f"Jogador 1 sofre {dano_overflow} de Buffer Overflow.")

    if buffer_overflow_2:
        dano_overflow = int(vida * 0.05)
        vida_jogador_2 -= dano_overflow
        print(f"Jogador 2 sofre {dano_overflow} de Buffer Overflow.")

    if regeneracao_turnos_1 > 0:
        vida_jogador_1 = min(vida_jogador_1 + 15, vida)
        print("Jogador 1 regenera 15 de vida.")
        regeneracao_turnos_1 -= 1

    if regeneracao_turnos_2 > 0:
        vida_jogador_2 = min(vida_jogador_2 + 15, vida)
        print("Jogador 2 regenera 15 de vida.")
        regeneracao_turnos_2 -= 1

    if tela_azul_1 > 0:
        defesa_jogador_1_backup = defesa_jogador_1
        defesa_jogador_1 = 0
        tela_azul_1 -= 1
    else:
        defesa_jogador_1 = defesa_jogador_1_backup if 'defesa_jogador_1_backup' in locals() else defesa_jogador_1

    if tela_azul_2 > 0:
        defesa_jogador_2_backup = defesa_jogador_2
        defesa_jogador_2 = 0
        tela_azul_2 -= 1
    else:
        defesa_jogador_2 = defesa_jogador_2_backup if 'defesa_jogador_2_backup' in locals() else defesa_jogador_2

    if not loop_infinito_1:
        opcao = int(input(
            f'''
        JOGADOR 1 - Sua vez:
        [1] Atacar
        [2] Curar
        Itens:
        [3] Poção de Força
        [4] Poção de Regeneração
        [5] Poção de Veneno
        [6] Escudo
        Status:
        [7] Buffer Overflow
        [8] Loop Infinito
        [9] Tela Azul
        [10] Cache Hit
        '''))

        if opcao == 1:
            critico = random.randint(1, 10) == 10
            ataque = ataque_jogador_1 * (2 if critico or forca_turnos_1 > 0 else 1)
            if escudo_ativo_2:
                print("Ataque bloqueado pelo escudo do Jogador 2!")
                escudo_ativo_2 = False
            else:
                dano = max(ataque - defesa_jogador_2, 0)
                vida_jogador_2 -= dano
                print(f"Jogador 1 ataca! Jogador 2 perde {dano} HP.")
            if critico:
                print("Ataque Crítico!")
        elif opcao == 2:
            vida_jogador_1 = min(vida_jogador_1 + cura, vida)
            print("Jogador 1 se curou.")
        elif opcao == 3:
            forca_turnos_1 = 2
            print("Poção de Força ativada por 2 turnos.")
        elif opcao == 4:
            regeneracao_turnos_1 = 3
            print("Poção de Regeneração ativa por 3 turnos.")
        elif opcao == 5:
            veneno_turnos_2 = 3
            print("Poção de Veneno usada em Jogador 2.")
        elif opcao == 6:
            escudo_ativo_1 = True
            print("Escudo ativado, próximo ataque será bloqueado.")
        elif opcao == 7:
            buffer_overflow_2 = True
            print("Jogador 2 sofreu Buffer Overflow.")
        elif opcao == 8:
            loop_infinito_2 = True
            print("Jogador 2 travou em Loop Infinito.")
        elif opcao == 9:
            tela_azul_2 = 2
            print("Jogador 2 sofreu Tela Azul por 2 turnos.")
        elif opcao == 10:
            if not usou_cache_1 and vida_jogador_1 < vida * 0.25:
                vida_jogador_1 += int(vida * 0.3)
                usou_cache_1 = True
                print("Cache Hit ativado: HP recuperado.")
            else:
                print("Cache Hit não pode ser usado agora.")
    else:
        print("Jogador 1 perdeu o turno por Loop Infinito.")
        loop_infinito_1 = False

    if vida_jogador_2 <= 0:
        break

    if not loop_infinito_2:
        if multiplayer:
            opcao = int(input("JOGADOR 2 - Sua vez (1-10): "))
        else:
            opcao = random.randint(1, 2)

        if opcao == 1:
            critico = random.randint(1, 10) == 10
            ataque = ataque_jogador_2 * (2 if critico or forca_turnos_2 > 0 else 1)
            if escudo_ativo_1:
                print("Ataque bloqueado pelo escudo do Jogador 1!")
                escudo_ativo_1 = False
            else:
                dano = max(ataque - defesa_jogador_1, 0)
                vida_jogador_1 -= dano
                print(f"Jogador 2 ataca! Jogador 1 perde {dano} HP.")
            if critico:
                print("Ataque Crítico!")
        elif opcao == 2:
            vida_jogador_2 = min(vida_jogador_2 + cura, vida)
            print("Jogador 2 se curou.")
        elif opcao == 3:
            forca_turnos_2 = 2
        elif opcao == 4:
            regeneracao_turnos_2 = 3
        elif opcao == 5:
            veneno_turnos_1 = 3
        elif opcao == 6:
            escudo_ativo_2 = True
        elif opcao == 7:
            buffer_overflow_1 = True
        elif opcao == 8:
            loop_infinito_1 = True
        elif opcao == 9:
            tela_azul_1 = 2
        elif opcao == 10:
            if not usou_cache_2 and vida_jogador_2 < vida * 0.25:
                vida_jogador_2 += int(vida * 0.3)
                usou_cache_2 = True
                print("Cache Hit ativado.")
    else:
        print("Jogador 2 perdeu o turno por Loop Infinito.")
        loop_infinito_2 = False

if vida_jogador_1 <= 0:
    print("Jogador 2 venceu!")
else:
    print("Jogador 1 venceu!")
