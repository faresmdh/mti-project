from models.player import Player
from models.subscription import Subscription


class MemberBuilder:
    def __init__(self):
        self.name = None,
        self.email = None,
        self.age = None,
        self.phone = None,
        self.address = None,
        self.join_date = None,
        self.positions = [],
        self.skills = [],
        self.category = "Cadets",
        self.subscription_status = 'Unpaid'

    def set_name(self, name):
        self.name = name
        return self

    def set_email(self, email):
        self.email = email
        return self

    def set_age(self, age):
        self.age = age
        return self

    def set_phone(self, phone):
        self.phone = phone
        return self

    def set_address(self, address):
        self.address = address
        return self

    def set_join_date(self, join_date):
        self.join_date = join_date
        return self

    def set_positions(self, positions):
        self.positions = positions
        return self

    def set_skills(self, skills):
        self.skills = skills
        return self

    def set_subscription_status(self, subscription_status):
        self.subscription_status = subscription_status
        return self

    def set_category(self, category):
        self.category = category
        return self



    def build(self):
        # Validate required fields
        if self.name is None:
            raise ValueError("name is required")
        if self.email is None:
            raise ValueError("email is required")
        if self.age is None:
            raise ValueError("age is required")
        if self.phone is None:
            raise ValueError("phone is required")
        if self.address is None:
            raise ValueError("address is required")
        if self.join_date is None:
            raise ValueError("join_date is required")

        return Player(
            id = 0,
            name=self.name,
            email=self.email,
            age=self.age,
            phone=self.phone,
            address=self.address,
            join_date=self.join_date,
            skills=self.skills,
            positions=self.positions,
            subscription_status=self.subscription_status
        )