class Allergies(object):

    def __init__(self, score):
        self.score = score
        self.items = ["eggs", "peanuts", "shellfish",
                      "strawberries", "tomatoes", "chocolate", "pollen", "cats"]
        self.allergies = self._match_allergies()

    def is_allergic_to(self, item):
        return item in self.allergies

    def _match_allergies(self):
        return [item for index,item in enumerate(self.items) if (1 << index) & self.score != 0]
        
    @property
    def lst(self):
        return self.allergies
