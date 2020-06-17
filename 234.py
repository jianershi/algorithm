"""
234. Web Crawler
https://www.lintcode.com/problem/web-crawler/description
hmm.. terrible code :(
"""
"""
class HtmlHelper:
    # @param (string)
    # @return (list)
    @classmethod
    def parseUrls(url):
        # Get all urls from a webpage of given url.
"""
from collections import deque
import re
import threading
class Solution:
    """
    @param url(string): a url of root page
    @return (list): all urls
    """
    def __init__(self):
        self.root_domain = None
        self.visited = set()
        self.queue = deque()
        pattern = "(?:https{0,1}:\/\/[a-z0-9]*\.)([a-z0-9]*\.[a-z0-9]*)(?:\/{0,1}.*)"
        self.r1 = re.compile(pattern)

    def crawler(self, url):
        # write your code here

        threads = []
        for index in range(3):
            x = threading.Thread(target=self.worker, args=(url,))
            threads.append(x)
            x.start()

        for index, thread in enumerate(threads):
            thread.join()

        return list(self.visited)

    def worker(self, url):
        self.root_domain = self.r1.findall(url)[0]
        if url not in self.visited:
            self.visited.add(url)
            self.queue.append(url)


        while self.queue:
            head = self.queue.popleft()
            results = HtmlHelper.parseUrls(head)
            for u in results:
                base_urls = self.r1.findall(u)
                if not base_urls or len(base_urls) > 1:
                    continue
                if base_urls[0] != self.root_domain:
                    continue
                if u not in self.visited:
                    self.visited.add(u)
                    self.queue.append(u)
