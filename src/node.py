from itertools import count

class Node:
    _ids = count(0)
    
    def __init__(self, state=None, parent=None):
        self.state = state
        self.children = set()
        self.parent = parent
        self.visits = 0
        self.value = 0
        self.id = next(self._ids)
    
    def generate_states(self):
        state_list = self.state.generate_states()
        for state in state_list:
            self.children.add(Node(state, parent=self))
        return self.children