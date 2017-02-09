'''
    This code sorts list of Players
    in decreasing order of scores.
    We are implementing new cmp
    function passed as a parameter
    to built-in sorted function
'''
class Player:
    def __init__(self, name, score):
        self.name = name
        self.score = score

    def __repr__(self):
        return "<name: %s : score: %s>%(self.name, self.score)"

    def comparator(a, b):
        to_be_sorted = []
        to_be_sorted.append(a)
        to_be_sorted.append(b)

        if a.score > b.score:
            return -1
        elif a.score < b.score:
            return 1
        else:
            if a.name < b.name:
                return -1
            else:
                return 1

n = int(raw_input())
data = []
for i in range(n):
    name, score = raw_input().split()
    score = int(score)
    player = Player(name, score)
    data.append(player)

data = sorted(data, cmp=Player.comparator)
for i in data:
    print i.name, i.score