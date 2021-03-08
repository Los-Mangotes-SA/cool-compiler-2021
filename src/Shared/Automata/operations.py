from Shared.Tools.utils import ContainerSet

def move(automaton, states, symbol):
    moves = set()
    for state in states:
        try:
            for new in automaton.transitions[state][symbol]:
                moves.add(new)
        except KeyError:
            continue
        
    return moves

def epsilon_closure(automaton, states):
    pending = [ s for s in states ]
    closure = { s for s in states }
    
    while pending:
        state = pending.pop()
        try:
            for new in automaton.transitions[state]['']:
                if not new in closure:
                    pending.append(new)
                    closure.add(new)
        except:
            continue
                
    return ContainerSet(*closure)