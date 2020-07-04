"""
275. Moving Shed
https://www.lintcode.com/problem/moving-shed/description?_from=contest&&fromId=94
TLE
"""
class Solution:
    """
    @param stops: An array represents where each car stops.
    @param k: The number of cars should be covered.
    @return: return the minimum length of the shed that meets the requirements.
    """
    def calculate(self, stops, k):
        # write your code here
        if not stops or len(stops) < 2:
            return 0

        # stops = sorted(stops)
        # print (stops)
        n = len(stops)
        m = max(stops)
        
        first_car = min(stops)
        j = first_car

        stops = set(stops)
        num_of_cars = 0
        max_window_size_required = 0
        for i in range(first_car, m + 1):
            while j < m + 1 and num_of_cars < k:
                if j in stops:
                    num_of_cars += 1
                j += 1

            if num_of_cars >= k:
                max_window_size_required = max(max_window_size_required, j - i)
            
            if i in stops:
                num_of_cars -= 1

        return max_window_size_required


s = Solution()
stops = [8059, 9154, 8728, 3572, 7426, 4462, 3583, 4235, 8482, 2332, 151, 5212, 824, 6324, 3094, 1182, 5837, 4273, 7370, 9742, 7345, 7527, 1740, 2058, 6627, 9428, 3523, 4526, 9583, 2550, 2031, 3519, 608, 8808, 3667, 137, 713, 1926, 4148, 361, 2788, 6456, 1543, 5793, 2120, 8416, 5947, 6767, 323, 1457, 9884, 1582, 6548, 7482, 7977, 6623, 2672, 2606, 8771, 6949, 3600, 9855, 2886, 4150, 6615, 1967, 7124, 1826, 6634, 4964, 5401, 1841, 6987, 9450, 8736, 2962, 238, 9988, 3837, 6149, 8359, 6440, 7354, 8465, 4270, 5152, 244, 9158, 6765, 5572, 1536, 5969, 6514, 1388, 7079, 292, 1221, 6552, 2763, 4360]
k = 90
print(s.calculate(stops, k))

