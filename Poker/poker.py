
from collections import Counter
from itertools import combinations
from Card import *


class jacks_or_better_scorer:
    
    def __init__(self, hand):
        """
        Take a hand and do some checking on it. Make sure it's 5 cards.
        Now get a list of suits and ids. We'll use the ids to check for
        straights and pairs, and the suits to check for flushes. Then we'll
        check if those exist simultaneously.
        
        Then we'll take the maximum possible payout.
        """
        assert len(hand)==5
        self.ids = [x.id for x in hand]
        self.suits = [x.suit for x in hand]
        prs = self.check_for_pairs()
        flsh = self.check_for_flush()
        strt = self.check_for_straight()
        strt_flsh = self.check_straight_flush(strt, flsh)
        self.score = max([prs, flsh, strt, strt_flsh])
        
    def check_for_pairs(self):
        """
        The counter object returns a list of tuples, where the 
        tuple is (id, number of appearances). We'll check for
        4 of a kind, then full house, then three of a kind, then
        two pairs, then finally one pair (but the id has to be bigger
        than 10, which means jack or higher). Whatever we find,
        we return the correct payout.
        """
        c = Counter(self.ids)
        m = c.most_common()[:2]
        if m[0][1] == 4:
            return 25
        elif m[0][1] == 3 and m[1][1] == 2:
            return 9  
        elif m[0][1] == 3:
            return 3
        elif m[0][1] == 2 and m[1][1] == 2:
            return 2
        elif m[0][1] == 2 and m[0][0] >= 11:
            return 1
        else:
            return 0
        
    def check_for_flush(self): 
        """
        Using the counter object described in the pairs check, but now
        we're just checking if all the suits are the same.
        """
        c = Counter(self.suits)
        m = c.most_common()[0][1]
        if m == 5:
            return 6
        else:
            return 0
        
    def check_for_straight(self):
        """
        Checking if the cards are in order using the straight helper
        function. The confusing part here is to check it both if the
        aces are counted as high and if they are counted as low.
        """
        is_straight = 0
        
        # section to handle if the ace is 1 instead of 14
        if 14 in self.ids:
            new_ids = [i if i != 14 else 1 for i in self.ids]
            is_straight += self.straight_helper(new_ids)
        
        # Check if straight with aces as 14
        is_straight += self.straight_helper(self.ids)
        
        if is_straight:
            return 4
        else:
            return 0
        
    def straight_helper(self, hand_ids):
        """
        A helper function that sorts the card ids,
        then goes through and makes sure that each card is
        one higher than the previous. If it's not, 
        we mark it as a 0, not a straight.
        """
        li2 = sorted(hand_ids)
        it=iter(li2[1:])
        if all(int(next(it))-int(i)==1 for i in li2[:-1]):
            return 1
        else:
            return 0
        
    def check_straight_flush(self, strt, flsh):
        """
        Check if this is a straight flush. If it is
        and both the king and ace are in there, 
        mark that it's a Royal flush and return the
        biggest payout. 
        """
        if flsh and strt:
            if 13 in self.ids and 14 in self.ids:
                return 800
            else:
                return 50
        else:
            return 0

def combinations(lst, depth, start=0, prepend=[]):
    if depth <= 0:
        yield prepend
    else:
        for i in range(start, len(lst)):
            for c in combinations(lst, depth - 1, i + 1, prepend + [lst[i]]):
                yield c
                
possible_hold_combos = [[]]
for i in range(1,6):
    for c in combinations([0,1,2,3,4], i):
        possible_hold_combos.append(c)

def play_poker(money, sim_strength=1000, max_count=10000, return_count=False, return_both=False, verbose=False):
    money_tally = [money]
    count = 0
    
    # Checks to see if we have enough money to play and that we haven't been playing too long
    while money > 0 and count < max_count:
        # bets 1 dollar and counts as playing
        count += 1
        money -= 1 
        
        # Get the cards setup
        cards = deck()
        cards.shuffle()
        cards.deal_five()
        

        # Set up our result checker
        d = {}
        for c in possible_hold_combos:
            d[str(c)] = []
                  
        # Now loop through all the hands and check what the expected score is. This is the Monte
        # Carlo part. We're using a bunch of random draws to see what the best move is statistically.
        for combo in possible_hold_combos:
            for i in range(sim_strength):
                cards.draw_cards(ids_to_hold=combo, shuffle_remaining=True)
                jb = jacks_or_better_scorer(cards.final_hand)
                d[str(combo)].append(jb.score)

        results = []
        for c, v in d.items():
            results.append((c,np.mean(v)))
        
        # Get the best possible move
        best_move = eval(sorted(results, key=lambda x: x[1], reverse=True)[0][0])
        
        # Now actually draw the cards based on that move (note we shuffle here so we aren't just using
        # whatever the last set of cards were. It would be cheating if we didn't shuffle.)
        cards.draw_cards(ids_to_hold=best_move, shuffle_remaining=True)
        winnings = jacks_or_better_scorer(cards.final_hand).score
        
        # Now keep track of our winnings and print if we ask it to. Then play again.
        money += winnings
        money_tally.append(money)
        if verbose:
            cards.show_hand()
            print(best_move)
            cards.show_final_hand()
            print("Hand %i, Money: %i"%(count,money))
    
    # Return things, whether it be money or lists of moneys, or how long we've been playing.
    if return_both:
        return count, money_tally
    elif return_count:
        return count
    else:
        return money_tally
    
credit= random.randrange(0, 50)
strength = random.randrange(0, 100)
num_plays = random.randrange(0, 50)
print(credit, strength, num_plays)

money_tally = play_poker(money=credit, sim_strength=strength, max_count=num_plays, verbose=True)
print(money_tally)


