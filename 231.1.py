"""
231. Typeahead
https://www.lintcode.com/problem/typeahead/description?_from=ladder&&fromId=75
"""
class Typeahead:
    """
    @param: dict: A dictionary of words dict
    """
    def __init__(self, dict):
        # do intialization if necessary
        self.dict = dict
        self.substr_dict = {}
        self.build_substr_dict()

    def build_substr_dict(self):
        for word in self.dict:
            n = len(word)
            for i in range(n):
                for j in range(i + 1, n + 1):
                    self.substr_dict[word[i:j]] = self.substr_dict.get(word[i:j], set())
                    self.substr_dict[word[i:j]].add(word)
    """
    @param: str: a string
    @return: a list of words
    """
    def search(self, str):
        # write your code here
        return list(self.substr_dict.get(str, set()))
