class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        good_triplets = set()
        for idx, triplet in enumerate(triplets):
            if triplet[0] > target[0] or triplet[1] > target[1] or triplet[2] > target[2]:
                continue

            print(idx, triplet)
            good_triplets.add(idx)

        exists = [0,0,0]
        for idx, triplet in enumerate(triplets):
            if idx not in good_triplets:
                continue

            if triplet[0] == target[0]:
                exists[0] = 1
            
            if triplet[1] == target[1]:
                exists[1] = 1

            if triplet[2] == target[2]:
                exists[2] = 1

        return True if sum(exists) == 3 else False