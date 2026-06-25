class Solution:
    def maxArea(self, heights: List[int]) -> int:
        result = 0
        
        l = 0
        r = len(heights) - 1

        areas = []

        while l < r:
            l_height = heights[l]
            r_height = heights[r]
            
            height = min(l_height, r_height)
            width = r - l

            area = height * width        
            areas.append(area)

            # print("\n===========")
            # print("left: ", l_height)
            # print("right: ", r_height)
            # print("height: ", height)
            # print("width: ", width)
            # print("area: ", area)
            # print("result: ", result)

            if l_height < r_height:
                l += 1
            elif l_height > r_height:
                r -= 1
            else:
                r -= 1

        return sorted(areas)[-1]