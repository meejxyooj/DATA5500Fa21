import random

suits = ["Hearts", "Diamonds", "Spades", "Clubs"]
faces = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King", "Ace"]

class Card:
    def __init__(self,face,suit):
        self.face = face
        self.suit = suit
    
    def value(self):
        if self.face in ["Jack", "Queen", "King"]:
            return 10
        elif self.face == "Ace":
            return 11
        else:
            return int(self.face)

    def __str__(self):
        return self.face + ' of ' + self.suit
        
class Deck:
    def __init__(self):
        self.cards = []
        for face in faces: 
            for suit in suits:
                c = Card(face, suit)
                self.cards.append(c)
                
    def shuffle(self):
        random.shuffle(self.cards)
    
    def drawCard(self):
        if not self.cards:
            raise Exception("No more cards: empty deck!")
        card = self.cards.pop()
        return card
        
    def __str__(self):
        cards = []
        for c in self.cards: 
            cards.append(str(c))
        return str(cards)
        
class Hand:
    def __init__(self, card):
        self.cards = []
        self.value = 0

    def add_card(self,card):
        self.cards.append(card)
        self.value += value(Card.value)
        
        
    
        
#test 1
def test1():
    card1 = Card('9', 'Spades')
    card2 = Card('Queen', 'Hearts')
    card3 = Card('King', 'Hearts')
    card4 = Card('9', 'Diamonds')
    print (card1, card2, card3, card4)
    
def test2():
    deck = Deck()
    print('----------- Before Shuffle -----------')
    print(deck)
    deck.shuffle()
    print('----------- After Shuffle -----------')
    print(deck)
    
test1()
test2()
