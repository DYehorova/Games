import math 
import random


class Player:
    def __init__(self, letter):
        #letter is x or o
        self.letter = letter
    # define all moves
    def get_move(self, game):
        pass

# use inheritance to build random computer player
# and a human player on top of generalized "player"


class RandomComputerPlayer(Player):
    def __init__(self, letter):
        super().__init__(letter)
    
    def get_move(self, game):
        # returns randomly chosen value from the list
        square = random.choice(game.available_moves())
        return square

class HumanPlayer(Player):
    def __init__(self, letter):
        super().__init__(letter)
    
    def get_move(self, game):
        valid_square = False
        val = None
        while not valid_square:
            square = input(self.letter + '\'s turn. Input move (0-8):')
            # need to check that the value is correct
            # it is an integer, the spot is available on the board
            try:
                val = int(square)
                if val not in game.available_moves():
                    raise ValueError
            except ValueError:
                print('Invalid Square Try again.')
            
            return val 

class SmartComputerPlayer(Player):

    def __init__(self, letter):
        super().__init__(letter)
    
    def get_move(self, game):
        # returns randomly chosen value from the list
        if len(game.available_moves()) == 9:
             square = random.choice(game.available_moves())
        else: 
            # get the square based on minimax algorithm
            square = self.minimax(game, self.letter)['position']
        return square
    
    def minimax(self, state, player):
        #state screenshots of the game
        max_player = self.letter #yourself
        other_player = 'O' if player == 'X' else 'X' # the other player

        # check whether there was a winner in previous move
        if state.current_winner == other_player:
            return {'position': None,
                    'score' : 1 * (state.num_empty_squares()+1) if other_player == max_player 
                    else -1 * (state.num_empty_squares()+1)
                    }
        elif not state.empty_squares(): # no empty squares
            return {'position': None, 'score': 0}

        if player == max_player:
            best = {'position' : None, 'score': -math.inf} # each score should maximize 
        else:
            best = {'position' : None, 'score': math.inf} # each score should minimize
       
        for possible_move in state.available_moves():
            # step 1: make a move, try that spot
            state.make_move(possible_move, player)
            
            # step 2: recurse using minimax to simulate a game after making that move
            sim_score = self.minimax(state, other_player)
            
            # step 3: undo the move
            state.board[possible_move] = ' '
            state.current_winner = None
            sim_score['position'] = possible_move
            
            # step 4: update the dictionaries if necessary
            if player == max_player: # maximize the max player
                if sim_score['score'] > best['score']:
                    best = sim_score # replace best score
            else: # minimize the other player
                if sim_score['score'] < best['score']:
                    best = sim_score    
        return best




