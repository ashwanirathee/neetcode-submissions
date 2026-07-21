class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        hashmap = {}
        def solve(i, j, m, n):
            if i == m-1 and j == n-1:
                return 1
            else:
                if i not in range(m) or j not in range(n):
                    return 0
                else:
                    if (i+1, j) in hashmap:
                        a = hashmap[(i+1, j)]
                    else:
                        a = solve(i+1, j, m, n)
                        hashmap[(i+1,j)] = a
                    
                    if (i, j+1) in hashmap:
                        b = hashmap[(i, j+1)]
                    else:
                        b = solve(i, j+1, m, n)
                        hashmap[(i,j+1)] = b
                    return a + b
        count = solve(0,0, m, n)
        return count
