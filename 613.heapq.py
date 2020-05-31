"""
613. High Five
since we only have to keep the first 5 largest results, it is ituitive to think
priority queue. we only needs to get rid of the smallest number in the queue
every time.

normally priority queue has insertion and pull time complexity of O(nlogn).
but here, we only need to keep 5 members, so the height of the tree is always 3.
      x
     / \
    x   x
   / \
  x   x
so time complexity becomes O(nlog3) = O(n)
"""
'''
Definition for a Record
class Record:
    def __init__(self, id, score):
        self.id = id
        self.score = score
'''
class Solution:
    # @param {Record[]} results a list of <student_id, score>
    # @return {dict(id, average)} find the average of 5 highest scores for each person
    # <key, value> (student_id, average_score)
    def highFive(self, results):
        import heapq
        student_scores = {} #student_id: heap[]

        for result in results:
            if result.id not in student_scores:
                student_scores[result.id] = []
            heapq.heappush(student_scores[result.id], result.score)
            if len(student_scores[result.id]) > 5:
                heapq.heappop(student_scores[result.id])

        student_average = {}
        for student in student_scores:
            student_average[student] = sum(student_scores[student]) / len(student_scores[student])
        return student_average
