import random
def play():
    user= input("Whats's  your choice?'r' for rock, 'p' for paper,'s' for scissor \n")
    computer= random.choice(['r','p','s'])
    if user== computer:
        return 'tie'
    if is_win(user,computer):
        return 'Won!!!!'
    return 'Lost'

def  is_win(player, opponent):
    #rock > scissor, scissor > paper,paper >rock

    if(player=='r' and opponent=='s')or (player=='s'and opponent=='p')or (player=='p'and opponent=='r'):
        return  True
print(play())