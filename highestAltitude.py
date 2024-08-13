from typing import List


class Solution:
    def largestAltitude(self, gain: List[int]) -> int:

        currAlt = maxAlt = 0

        for i in gain:

            currAlt += i

            if currAlt > maxAlt:
                maxAlt = currAlt

        return maxAlt
