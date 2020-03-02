####
# Each team's file must define four tokens:
#     team_name: a string
#     strategy_name: a string
#     strategy_description: a string
#     move: A function that returns 'c' or 'b'
####
probe_number=0
team_name = 'Bruhloe' # Only 10 chars displayed.
strategy_name = 'Probe master97'
strategy_description = 'Big Brain strats'
    
def move(my_history, their_history, my_score, their_score):
    if len(my_history) <= 2:
        if len(my_history) == 0:
            return('b')
        if len(my_history) >= 1:
            return('c')
        if their_history[-1] == ('c'):
            probe_number=(probe_number+1)
    elif probe_number >= 2:
        return('b')
    else:
	if their_history[-1] == ('b'):				
            return('b')
        if their_history[-1] == ('c'):
            return('c')