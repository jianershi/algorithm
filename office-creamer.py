class Solution:
    def max_amount_to_order(self, onHand, supplier, demand):
        supplier.sort()

        left = 0
        right = len(supplier)

        while left + 1 < right:
            mid = (left + right) // 2
            if self.is_valid(onHand, supplier, demand, mid):
                left = mid
            else:
                right = mid

        if self.is_valid(onHand, supplier, demand, right):
            return right
        return left

    def is_valid(self, on_hand, supplier, demand, mid):
        new_on_hand = on_hand + supplier[-mid:]
        new_on_hand.sort()

        i = 0
        days = 0
        for i in range(0,len(new_on_hand), demand):
            for j in range(0, min(demand, len(new_on_hand) - i)):
                if new_on_hand[i + j] - days < 0:
                    return False
            days += 1
        return True

s = Solution()
onHand = [1,0,1]
supplier = [2,0,2,0,0,2]
demand = 2
print(s.max_amount_to_order(onHand, supplier, demand))
