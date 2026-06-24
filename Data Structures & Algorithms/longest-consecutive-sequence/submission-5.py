class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums = list(set(nums))

        if len(nums) == 0:
            return 0

        longest = 0
        for n in nums:
            if (n-1) not in nums:
                start = n
                sequence = [start]
                next_num = start + 1

                while next_num is not None:
                    if next_num in nums:
                        sequence = sequence + [next_num]
                        next_num = next_num + 1
                    else:
                        next_num = None 

                if len(sequence) > longest:
                    longest = len(sequence)

        return longest
                                    
