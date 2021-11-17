class Solution:
    def trap(self, height):
        areas = 0
        max_l = max_r = 0
        left= 0
        right= len(height)-1
        while left< right:
            if height[left] < height[right]:
                if height[left] > max_l:
                    max_l = height[left]
                else:
                    areas += max_l - height[left]
                left +=1
            else:
                if height[right] > max_r:
                    max_r = height[right]
                else:
                    areas += max_r - height[right]
                right -=1
        return areas
    height=list(map(int,input().split()))
    print(trap(height))

        