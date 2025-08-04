
import random

def random_player(prev_play):
    return random.choice(["R", "P", "S"])

def quincy(prev_play):
    if not hasattr(quincy, "plays"):
        quincy.plays = 0
    result = ["R", "P", "S"][quincy.plays % 3]
    quincy.plays += 1
    return result

def abbey(prev_play):
    if not hasattr(abbey, "last_opponent_play"):
        abbey.last_opponent_play = ""
    if abbey.last_opponent_play == "":
        result = "R"
    else:
        result = abbey.last_opponent_play
    abbey.last_opponent_play = prev_play
    return result

def kris(prev_play):
    return random.choice(["R", "P", "S"])

def mrugesh(prev_play):
    if not hasattr(mrugesh, "opponent_history"):
        mrugesh.opponent_history = []
    if prev_play:
        mrugesh.opponent_history.append(prev_play)
    guess = "R"
    if len(mrugesh.opponent_history) > 0:
        last_ten = mrugesh.opponent_history[-10:]
        most_common = max(set(last_ten), key=last_ten.count)
        guess = most_common
    return beat(guess)

def beat(move):
    if move == "R":
        return "P"
    elif move == "P":
        return "S"
    else:
        return "R"

def play(player1, player2, num_games=1000, verbose=False):
    p1_prev = ""
    p2_prev = ""
    p1_score = 0
    p2_score = 0
    ties = 0
    for _ in range(num_games):
        p1 = player1(p2_prev)
        p2 = player2(p1_prev)

        if p1 == p2:
            ties += 1
        elif (
            (p1 == "R" and p2 == "S") or
            (p1 == "P" and p2 == "R") or
            (p1 == "S" and p2 == "P")
        ):
            p1_score += 1
        else:
            p2_score += 1

        p1_prev = p1
        p2_prev = p2

        if verbose:
            print(f"You played: {p1} | Opponent played: {p2}")
    return {
        "Player 1": p1_score,
        "Player 2": p2_score,
        "Ties": ties
    }
