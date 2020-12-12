import json
import pprint

with open("./data/leaderboard.json", "r") as f:
    leaderboard = json.load(f)
pprint.pprint(leaderboard)
