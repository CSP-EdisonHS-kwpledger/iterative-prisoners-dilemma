####
# Each team's file must define four tokens:
#     team_name: a string
#     strategy_name: a string
#     strategy_description: a string
#     move: A function that returns 'c' or 'b'
####

team_name = 'Team Pledger'
strategy_name = 'Opponent\'s Most Common Move'
strategy_description = '''\
Collude on first move.
From second move on, pick whatever the opponent's most common move is.
'''

from statistics import mode
    
def move(my_history, their_history, my_score, their_score):
    '''Make my move based on the history with this player.
    
    history: a string with one letter (c or b) per round that has been played with this opponent.
    their_history: a string of the same length as history, possibly empty. 
    The first round between these two players is my_history[0] and their_history[0]
    The most recent round is my_history[-1] and their_history[-1]
    
    Returns 'c' or 'b' for collude or betray.
    '''

    if len(their_history)==0:     # If this is the first move, 
        return 'c'                # Collude.
    else:
        return mode(their_history) # After that, return their most common move.
    
    
    