class Player:
    def __init__(
            self,
            id: int,
            name: str = "",
            email: str = "",
            age: int = "",
            phone: str = "",
            category: str = "Cadets",
            address: str = "",
            join_date: str = "",
            positions: list = [],
            skills: list = [],
            subscription_status: str = "Unpaid"
    ):
        self.id = id
        self.name = name
        self.age = age
        self.email = email
        self.phone = phone
        self.category = category
        self.address = address
        self.join_date = join_date
        self.positions = positions
        self.skills = skills
        self.subscription_status = subscription_status

    def add_position(self, position: str):
        if position is not None:
            self.positions.append(position)

    def remove_position(self, position: str):
        if self.positions.__contains__(position):
            self.positions.remove(position)

    def add_skill(self, skill: str):
        if skill is not None:
            self.skills.append(skill)

    def remove_skill(self, skill: str):
        if self.skills.__contains__(skill):
            self.skills.remove(skill)

    def update_player(
            self,
            name: str=None,
            email: str=None,
            age: int=None,
            phone: str=None,
            category: str=None,
            address: str=None,
            join_date: str=None,
            positions: list=None,
            skills: list=None,
            subscription_status:str=None
    ):
        if name is not None : self.name = name
        if email is not None : self.email = email
        if age is not None : self.age = age
        if phone is not None : self.phone = phone
        if category is not None : self.category = category
        if address is not None : self.address = address
        if join_date is not None : self.join_date = join_date
        if positions is not None : self.positions = positions
        if skills is not None : self.skills = skills
        if subscription_status is not None : self.subscription_status = subscription_status

    def generate_player_card(self):
        print("Player card -> ")
        print(
            f"• ID : {self.id} \n• Full name : {self.name}\n• Age : {self.age} years old \n• Email address : {self.email}\n• Phone number : {self.phone}\n• Category : {self.category}\n• Joined : {self.join_date}\n• Address : {self.address}\n• Subscription status: {self.subscription_status}")
        print("• Positions :")
        for p in self.positions:
            print(f"    - {p}")
        print("• Skills :")
        for s in self.skills:
            print(f"    - {s}")

if __name__ == "__main__":
    # creating new player
    p = Player(1,"Meddahi Fares", "fares.mdh1@gmail.com", 25, "0558015936", "Senior", "Djebahia", "13/12/2024",
               ["Middle", "Attack"], ["Left leg", "Shooter"])

    # adding new position
    p.add_position("Goal keeper")

    # removing existing position
    p.remove_position("Attack")

    # adding new skill
    p.add_skill("Left corners")

    # removing existing skill
    p.remove_skill("Shooter")

    # update phone and email
    p.update_player(email="fares.meddahi@univ-bouira.dz",phone="067344652")

    # display player card
    p.generate_player_card()
