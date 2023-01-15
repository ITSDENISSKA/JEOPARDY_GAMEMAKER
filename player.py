class Player:
    def __init__(self, name):
        self.name = name
        self.score = 0

    def get_score(self):
        return self.score

    def plus_score(self, n):
        self.score += n

    def minus_score(self, n):
        self.score -= n
