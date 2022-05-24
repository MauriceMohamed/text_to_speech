class Answer:
    def __init__(self, answer):
        self.answer = answer

    def __str__(self):
        return self.answer

    def __repr__(self):
        return self.answer

    def __eq__(self, other):
        return self.answer == other.answer

    def __hash__(self):
        return hash(self.answer)