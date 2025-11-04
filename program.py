import csv
from random import randint

from models.club import Club
from managers.club_manager import ClubRepository


def csv_to_nested_dict(csv_file):
    # nested dictionary format
    data = {"Cadets":[],"Juniors":[],"Senior":[]}

    with open(csv_file, encoding='utf-8') as f:
        reader = csv.DictReader(f, delimiter="\t")
        for row in reader:
            category = row['category']

            player = {
                "player_id": row['player_id'],
                "player_name": row['player_name'],
                "email": row['email'],
                "phone": row['phone'],
                "position": row['position'],
                "age": int(row['age']),
            }

            if category in data:
                data[category].append(player)
            else:
                data[category] = [player]

        return data


def players_to_html(data):
    html = ['<html><head><meta charset="utf-8"></head><body>']

    for category, players in data.items():
        html.append(f"<h3>Liste des {category}</h3>")
        html.append('<table border="3">')
        html.append("<thead><tr><th>ID</th><th>Name</th><th>Email</th><th>Phone</th><th>Position</th><th>Age</th></tr></thead><tbody>")

        for player in players:
            html.append("<tr>")
            html.append(f"<td>{player['player_id']}</td>")
            html.append(f"<td>{player['player_name']}</td>")
            html.append(f"<td>{player['email']}</td>")
            html.append(f"<td>{player['phone']}</td>")
            html.append(f"<td>{player['position']}</td>")
            html.append(f"<td>{player['age']} ans</td>")
            html.append("</tr>")

        html.append("</tbody></table>")

    html.append("</body></html>")
    return "\n".join(html)

if __name__ == "__main__":

    clubRepo = ClubRepository()

    # Creating a club
    club = Club("ABR Djebahia","ABRD",clubRepo)

    # Showing dashboard
    club.show_dashboard()

    # Register random players to events
    for e in club.events:
        for i in range(0,11):
            e.register_player(club.players[randint(0, 14)])
        e.display_event()

    # showing subscriptions
    for s in club.subscriptions:
        s.display_subscription()

    # filename = "players.csv"  # change to your file name
    # players = csv_to_nested_dict(filename)
    # print(players)
    # html_txt = players_to_html(players)
    # with open("players.html", "w", encoding="utf-8") as f:
    #     f.write(html_txt)
    #
    # print("HTML file generated: players.html")


