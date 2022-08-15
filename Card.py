import random
import copy

class card:
    
    def __init__(self, index, suit):
        """
        Each card gets an ID and a suit so that we can build a deck of all the possible cards.
        We'll also store a name and an id-to-name converter so that we can always get the name
        really easily. 
        """
        self.id = index
        self.suit = suit
        self.id_to_name = {2: 'two', 3: 'three', 4:'four', 5:'five', 6:'six', 7:'seven',
                      8: 'eight', 9: 'nine', 10: 'ten', 11: 'jack', 12: 'queen',
                      13: 'king', 14: 'ace'}
        self.suit_to_name = {'H': 'hearts', 'D': 'diamonds', 'C': 'clubs', 'S': 'spades'}
        self.name = str(self.id_to_name[index])+' '+str(self.suit_to_name[suit])  

class deck:
    
    def __init__(self):
        """
        Creates the deck and stores it in an attribute for later use.
        Also makes it so we can store the "current hand" of the player
        """
        self.deck = self.build_deck()
        self.final_hand = None
        
    def build_deck(self):
        """
        Loops through all suits and card values (by id) to create all 52 cards.
        """
        deck = []
        suits = ['H','D','C','S']
        for suit in suits:
            for idx in range(2,15):
                deck.append(card(idx, suit))
        return deck
    
    def shuffle(self):
        """
        Shuffles the cards so they are in a random order
        """
        random.shuffle(self.deck)
        
    def deal_five(self):
        """
        Puts the first five cards into the players hand
        and sets the rest of the cards into a new attribute called
        "remaining_cards"
        """
        self.hand = self.deck[:5]
        self.remaining_cards = self.deck[5:]
    
    def draw_cards(self, ids_to_hold=[], shuffle_remaining=False):
        """
        This is to be run after we deal 5. This will figure out how many
        cards the player wants to hold from their hand (based on the input)
        and then replace the rest of the cards from the "remaining_cards."
        Since we're going to want to test this over and over, we'll
        also add a "shuffle_remaining" option so that we can shuffle
        the cards not in the players hand over and over if we want.
        The "IDS to hold" tell which card locations we want to hold - 
        not the card id, but the card location in the hand. So if we want
        to hold the first element in the hand list (in the 0th array spot) and 
        the 3rd card (2nd array spot), ids_to_hold = [0,2].
        """
        new_hand = copy.copy(self.hand)            
        remaining_cards = copy.copy(self.remaining_cards)
        
        if shuffle_remaining:
            random.shuffle(remaining_cards)
            
        for i, card in enumerate(new_hand):
            if i not in ids_to_hold:
                new_hand[i] = remaining_cards.pop(0)
        
        self.final_hand = new_hand
    
    def show_hand(self):
        """
        This is just a pretty printing option so we can
        see what's in the hand of the player.
        """
        for c in self.hand:
            print(c.name)

    def show_final_hand(self):
        for c in self.final_hand:
            print(c.name)
