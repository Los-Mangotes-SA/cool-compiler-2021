from NFA import NFA

class DFA(NFA):
    
    def __init__(self, states, finals, transitions, start=0):
        assert all(isinstance(value, int) for value in transitions.values())
        assert all(len(symbol) > 0 for origin, symbol in transitions)
        
        transitions = { key: [value] for key, value in transitions.items() }
        NFA.__init__(self, states, finals, transitions, start)
        self.current = start
        
    def _move(self, symbol):
        try:
            self.current = self.transitions[self.current][symbol][0]
            return True
        except:
            return False
    
    def _reset(self):
        self.current = self.start
        
    def recognize(self, string):
        for char in string:
            if not self._move(char):
                self._reset()
                return False
        if not self.current in self.finals:
            self._reset()
            return False
        self._reset()
        return True