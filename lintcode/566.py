"""
566. GFS Client
"""
'''
Definition of BaseGFSClient
class BaseGFSClient:
    def readChunk(self, filename, chunkIndex):
        # Read a chunk from GFS
    def writeChunk(self, filename, chunkIndex, content):
        # Write a chunk to GFS
'''


class GFSClient(BaseGFSClient):
    """
    @param: chunkSize: An integer
    """
    def __init__(self, chunkSize):
        # do intialization if necessary
        super().__init__()
        self.chunk_size = chunkSize
        self.filename_2_number_of_chunks = {}
    """
    @param: filename: a file name
    @return: conetent of the file given from GFS
    """
    def read(self, filename):
        # write your code her
        if filename not in self.filename_2_number_of_chunks:
            return None
        number_of_chunks = self.filename_2_number_of_chunks[filename]
        result = ""
        for chunk_index in range(number_of_chunks):
            result += super().readChunk(filename, chunk_index)
        return result

    """
    @param: filename: a file name
    @param: content: a string
    @return: nothing
    """
    def write(self, filename, content):
        # write your code here
        number_of_chunks = len(content) // self.chunk_size if len(content) % self.chunk_size == 0 else len(content) // self.chunk_size + 1
        self.filename_2_number_of_chunks[filename] = number_of_chunks
        for chunk_index in range(number_of_chunks):
            super().writeChunk(filename, chunk_index, content[chunk_index * self.chunk_size: self.chunk_size * (chunk_index + 1)])
