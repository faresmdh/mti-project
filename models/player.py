class Player:
    def __init__(
            self,
            id: int = 0,
            name: str = "",
            email: str = "",
            age: int = 0,
            phone: str = "",
            category: str = "Cadets",
            address: str = "",
            join_date: str = "",
            positions: list = None,
            skills: list = None,
            subscription_status: str = "Unpaid"
    ):
        self.id = id
        self.name = name
        self.email = email
        self.age = age
        self.phone = phone
        self.category = category
        self.address = address
        self.join_date = join_date
        self.positions = positions if positions is not None else []
        self.skills = skills if skills is not None else []
        self.subscription_status = subscription_status

    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "email": self.email,
            "age": self.age,
            "phone": self.phone,
            "category": self.category,
            "address": self.address,
            "join_date": self.join_date,
            "positions": self.positions,
            "skills": self.skills,
            "subscription_status": self.subscription_status
        }

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