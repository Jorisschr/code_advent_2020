import json
from datetime import datetime
from pprint import pprint

import pandas as pd


def parse_input() -> dict:
    """Parse the json containing the leaderboard data

    Returns
    -------
    dict
        dictionary containing the data
    """
    with open("./data/leaderboard.json", "r") as f:
        leaderboard = json.load(f)
    return leaderboard


def create_overview(lb: dict) -> pd.DataFrame:
    """Create an overview of the leaderboard

    Parameters
    ----------
    lb : dict
        dictionary containing the leaderboard information

    Returns
    -------
    pd.DataFrame
        dataframe containing the overview
    """
    rows = []
    for key in lb["members"]:
        d = lb["members"][key]["completion_day_level"]
        for k_1 in d:
            for k_2 in d[k_1]:
                rows.append(
                    [
                        lb["members"][key]["name"],
                        int(k_1),
                        int(k_2),
                        datetime.fromtimestamp(int(d[k_1][k_2]["get_star_ts"])),
                    ]
                )
    df = pd.DataFrame(data=rows, columns=["name", "problem", "part", "time"])
    return df.sort_values(by="time")


if __name__ == "__main__":
    lb = parse_input()
    df = create_overview(lb)

    df.to_csv("./data/leaderboard.csv", index=False)
