
team_name = 'Sexy Boize' # Only 10 chars displayed.
strategy_name = 'Epic Points'
strategy_description = '''First round always collude. We retaliate if we
received a severe punishment last round. If their constantly betraying, we
betray with them. If they constantly collude, we betray. If none of these 
conditions are met, we collude.
'''
    
def move(my_history, their_history, my_score, their_score):
    if len(my_history == 0):
      return 'c'
    elif my_history[-1] == 'c' and their_history[-1] == 'b':
      return 'b'
    elif their_history[-1] == their_history[-2] == their_history[-3] == 'b':
      return 'b'
    elif their_history[-1] == their_history[-2] == 'c':
      return 'b'
    else:
      return 'c'
