class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        length = len(matrix[0])
        for rotate in range(length//2):
            this_len = length - rotate * 2 - 1
            #print("rotate: ", rotate)
            for i in range(this_len):
                c1 = rotate
                c2 = rotate + i
                c3 = rotate + this_len
                c4 = rotate + this_len - i
                p1 = (c1, c2)
                p2 = (c2, c3)
                p3 = (c3, c4)
                p4 = (c4, c1)

            #    print(p1, p2, p3, p4)
            #    print(matrix[c1][c2], matrix[c2][c3], matrix[c3][c4], matrix[c4][c1])
                t = matrix[c1][c2]
                matrix[c1][c2] = matrix[c4][c1]
                matrix[c4][c1] = matrix[c3][c4]
                matrix[c3][c4] = matrix[c2][c3]
                matrix[c2][c3] = t
            #    print(matrix[c1][c2], matrix[c2][c3], matrix[c3][c4], matrix[c4][c1])
