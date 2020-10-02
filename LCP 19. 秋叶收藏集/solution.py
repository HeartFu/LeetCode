class Solution:
    def minimumOperations(self, leaves: str) -> int:
        n = len(leaves)
        f = [[0, 0, 0] for _ in range(n)]
        f[0][0] = int(leaves[0] == "y")
        f[0][1] = f[0][2] = f[1][2] = float("inf")

        for i in range(1, n):
            leaf = leaves[i]
            f[i][0] = f[i - 1][0] + int(leaf != 'r')
            f[i][1] = min(f[i - 1][0], f[i - 1][1]) + int(leaf != 'y')
            if i >= 2:
                f[i][2] = min(f[i - 1][1], f[i - 1][2]) + int(leaf != 'r')
            
        return f[n - 1][2]
