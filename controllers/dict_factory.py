import sys


class DictFactory:
    @staticmethod
    def create_dict(type,element):
        if type == "member":
            return {
                "id": element.id,
                "name": element.name,
                "email": element.email,
                "age": element.age,
                "phone": element.phone,
                "category": element.category,
                "address": element.address,
                "join_date": element.join_date,
                "positions": element.positions,
                "skills": element.skills,
                "subscription_status": element.subscription_status
            }
        elif type == "event":
            return {
                "id": element.id,
                "name": element.name,
                "date": element.date,
                "e_type": element.e_type,
                "organizer": element.organizer,
                "oponent": element.opponent,
                "result": element.result,
                "players": element.players,
                "duration": element.duration
            }
        elif type == "subscription":
            return {
                "id": element.id,
                "player_id": element.player_id,
                "date": element.date,
                "status": element.status,
                "amount": element.amount,
                "duration": element.duration,
                "player": DictFactory.create_dict("member",element.player) if element.player else None
            }
        else :
            print("Bad element : " + type)
            sys.exit()