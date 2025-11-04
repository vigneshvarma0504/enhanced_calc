# app/calculator_memento.py

class Memento:
    """Stores a snapshot of calculator history."""
    def __init__(self, state):
        self._state = list(state)

    def get_state(self):
        return self._state


class Caretaker:
    """Manages undo/redo using Memento pattern."""
    def __init__(self):
        self._undo_stack = []
        self._redo_stack = []

    def save_state(self, state):
        self._undo_stack.append(Memento(state))
        self._redo_stack.clear()

    def undo(self):
        if not self._undo_stack:
            return None  # pragma: no cover
        memento = self._undo_stack.pop()
        self._redo_stack.append(memento)
        return memento.get_state()

    def redo(self):
        if not self._redo_stack:
            return None # pragma: no cover
        memento = self._redo_stack.pop()
        self._undo_stack.append(memento)
        return memento.get_state()
