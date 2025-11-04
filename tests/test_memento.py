# tests/test_memento.py
from app.calculator_memento import Memento, Caretaker

def test_memento_get_state():
    state = ["a", "b", "c"]
    m = Memento(state)
    assert m.get_state() == state

def test_caretaker_save_and_undo_redo():
    caretaker = Caretaker()
    state1 = ["first"]
    state2 = ["second"]

    caretaker.save_state(state1)
    caretaker.save_state(state2)

    # Undo should return the last state saved
    undone = caretaker.undo()
    assert undone == state2

    # Redo should reapply the undone state
    redone = caretaker.redo()
    assert redone == state2
