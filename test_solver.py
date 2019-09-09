from solver import Solver
import random
import pytest
import pdb
# @pytest.mark.skip
# start_string = '864371259325849761971265843436192587198657432257483916689734125713528694542916378'
# solver = Solver(start_string)
#864371259
#325849761
#971265843
#436192587
#198657432
#257483916
#689734125
#713528694
#542916378

# indexes
# zero  =  [ 0,  1,  2,  9, 10, 11, 18, 19, 20]
# one   =  [ 3,  4,  5, 12, 13, 14, 21, 22, 23]
# two   =  [ 6,  7,  8, 15, 16, 17, 24, 25, 26]

# three =  [27, 28, 29, 36, 37, 38, 45, 46, 47]
# four  =  [30, 31, 32, 39, 40, 41, 48, 49, 50]
# five  =  [33, 34, 35, 42, 43, 44, 51, 52, 53]

# six   =  [54, 55, 56, 63, 64, 65, 72, 73, 74]
# seven =  [57, 58, 59, 66, 67, 68, 75, 76, 77]
# eight =  [60, 61, 62, 69, 70, 71, 78, 79, 80]
# return num in [ self.start_string[x] for x in [zero, one, two, three, four, five, six, seven, eight][box]]

def test_stores_initial_string():
    start_string = '004300209005009001070060043006002087190007400050083000600000105003508690042910300'
    solver = Solver(start_string)
    assert solver.start_string == start_string

def test_initial_length():
    short_string = '0'
    expected_error = "Expected length is 81 characters. 0 is 1 character long."

    with pytest.raises(Exception) as e:
        Solver(short_string)
    assert str(e.value) == expected_error

def test_numericality():
    short_string = 'a'*81
    expected_error = f'Expected {short_string} to contain only numbers.'

    with pytest.raises(Exception) as e:
        Solver(short_string)
    assert str(e.value) == expected_error

def test_sets_next_empty_returns_true():
    start_string = '860371259325849761971265843436192587198657432257483916689734125713528694542916378'
    solver = Solver(start_string)
    index_of_empty = 2

    assert solver.find_next_empty() == True
    assert solver.next_empty == index_of_empty

def test_sets_next_empty_returns_false_when_finished():
    start_string = '864371259325849761971265843436192587198657432257483916689734125713528694542916378'
    solver = Solver(start_string)

    assert solver.find_next_empty() == False

def test_next_empty_starts_with_none():
    start_string = '860371259325849761971265843436192587198657432257483916689734125713528694542916378'
    solver = Solver(start_string)

    assert solver.next_empty == None

def test_row_has_number():
    start_string = '064371259325849761971265843436192587198657432257483916689734125713528694542916378'
    solver = Solver(start_string)
    row = 0
    missing = '8'
    present = '1'

    assert solver.row_has_number(row,missing) == False
    assert solver.row_has_number(row,present) == True

def test_col_has_number():
    start_string = '064371259325849761971265843436192587198657432257483916689734125713528694542916378'
    solver = Solver(start_string)
    col = 0
    missing = '8'
    present = '3'

    assert solver.col_has_number(col,missing) == False
    assert solver.col_has_number(col,present) == True

def test_box_has_number():
    # start_string = '064371259325049761971265843436192587198657432257483916689734125713528694542916378'
    start_string = '064371259325049761971265043436192507190657432257403916609734125713520694542916370'
    #864 371 259
    #325 849 761
    #971 265 843

    #436 192 587
    #198 657 432
    #257 483 916

    #689 734 125
    #713 528 694
    #542 916 378
    solver = Solver(start_string)
    box = 6
    missing = '8'
    present = '3'

    assert solver.box_has_number(box,missing) == False
    assert solver.box_has_number(box,present) == True

def test_valid_trial():
    start_string = '064371259325849761971265843436192587198657432257483916689734125713528694542916378'
    solver = Solver(start_string)
    #864371259
    #325849761
    #971265843
    #436192587
    #198657432
    #257483916
    #689734125
    #713528694
    #542916378
    possible = '8'
    impossible = '6'
    index = 0
    assert solver.valid_trial(index, possible) == True
    assert solver.valid_trial(index, impossible) == False

def test_row_for():
    start_string = '864371259325849761971265843436192587198657432257483916689734125713528694542916378'
    solver = Solver(start_string)

    assert solver.row_for(1) == 0
    assert solver.row_for(13) == 1
    assert solver.row_for(25) == 2
    assert solver.row_for(80) == 8

def test_col_for():
    start_string = '864371259325849761971265843436192587198657432257483916689734125713528694542916378'
    solver = Solver(start_string)
    assert solver.col_for(0) == 0
    assert solver.col_for(1) == 1
    assert solver.col_for(12) == 3
    assert solver.col_for(80) == 8

def test_box_for():
    start_string = '864371259325849761971265843436192587198657432257483916689734125713528694542916378'
    solver = Solver(start_string)
    #864 371 259
    #325 849 761
    #971 265 843

    #436 192 587
    #198 657 432
    #257 483 916

    #689 734 125
    #713 528 694
    #542 916 378
    assert solver.box_for(0) == 0
    assert solver.box_for(4) == 1
    assert solver.box_for(28) == 3
    assert solver.box_for(64) == 6

def test_replace():
    start_string = '004300209005009001070060043006002087190007400050083000600000105003508690042910300'
    solver = Solver(start_string)
    next_string = '804300209005009001070060043006002087190007400050083000600000105003508690042910300'
    value = '8'
    index = 0
    solver.replace(index, value)
    assert solver.start_string == next_string

def test_solve():
    start_string =  '004300209005009001070060043006002087190007400050083000600000105003508690042910300'
    # start_string = '864371259025849761971265843436192587198657432257483916689734125713528694542916378'
    finished_string = '864371259325849761971265843436192587198657432257483916689734125713528694542916378'
    solver = Solver(start_string)

    solver.solve()
    # print('Actual: 864371259325849761971265843436192587198657432257483916689734125713528694542916378')

    assert solver.start_string == finished_string


