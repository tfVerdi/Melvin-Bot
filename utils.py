from random import randint

def getRandomInt(upper_limit: int) -> int:
    return randint(1, upper_limit)

class Assortment:
    def __init__(self, items):
        self.HISTORY_LIMIT = 10
        self.ITEMS = items
        self.history = []
    
    def _add_to_history(self, item = tuple | str):
        self.history.append(item)
        if len(self.history) > self.HISTORY_LIMIT:
            self.history = self.history[1:]
    
    def recently_used(self, item = tuple | str) -> bool:
        return item in self.history
    
    def get_random(self) -> tuple | str:
        random_index = randint(0, len(self.ITEMS)-1)
        while self.recently_used(self.ITEMS[random_index]):
            random_index = randint(0, len(self.ITEMS)-1)
        self._add_to_history(self.ITEMS[random_index])
        return self.ITEMS[random_index]