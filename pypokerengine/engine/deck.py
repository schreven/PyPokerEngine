from functools import reduce

from pypokerengine.engine.card import Card
import random

class Deck:

  def __init__(self, deck_ids=None, cheat=False, cheat_card_ids=[], cst_cheat_ids = []):
    self.cheat = cheat
    self.cheat_card_ids = cheat_card_ids
    self.cst_cheat_ids = cst_cheat_ids
    self.deck = [Card.from_id(cid) for cid in deck_ids] if deck_ids else self.__setup()
    #print(cst_cheat_ids)


  def draw_card(self):
    return self.deck.pop()

  def draw_cards(self, num):
    return reduce(lambda acc, _: acc + [self.draw_card()], range(num), [])

  def size(self):
    return len(self.deck)

  def restore(self):
    self.deck = self.__setup()

  def shuffle(self):
    if not self.cheat:
      random.shuffle(self.deck)

#  def distr_cheat_cards(self):
#    self.deck = [Card.from_id(cid) for cid in self.cst_cheat_ids[:20]]
#    del self.cst_cheat_ids[:20]
#    return
  # serialize format : [cheat_flg, chat_card_ids, deck_card_ids]
  def serialize(self):
    return [self.cheat, self.cheat_card_ids, self.cst_cheat_ids, [card.to_id() for card in self.deck]]

  @classmethod
  def deserialize(self, serial):
    cheat, cheat_card_ids, cst_cheat_ids, deck_ids = serial
    return self(deck_ids=deck_ids, cheat=cheat, cheat_card_ids=cheat_card_ids, cst_cheat_ids = cst_cheat_ids)

  def __setup(self):
    return self.__setup_cheat_deck() if self.cheat else self.__setup_52_cards()

  def __setup_52_cards(self, nb_cards = 52):
    return [Card.from_id(cid) for cid in range(1,nb_cards+1)]

  def __setup_cheat_deck(self, nb_cards = 52):
    cards = [Card.from_id(cid) for cid in self.cst_cheat_ids[:52]]
    del self.cst_cheat_ids[:20]
    return cards[::-1]


