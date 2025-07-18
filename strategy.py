class Strategy:
    def __init__(self, dice_values):
        self.dice = dice_values
        self.counter = {i: self.dice.count(i) for i in range(1, 7)}
        self.unique = sorted(set(self.dice))

    def calculate_all(self):
        scores = {}
        for i in range(1, 7):
            scores[f"{i}s"] = self.counter.get(i, 0) * i

        scores["Choice"] = sum(self.dice)
        scores["3 of a kind"] = self.of_a_kind(3)
        scores["4 of a kind"] = self.of_a_kind(4)
        scores["Full House"] = self.full_house()
        scores["S. Straight"] = self.small_straight()
        scores["L. Straight"] = self.large_straight()
        scores["Yacht"] = 50 if 5 in self.counter.values() else 0
        return scores

    def of_a_kind(self, n):
        for count in self.counter.values():
            if count >= n:
                return sum(self.dice)
        return 0

    def full_house(self):
        vals = list(self.counter.values())
        return 25 if (3 in vals and 2 in vals) else 0

    def small_straight(self):
        straights = [{1,2,3,4}, {2,3,4,5}, {3,4,5,6}]
        for s in straights:
            if s.issubset(set(self.dice)):
                return 30
        return 0

    def large_straight(self):
        return 40 if set(self.dice) in [{1,2,3,4,5}, {2,3,4,5,6}] else 0
