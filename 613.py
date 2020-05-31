"""
613. High Five
O(nlogn) for sorting. then iterate through the array once. so o(n)
overall o(nlogn)

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
        # Write your code here
        results.sort(key=lambda x: (x.id, -x.score))

        result = {}
        current_student_total = 0
        last_student = None
        student_score_count = 0
        for i in range(len(results)):
            if last_student is not None and results[i].id != last_student:
                result[last_student] = current_student_total / student_score_count
                current_student_total = 0
                student_score_count = 0

            last_student = results[i].id
            if student_score_count == 5:
                continue
            student_score_count += 1
            current_student_total += results[i].score
        result[last_student] = current_student_total / student_score_count
        return (result)
