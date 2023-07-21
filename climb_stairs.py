import sys


class Solution:
    # Function to count number of ways to reach the nth stair.

    def __init__(self):
        sys.setrecursionlimit(10**6)
        self.mem = {1: 1, 2: 2}

    def countWays(self, n):
        if (n in self.mem):
            return self.mem[n]
        else:
            self.mem[n] = (self.countWays(n - 1) +
                           self.countWays(n - 2)) % 1000000007
            return self.mem[n]
