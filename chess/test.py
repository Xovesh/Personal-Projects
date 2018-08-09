from chess import Game,Table,Piece
from chess.pieces import King, Knight, Rook, Bishop, Pawn

a = Game.Chess()
a.visualizeboard()

def start(self):
    a = self.table.getplayboard()
    a[2][0] = Knight.Knight(32, "Black", 2, 0)
    a[3][0] = Knight.Knight(32, "Black", 3, 0)
    self.pawnmovement()