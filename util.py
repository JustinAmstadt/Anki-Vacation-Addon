# import the main window object (mw) from aqt
from aqt import mw
# import the "show info" tool from utils.py
from aqt.utils import showInfo, qconnect
# import all of the Qt GUI library
from aqt.qt import *
from .util import select_deck_id

# For development purposes only
# Will reset all the cards in a deck to the range set. 0-0 range makes all cards immediately available. 1 is the next day
def resetDeck() -> None:
    test_deck_id = 1706090935037
    deck_card_ids = mw.col.decks.cids(test_deck_id)

    mw.col.sched.reschedCards(deck_card_ids, 0, 3)

def reschedule() -> None:
    
    """ Adds new cards to a deck
    for i in range(0,200):
        note = mw.col.newNote()
        note["Front"] = str(i)
        note.note_type()["did"] = test_deck_id
        mw.col.addNote(note)

    print("Before Sort")
    """

    deck_id = select_deck_id("Which deck would you like to reschedule?")
    if deck_id is None:
        return

    deck_card_ids = mw.col.decks.cids(deck_id)

    start_range = 1
    end_range = 6
    counter = start_range

    day_buckets = {
        1: [],
        2: [],
        3: [],
        4: [],
        5: [],
        6: [],
    }

    for cid in deck_card_ids:
        c = mw.col.get_card(cid)
        print(c.due)

        if c.due == 1:
            day_buckets[counter].append(cid)
            counter = counter + 1

            if counter > end_range:
                counter = start_range

    total_sorted = 0

    for key, value in day_buckets.items():
        mw.col.sched.reschedCards(value, key, key)
        total_sorted = total_sorted + len(value)

    """
    print("After Sort")
    for cid in deck_card_ids:
        c = mw.col.get_card(cid)
        print(c.due)
    """

    showInfo(str(total_sorted) + " cards rescheduled")

action = QAction("Reschedule", mw)
qconnect(action.triggered, reschedule)
mw.form.menuTools.addAction(action)

"""
action = QAction("Reset Deck", mw)
qconnect(action.triggered, resetDeck)
mw.form.menuTools.addAction(action)
"""