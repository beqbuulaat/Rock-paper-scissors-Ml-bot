
import random

def player(prev_play, opponent_history=[]):
    if prev_play:
        opponent_history.append(prev_play)

    if not hasattr(player, "histories"):
        player.histories = {}
        player.last_sequence = ""

    # Добавим последние 3 хода оппонента как ключ
    if len(opponent_history) >= 3:
        player.last_sequence = "".join(opponent_history[-3:])
        if player.last_sequence not in player.histories:
            player.histories[player.last_sequence] = {"R": 0, "P": 0, "S": 0}
        if len(opponent_history) >= 4:
            next_move = opponent_history[-1]
            seq = "".join(opponent_history[-4:-1])
            if seq in player.histories:
                player.histories[seq][next_move] += 1

        # Предсказать следующий ход соперника
        guess = max(player.histories[player.last_sequence], key=player.histories[player.last_sequence].get)
    elif len(opponent_history) > 0:
        guess = opponent_history[-1]
    else:
        guess = random.choice(["R", "P", "S"])

    # Победить предсказанный ход
    beats = {"R": "P", "P": "S", "S": "R"}
    return beats[guess]
