def list_index(score, rets):
    if score <= 0:
        return rets
    index = 0
    while 2 ** (index + 1) <= score:
        index += 1
    rets.append(index)
    score -= 2 ** index
    return list_index(score, rets)

class Allergies(object):

    def __init__(self, score):
        self.score = score
        self.items = ["eggs", "peanuts", "shellfish",
                      "strawberries", "tomatoes", "chocolate", "pollen", "cats"]

    def is_allergic_to(self, item):
        return item in self.lst

    @property
    def lst(self):
        results = []
        rets = list_index(self.score,[])
        for index in rets:
            if index < len(self.items):
                results.append(self.items[index])
        return results

