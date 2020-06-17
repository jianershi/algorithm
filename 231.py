"""
231. Typeahead
https://www.lintcode.com/problem/typeahead/description?_from=ladder&&fromId=75
brute force
"""
class Typeahead:
    """
    @param: dict: A dictionary of words dict
    """
    def __init__(self, dict):
        # do intialization if necessary
        self.dict = dict

    """
    @param: str: a string
    @return: a list of words
    """
    def search(self, str):
        # write your code here
        results = []
        for word in self.dict:
            if str in word:
                results.append(word)
        return results
