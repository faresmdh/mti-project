import csv
import html
from collections import defaultdict

from club import Club


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

    players_csv_file = "players.csv"
    club = Club("ABR Djebahia","ABRD",[])
    club.add_players_from_csv(players_csv_file)
    club.show_dashboard()

    # filename = "players.csv"  # change to your file name
    # players = csv_to_nested_dict(filename)
    # print(players)
    # html_txt = players_to_html(players)
    # with open("players.html", "w", encoding="utf-8") as f:
    #     f.write(html_txt)
    #
    # print("HTML file generated: players.html")


