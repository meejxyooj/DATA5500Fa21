import random
# Create Deck

class DeckOfCards():
    def __init__(self):
        self.deck = []
        suits = ["Hearts", "Diamonds", "Spades", "Clubs"]
        faces = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King", "Ace"]
        
        for suit in suits:
            for face in faces:
                self.deck.append(Card(suit, face))
                
    def shuffleDeck(self):
        random.shuffle(self.deck)
                
    def printDeck(self):
        for card in self.deck:
            print(card.face, " of ", card.suit, end=", ")
    
    def draw(self): #use to draw the first card from the list
        return self.deck.pop()


# Create Card
class Card():
    def __init__(self, suit, face):
        self.suit = suit
        self.face = face
# Create Hand
class Hand():
    def __inint__(self):
        self.hand = []
        
    def addCard(self, card):
        self.hand.append(card)
        return self.hand
        
    def cardValue():
        value = 0 
        if card.face == "A":
            value += 11
            return value
            
        
# Create Dealer

# Create Player