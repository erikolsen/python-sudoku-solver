from solver import Solver

if __name__ == '__main__':
    board_string = '040100050107003960520008000000000017000906800803050620090060543600080700250097100'
    solver = Solver(board_string)
    print(f'Initial:  {solver.start_string}')
    solver.solve()
    print(f'Finished: {solver.start_string}')
    finished_string = '346179258187523964529648371965832417472916835813754629798261543631485792254397186'
    print(f'Correct:  {finished_string}')

