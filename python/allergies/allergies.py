class Allergies(object):

    def __init__(self, score):
        self.score = score
        self.items = ["eggs", "peanuts", "shellfish",
                      "strawberries", "tomatoes", "chocolate", "pollen", "cats"]
        self.allergies = self._match_allergies()

    def is_allergic_to(self, item):
        return item in self.allergies

    def _match_allergies(self):
        match_result = list(bin(self.score & 255)[2:])
        match_result.reverse()
        allergies = []
        for index, value in enumerate(match_result):
            if value == "1":
                allergies.append(self.items[index])
        return allergies

    @property
    def lst(self):
        return self.allergies
