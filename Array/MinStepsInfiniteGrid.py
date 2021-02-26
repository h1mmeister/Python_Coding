class Solution:
    # @param A : list of integers
    # @param B : list of integers
    # @return an integer
    def cover_points(self, A, B):
        min_steps = 0
        for i in range(1, len(A)):
            min_steps += max(abs(A[i] - A[i - 1]), abs(B[i] - B[i - 1]))

        return min_steps