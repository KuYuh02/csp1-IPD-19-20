####
# Each team's file must define four tokens:
#     team_name: a string
#     strategy_name: a string
#     strategy_description: a string
#     move: A function that returns 'c' or 'b'
####

team_name = 'E1'
strategy_name = 'Betray then Collude'
strategy_description = 'We will betray for the first round. After that, if the other team betrays us when we collude, then the next round we will betray them back. But if they collude with us then we will collude with them as well.'
    
def move(my_history, their_history, my_score, their_score):
    '''Make my move based on the history with this player.
    
    history: a string with one letter (c or b) per round that has been played with this opponent.
    their_history: a string of the same length as history, possibly empty. 
    The first round between these two players is my_history[0] and their_history[0]
    The most recent round is my_history[-1] and their_history[-1]
    
    Returns 'c' or 'b' for collude or betray.
    '''
    
    #This example player always betrays.      
    if len(my_history)==0: # It's the first round; betray.
        return 'b'
    elif my_history[-1]=='c' and their_history[-1]=='b':
        return 'b' # Betray if they were severely punished last time,
    else:
        return 'c' #collude if they collude
