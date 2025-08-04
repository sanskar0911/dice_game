import random

def play_game(players, rounds=10):
    scores = {player: 0 for player in players}
    streak = {player: 0 for player in players}  

    for r in range(1, rounds + 1):
        print(f"\n--- Round {r} ---")
        for player in players:
            roll = random.randint(1, 6)
            print(f"{player} rolls: {roll}")
            if roll == 6:
                scores[player] += 10
                streak[player] += 1
                if streak[player] == 2:
                    scores[player] += 5  
                    print(f"{player} gets a 5-point bonus for double 6s!")
                    streak[player] = 0
            elif roll == 1:
                scores[player] += 5
                streak[player] = 0
            else:
                scores[player] += roll
                streak[player] = 0

            if scores[player] < 0:
                scores[player] = 0

    return scores

def find_highest_scorer(scores):
    return max(scores.items(), key=lambda x: x[1])


players = input("Enter player names (comma-separated): ").split(",")
players = [p.strip().capitalize() for p in players]
num_rounds = int(input("Enter number of rounds (min 10): "))
if num_rounds < 10:
    num_rounds = 10


final_scores = play_game(players, num_rounds)

print("\n--- Final Scores ---")
for p, s in final_scores.items():
    print(f"{p}: {s}")

winner, high_score = find_highest_scorer(final_scores)
print(f"\n🏆 Winner: {winner} with {high_score} points!")
