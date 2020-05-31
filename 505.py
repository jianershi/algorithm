"""
basically when 5 min expires, it needs to be deleted forever.
since hit is quite oftenlly called
we can remove the hit using lazy method at get_hit_count_in_last_5_minutes
we may have to move n prev node
we need to save the count in chronological order in order to move it
we can use a deque, we don't need to record count.
we peek head, then pop if > 5min,
whatever is left in the deque satisfies 5min method
then we just need to count the lngth
"""
from collections import deque
class WebLogger:
    
    def __init__(self):
        # do intialization if necessary
        self.hit_table = deque()

    """
    @param: timestamp: An integer
    @return: nothing
    """
    def hit(self, timestamp):
        # write your code here
        self.hit_table.append(timestamp)

    """
    @param: timestamp: An integer
    @return: An integer
    """
    def get_hit_count_in_last_5_minutes(self, timestamp):
        # write your code here
        while self.hit_table and timestamp - self.hit_table[0] >= 300:
            self.hit_table.popleft()
        return len(self.hit_table)

s = WebLogger()
s.hit(1)
s.hit(2)
s.get_hit_count_in_last_5_minutes(3)
s.hit(300)
s.get_hit_count_in_last_5_minutes(300)
s.get_hit_count_in_last_5_minutes(301)

