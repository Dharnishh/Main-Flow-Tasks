def maximal_rectangle(matrix):
    if not matrix:
        return 0
    max_area = 0
    dp = [0] * len(matrix[0])
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            dp[j] = dp[j] + 1 if matrix[i][j] == '1' else 0
        stack = []
        for j in range(len(dp) + 1):
            while stack and (j == len(dp) or dp[stack[-1]] >= dp[j]):
                height = dp[stack.pop()]
                width = j if not stack else j - stack[-1] - 1
                max_area = max(max_area, height * width)
            stack.append(j)
    return max_area

# Example usage
matrix = [
    ["1","0","1","0","0"],
    ["1","0","1","1","1"],
    ["1","1","1","1","1"],
    ["1","0","0","1","0"]
]
print("Maximal Rectangle Area:", maximal_rectangle(matrix))