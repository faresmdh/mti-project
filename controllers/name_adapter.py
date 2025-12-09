class NameAdapter:
    def __init__(self,firstname,lastname):
        self.name = firstname + " " + lastname

    def get_name(self):
        return self.name