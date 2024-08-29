import collections
from random import choice, choices

Card = collections.namedtuple("Card", ["rank", "suit"])


class FrenchDeck:
    ranks = [str(n) for n in range(2, 11)] + list("JQKA")
    suits = "spades diamonds clubs hearts".split()

    def __init__(self) -> None:
        self._cards = [Card(r, s) for s in self.suits for r in self.ranks]

    def __len__(self):
        return len(self._cards)

    def __getitem__(self, position):
        return self._cards[position]

fd = FrenchDeck()

print(choice(fd))
print(choices(fd, k=4))

for card in fd[:3]:
    print(card)

for card in reversed(fd[:3]):
    print(card)

print(Card("3", "spades") in fd)
print(Card("Q", "beasts") in fd)


suit_values = dict(spades=3, hearts=2, diamonds=1, clubs=0)
def spades_high(card: Card):
    rank_value = FrenchDeck.ranks.index(card.rank)
    return rank_value * len(suit_values) + suit_values[card.suit]

for card in sorted(fd, key=spades_high):
    print(card)
    
    
test = "a"

obj1 = hash(test)
obj2 = hash(test)
print(obj1, obj2)