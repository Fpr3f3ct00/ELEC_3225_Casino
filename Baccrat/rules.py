from Card import Card, Shoe
from hands import Player, Banker
from persons import Person

class Game:
    """Application of the rules of baccarat - player banker variation. This class
    manages only the card handling and its results.

    Args:
        num_decks: int, number of decks of the initial shoe. Optional, default
            value 8.

    Attributes:
        player_value: int, value of player hand.
        player_cards: str, cards of player hand.
        banker_value: int, value of banker hand.
        banker_cards: str, cards of banker hand.
        num_decks: int, current number of decks in the shoe.
    """
    def __init__(self, num_decks=8):
        self._game_running = False
        self._persons = []
        self._player = None
        self._banker = None
        self.create_shoe(num_decks)

    @property
    def player_value(self):
        """Returns value of player hand.

        Raises:
            ValueError: If _player is None.
        """
        if not self._player:
            raise ValueError('No hands were dealt.')
        return self._player.value

    @property
    def player_values(self):
        """Returns the individual card values of player hand.
        """
        if not self._player:
            raise ValueError('No hands were dealt.')
        values = []
        for card in self._player.cards:
            values.append(card.value)
        return values

    @property
    def player_cards(self):
        """Returns cards of player hand.
        """
        if not self._player:
            raise ValueError('No hands were dealt.')
        return ', '.join([card.__str__() for card in self._player.cards])

    @property
    def banker_value(self):
        """Returns value of banker hand.
        """
        if not self._banker:
            raise ValueError('No hands were dealt.')
        return self._banker.value

    @property
    def banker_values(self):
        """Returns the individual card values of banker hand.
        """
        if not self._banker:
            raise ValueError('No hands were dealt.')
        values = []
        for card in self._banker.cards:
            values.append(card.value)
        return values

    @property
    def banker_cards(self):
        """Returns cards of banker hand.
        """
        if not self._banker:
            raise ValueError('No hands were dealt.')
        return ', '.join([card.__str__() for card in self._banker.cards])

    @property
    def num_decks(self):
        """Returns initial number of decks of _shoe."""
        return self._shoe.num_decks

    @property
    def num_cards(self):
        """Returns current number of cards in shoe."""
        return self._shoe.num_cards

    def create_shoe(self, num_decks):
        """Creates an instance of Shoe with num_decks."""
        self._shoe = Shoe(num_decks)
        self._num_decks = num_decks

    def deal_hands(self):
        """Deals both hands. Creates a player and banker instance and pops two
        cards from the Shoe instance. Sets the game as open.
        """
        if self._game_running:
            raise GameError('Game is running')
        self._player = Player(self._shoe.draw_cards(2))
        self._banker = Banker(self._shoe.draw_cards(2))
        self._game_running = True

    def is_natural(self):
        """Checks if there is an hand with a natural. If there is closes the
        game.

        Returns:
            bol, True if there is a natural, False otherwise.
        """
        if not self._game_running:
            raise GameError('Game is not running.')
        natural = self._player.is_natural() or self._banker.is_natural()
        if natural:
            self._game_running = False
        return natural

    def draw_thirds(self):
        """Applies the third card drawing rules to draw a possible third card
        for both hands. Closes the game.

        Returns: list with tuples, each tuple contains the hand and card that
            was drawn to which the third card rules were applied.
        """
        if not self._game_running:
            raise GameError('Game is not running.')
        if self.is_natural():
            raise GameError('Can\'t draw third cards when there is a natural.')
        third_draws = []
        if self._player.draw_third():
            self._player.add_cards(self._shoe.draw_cards(1))
            third_draws.append(['player', self._player.cards[2].__str__()])
            if self._banker.draw_third(self._player.cards[2]):
                self._banker.add_cards(self._shoe.draw_cards(1))
                third_draws.append(['banker', self._banker.cards[2].__str__()])
        elif self._banker.draw_third():
            self._banker.add_cards(self._shoe.draw_cards(1))
            third_draws.append(['banker', self._banker.cards[2].__str__()])
        self._game_running = False
        return third_draws

    def game_result(self):
        """Checks was is the result of the game.

        Returns:
            str, with the winning hand or 'tie' in case is a tie.
        """
        if self._game_running:
            raise GameError('Game is running.')
        if self._player.value > self._banker.value:
            return 'player'
        elif self._player.value < self._banker.value:
            return 'banker'
        else:
            return 'tie'

    def __repr__(self):
        """Return the representation string as if the object was
        called when creating a new instance with the current number of decks.
        """
        return f'Game({self._shoe.num_decks})'

class Table(Game):
    """Table of a game of baccarat. Introduces the persons and betting system.
    Sets the bets as open. Subclass of Game.

    Attributes:
        num_persons: int, total number of persons.
        available_persons: list, with the indexes of the persons that are still
            in game with a positive balance.
        valid_bets: list, with the indexes of the persons that currently have a
            valid bet on the table.
    """
    def __init__(self, num_decks=8):
        self._bets_open = True
        Game.__init__(self, num_decks)

    @property
    def num_persons(self):
        """Retuns the total number of persons."""
        return len(self._persons)

    @property
    def available_persons(self):
        """Returns the list of indexes of the persons with positive balance."""
        persons = []
        for person in self._persons:
            if person.balance > 0:
                persons.append(self._persons.index(person))
        return persons

    @property
    def valid_bets(self):
        """Returns the list of persons with valid bets on table."""
        persons = []
        for person_i in self.available_persons:
            if self._persons[person_i].is_valid_bet():
                persons.append(person_i)
        return persons

    def deal_hands(self):
        """Deals both hands. Calls deal_hands from the superclass Game. Sets the
        bets as closed.
        """
        if not self._bets_open:
            raise GameError('There are some bets on table.')
        self._bets_open = False
        Game.deal_hands(self)

    def add_person(self, balance):
        """Add a new person to the table.

        Args:
            balance: int, the initial balance of the person.
        """
        self._persons.append(Person(balance))

    def bet(self, person_i, hand_bet, amount_bet):
        """Place a bet.

        Args:
            person_i: int, index of the person that will make the bet.
            hand_bet: str, the hand to be bet. Can also be a tie.
            amount_bet: int, the amount to bet.
        """
        if not self._bets_open:
            raise GameError('A person cannot make a bet after the hands are dealt.')
        #print(str(hand_bet)+"  "+str(amount_bet))
        self._persons[person_i].hand_bet = hand_bet
        self._persons[person_i].amount_bet = amount_bet

    def bet_result(self, person_i):
        """Apply the result, win or loss, of a bet according to the result of a game.

        Args:
            person_i: int, the index of the person to apply the bet result.
        """
        if self._persons[person_i].hand_bet == self.game_result():
            self._persons[person_i].win()
            result = ('win', self._persons[person_i].balance)
        else:
            self._persons[person_i].lose()
            result = ('lose', self._persons[person_i].balance)
        return result

    def open_bets(self):
        if not self.valid_bets:
            self._bets_open = True
        return self._bets_open

    def __getitem__(self, person_i):
        """Get the status of a person.

        Args:
            person_i: int, the index of the person to get the status.

        Returns:
            str, the status of the person.
        """
        return self._persons[person_i].__str__()

class GameError(Exception):
    pass
