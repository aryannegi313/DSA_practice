def max_area(height):
    left = 0
    right = len(height) - 1
    max_water = 0
    
    while left < right:
        h = min(height[left], height[right])
        b = right - left
        area = h * b
        max_water = max(area, max_water)
        
        if height[right] < height[left]:
            right = right -1
        else:
            left = left + 1
    
    return max_water
            
    
    
height = [1, 8, 6, 2, 5, 4, 8, 3, 7]
print(max_area(height))  # 49