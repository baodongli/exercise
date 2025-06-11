class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        '''
        rowRemDigits = [set([str(c) for c in range(1, 10)]) for _ in range(9)]
        colRemDigits = [set([str(c) for c in range(1, 10)]) for _ in range(9)]
        gridRemDigits = [set([str(c) for c in range(1, 10)]) for _ in range(9)]
        cellToFill = []

        def getChoices(cell):
            row, col = cell
            gi = (row // 3) * 3 + col // 3
            return rowRemDigits[row] & colRemDigits[col] & gridRemDigits[gi]

        def cell_comp(c1, c2):
            nonlocal rowRemDigits, colRemDigits, gridRemDigits
            c1Choices = getChoices(c1)
            c2Choices = getChoices(c2)
            #print(c1, ": ", c1Choices, c2, ": ", c2Choices)
            #print(rowRemDigits[row1], colRemDigits[col1], gridRemDigits[gi1])
            #print(rowRemDigits[row2], colRemDigits[col2], gridRemDigits[gi2])
            sz1 = len(c1Choices)
            sz2 = len(c2Choices)
            if sz1 > sz2:
                return 1
            elif sz1 < sz2:
                return -1
            else:
                return 0

        for row in range(9):
            rowDigits = []
            for col in range(9):
                digit = board[row][col]
                if board[row][col] == '.':
                    cellToFill.append((row, col))
                else:
                    rowRemDigits[row].remove(digit)
                    colRemDigits[col].remove(digit)
                    gridRemDigits[(row // 3) * 3 + col // 3].remove(digit)
        
        cellToFill = sorted(cellToFill, key=cmp_to_key(cell_comp), reverse=True)
        #print(cellToFill)

        stack = []
        while cellToFill:
            cell = cellToFill.pop()
            choices = getChoices(cell)
            row, col = cell
            #print(row, col, choices)
            while not choices:
                cellToFill.append(cell)
                cell, digit, choices = stack.pop()
                row, col = cell
                board[row][col] = '.'
                rowRemDigits[row].add(digit)
                colRemDigits[col].add(digit)
                gridRemDigits[(row // 3) * 3 + col // 3].add(digit)

            digit = choices.pop()
            
            #print(stack)
            rowRemDigits[row].remove(digit)
            colRemDigits[col].remove(digit)
            gridRemDigits[(row // 3) * 3 + col // 3].remove(digit)
            board[row][col] = digit
            stack.append((cell, digit, choices))
        # print(board)
        '''
        rowDigitsUsed = [[False for _ in range(9)] for _ in range(9)]
        colDigitsUsed = [[False for _ in range(9)] for _ in range(9)]
        gridDigitsUsed = [[False for _ in range(9)] for _ in range(9)]
        cellToFill = []

        def getChoices(cell):
            nonlocal rowDigitsUsed, colDigitsUsed, gridDigitsUsed
            row, col = cell
            gi = (row // 3) * 3 + col // 3
            choices = []
            for i in range(9):
                if not rowDigitsUsed[row][i] and not colDigitsUsed[col][i] and not gridDigitsUsed[gi][i]:
                    choices.append(str(i + 1))
            return choices

        def cell_comp(c1, c2):
            c1Choices = getChoices(c1)
            c2Choices = getChoices(c2)
            #print(c1, ": ", c1Choices, c2, ": ", c2Choices)
            #print(rowRemDigits[row1], colRemDigits[col1], gridRemDigits[gi1])
            #print(rowRemDigits[row2], colRemDigits[col2], gridRemDigits[gi2])
            sz1 = len(c1Choices)
            sz2 = len(c2Choices)
            if sz1 > sz2:
                return 1
            elif sz1 < sz2:
                return -1
            else:
                return 0

        for row in range(9):
            rowDigits = []
            for col in range(9):
                digit = board[row][col]
                if board[row][col] == '.':
                    cellToFill.append((row, col))
                else:
                    v = int(digit) - 1
                    rowDigitsUsed[row][v] = True
                    colDigitsUsed[col][v] = True
                    gridDigitsUsed[(row // 3) * 3 + col // 3][v] = True
        
        cellToFill = sorted(cellToFill, key=cmp_to_key(cell_comp), reverse=True)
        #print(cellToFill)

        stack = []
        while cellToFill:
            cell = cellToFill.pop()
            choices = getChoices(cell)
            row, col = cell
            #print(row, col, choices)
            while not choices:
                cellToFill.append(cell)
                cell, digit, choices = stack.pop()
                row, col = cell
                board[row][col] = '.'
                v = int(digit) - 1
                rowDigitsUsed[row][v] = False
                colDigitsUsed[col][v] = False
                gridDigitsUsed[(row // 3) * 3 + col // 3][v] = False

            digit = choices.pop()
            v = int(digit) - 1
            
            #print(stack)
            rowDigitsUsed[row][v] = True
            colDigitsUsed[col][v] = True
            gridDigitsUsed[(row // 3) * 3 + col // 3][v] = True
            board[row][col] = digit
            stack.append((cell, digit, choices))
