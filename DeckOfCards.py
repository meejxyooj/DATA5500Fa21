import random

suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')
faces = ('2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King', 'Ace')
values = {'2':2, '3':3, '4':4, '5':5, '6':6, '7':7, '8':8, '9':9, '10':10, 'Jack':10, 'Queen':10, 'King':10, 'Ace':11}

class Card:
    
    def __init__(self, suit, face):
        self.suit = suit
        self.face = face
        
    def __str__(self):
        return self.face + " of " + self.suit
        
class DeckOfCards: 
    
    def __init__(self, deck = []):
        self.deck = deck
        for suit in suits: 
            for face in faces: 
                self.deck.append(Card(suit,face))
                
    def __str__(self):
        deck_comp = ''
        for card in self.deck:
            deck_comp += card.__str__() + ', '
        return deck_comp
        
    def shuffleDeck(self):
        random.shuffle(self.deck)
        
    def deal(self):
        return self.deck.pop(0)
        
# test_deck = Deck()
# print(test_deck)

class Hand:
    def __init__(self):
        self.cards = []
        self.value = 0
        
    def add_card(self, card):
        self.cards.append(card)
        self.value += values[card.face]
        
# while True:
#print Welcome to Blackjack
print("Welcome to Black Jack!")

#print the unshuffled deck
deck = DeckOfCards()
print("Deck before shuffling")
print(deck)

#Shuffle deck
deck.shuffleDeck()
print("\nDeck after shuffling")
print(deck)

#draw cards into hand
print("This is your hand")
playerHand = Hand()
playerHand.add_card(deck.deal())
playerHand.add_card(deck.deal())



    
    

        
# test_deck = Deck()
# print(test_deck)
# test_deck.shuffleDeck()
# print(test_deck)

# test_player = Hand()
# test_player.add_card(test_deck.deal())
# test_player.add_card(test_deck.deal())
# test_player.add_card(test_deck.deal())
# test_player.add_card(test_deck.deal())

# for card in test_player.cards:
#     print (card)
# print(test_player.value)

# test_dealer = random.randint(17,23)
# print(test_dealer)
