from Tile import Tile

class Agent:

    MIN_VALUE = -1000000
    MAX_VALUE= 1000000

    def __init__(self, game, color, max_depth):
        self.game = game
        self.color = color
        self.max_depth = max_depth
    

    def do_min_max(self, current_board):
        move, value = self.max(current_board, self.color, 0, self.MIN_VALUE, self.MAX_VALUE)
        return move
    

    def max(self, current_board, current_color, depth, alpha: int, beta: int):
       
        if (self.game.check_terminal(current_board, current_color)):
            return None, self.game.evaluate(current_board, current_color, -1000)

        if (depth == self.max_depth):
            return None, self.game.evaluate(current_board, current_color, )

        possible_moves =  self.game.generate_all_possible_moves(current_board, current_color)
        best_move = None
        best_move_value = self.MIN_VALUE
        for move in possible_moves:
            temp_move, value = self.min(current_board.next_board(current_color, move), self.game.opponent(current_color), depth + 1, alpha, beta)
            if (value > best_move_value):
                best_move_value = value
                best_move = move
            if beta <= value:
                return best_move, best_move_value
                # implement alpha-beta here
                
        return best_move, best_move_value

   
    def min(self, current_board, current_color, depth, alpha: int, beta: int):
        if (self.game.check_terminal(current_board, current_color)):
            return None, self.game.evaluate(current_board, current_color, +1000)

        if (depth == self.max_depth):
            return None, self.game.evaluate(current_board, current_color)

        possible_moves = self.game.generate_all_possible_moves(current_board, current_color)
        best_move = None
        best_move_value = self.MAX_VALUE
        for move in possible_moves:
            temp_move, value = self.max(current_board.next_board(current_color, move),
                                        self.game.opponent(current_color), depth + 1, alpha, beta)
            if (value < best_move_value):
                best_move_value = value
                best_move = move
            if alpha >= value:
                return best_move, best_move_value
                # implement alpha-beta here

        return best_move, best_move_value




