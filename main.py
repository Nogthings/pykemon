from constants *
from models *

#Firs, define pokemons with stats

pokemon1 = Pokemon("Bulbasaur", 100, "grass", "poison")
pokemon2 = Pokemon("Charmander", 100, "fire", none)
pokemon1.current_hp = 45
pokemon2.current_hp = 39

#stats
pokemon1.stats = {
    HP: 45,
    ATTACK: 49,
    DEFFENSE: 49,
    SPATTACK: 65,
    SPDEFENSE: 65,
    SPEED: 45
}

pokemon2.stats = {
    HP: 39,
    ATTACK: 52,
    DEFFENSE: 43,
    SPATTACK: 80,
    SPDEFENSE: 65,
    SPEED: 65
}

#attacks
pokemon1.attacks [Attack("scratch", "normal", PHYSICAL, 10, 10, 100)]
pokemon2.attacks [Attack("scratch", "normal", PHYSICAL, 10, 10, 100)]

#start-Battle
battle = Battle (pokemon1)

    def ask_command(pokemon1):
        command = None
        while not command:
            #DO ATTACK -> attack 0
            tmp_command = input ("What should"+ pokemon.name + "do?").split(" ")
            if len(tmp_command) == 2:
                try:
                    if tmp_command[0] == DO_ATTACK and 0 <= int(tmp_command[1]) < 4
                        command = Command ({DO_ATTACK: (int(tmp_command[1]) })
                except Exception:
                    pass
        return command

    while not battle.is_finished():
        #first ask for command
        command1 = ask_command(pokemon1)
        command2 = ask_command(pokemon2)

        turn = Turn()
        turn.command1 = command1
        turn.command2 = command2

        if turn.can_start():
            #execute turn
            battle.execute_turn(turn)
            Battle.print_current_status()
