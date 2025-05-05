#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'crosswordPuzzle' function below.
#
# The function is expected to return a STRING_ARRAY.
# The function accepts following parameters:
#  1. STRING_ARRAY crossword
#  2. STRING words
#
def revertHorizontal(crossword, row, columns):
    for col in columns:
        crossword[row][col] = '-'
        
def revertVertical(crossword, col, rows):
    for row in rows:
        crossword[row][col] = '-'
        
def solvePuzzle(crossword, word_locations, words, length_map, word_used, word_no):
    if word_no == len(words):
        return True
    potential_words = []
    pos, dir, length = word_locations[word_no]

    for word_index in length_map[length]:
        word = words[word_index]
        if not word_used[word]:
            c = crossword[pos[0]][pos[1]]
            if c == '-':
                potential_words.append(word_index)
            elif c == word[0]:
                potential_words.append(word_index)

    solved = False
    for word_index in potential_words:
        # Fill it
        word = words[word_index]
        filled = True
        if dir == 'h':
            columns = []
            for col in range(pos[1], pos[1] + length):
                if crossword[pos[0]][col] == '-':
                    columns.append(col)
                    crossword[pos[0]][col] = word[col - pos[1]]
                elif crossword[pos[0]][col] != word[col - pos[1]]:
                    # revert
                    revertHorizontal(crossword, pos[0], columns)
                    filled = False
                    break
            if not filled:
                continue       
            word_used[word] = True
            if solvePuzzle(crossword, word_locations, words, length_map, word_used, word_no + 1):
                solved = True
                break
            word_used[word] = False
            # doesn't solve, revert it
            revertHorizontal(crossword, pos[0], columns)
        else:
            rows = []
            for row in range(pos[0], pos[0] + length):
                if crossword[row][pos[1]] == '-':
                    rows.append(row)
                    crossword[row][pos[1]] = word[row - pos[0]]
                elif crossword[row][pos[1]] != word[row - pos[0]]:
                    revertVertical(crossword, pos[1], rows)
                    filled = False
                    break
            if not filled:
                continue
            word_used[word] = True
            if solvePuzzle(crossword, word_locations, words, length_map, word_used, word_no + 1):
                solved = True
                break
            word_used[word] = False
            revertVertical(crossword, pos[1], rows)         
    
    return solved        

    
def crosswordPuzzle(crossword, words):
    # Write your code here
    # find all the rows and columns that need to be filled
    
    puzzle = [[crossword[row][col] for col in range(len(crossword[0]))] for row in range(len(crossword))]
    puzzle_words = words.split(";")
    word_locations = []
    for row, _ in enumerate(crossword):
        horizontal_length = 0
        start_col = -1
        for col, c in enumerate(crossword[row]):
            if c == '-':
                horizontal_length += 1
                
                if start_col < 0:
                    start_col = col

                # check vertical
                if row - 1 < 0 or crossword[row-1][col] != '-':
                    vertical_length = 1
                    row1 = row + 1
                    while row1 < len(crossword) and crossword[row1][col] == '-':
                        vertical_length += 1
                        row1 += 1
                    if vertical_length > 1:
                        word_locations.append(((row, col), 'v', vertical_length))
            elif c == "+":
                if horizontal_length > 1: 
                    word_locations.append(((row, start_col), 'h', horizontal_length))
                start_col = -1
                horizontal_length = 0
        if horizontal_length > 1: 
            word_locations.append(((row, start_col), 'h', horizontal_length))
    length_map = {}
    word_used = {}
    for index, word in enumerate(puzzle_words):
        length = len(word)
        if length not in length_map:
            length_map[length] = []        
        length_map[length].append(index)
        word_used[word] = False

    solved = solvePuzzle(puzzle, word_locations, puzzle_words, length_map, word_used, 0)
    result = []
    for row in puzzle:
        result.append("".join(row))
    return result
    
if __name__ == '__main__':
    '''
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    crossword = []

    for _ in range(10):
        crossword_item = input()
        crossword.append(crossword_item)

    words = input()

    result = crosswordPuzzle(crossword, words)

    fptr.write('\n'.join(result))
    fptr.write('\n')

    fptr.close()
    '''
    crosswordPuzzle(["+-++++++++", "+-++-+++++", "+-------++", "+-++-+++++", "+-++-+++++", "+-++-+++++", "++++-+++++", "++++-+++++", "++++++++++", "----------"], "CALIFORNIA;NIGERIA;CANADA;TELAVIV")

