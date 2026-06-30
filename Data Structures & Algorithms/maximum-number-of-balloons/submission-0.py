class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        freq = {}
        for i in text:
            freq[i] = freq.get(i, 0) + 1

        print(freq)
        count = 0
        running = True
        while running:
            for i in "balloon":
                if i in freq.keys() and freq[i] > 0:
                    freq[i] -= 1
                else:
                    running = False
                    break
            if running != False:
                count+=1

        return count