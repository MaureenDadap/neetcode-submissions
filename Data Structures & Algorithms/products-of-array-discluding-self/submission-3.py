class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        products = []

        for i, num in enumerate(nums):
            product = 1

            for j, num2 in enumerate(nums):
                if i == j:
                    continue

                if j == 0:
                    product = num2
                else:
                    product = product * num2

            products += [product]

        return products


            