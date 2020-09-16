"""
first try to understand proper data structure for this.
first of all, the server list does not need to be sorted.
it need to support add/remove/pick in O(1)
a hashmap will suffice

to support random access however, we cannot use hashmap because it does not have O(1) enumerate
instead using array.
array usually cannot support o(1) remove,
however, it does not need to be ordered, so we can just using 2 pointers to swap the last element and the element we want to remove
resulting in o(1)
over all, add/remove/pick all in o(1)

in order to implement this, we still need to have a hashmap to record server_id_2_index

"""
import random
class LoadBalancer:
    def __init__(self):
        # do intialization if necessary
        self.server_ids = [] #this is an un ordered list of mahne_ids
        self.server_id_2_index = {}

    """
    @param: server_id: add a new server to the cluster
    @return: nothing
    """
    def add(self, server_id):
        # write your code here
        self.server_ids.append(server_id)
        self.server_id_2_index[server_id] = len(self.server_ids) - 1

    """
    @param: server_id: server_id remove a bad server from the cluster
    @return: nothing
    """
    def remove(self, server_id):
        # write your code here
        if server_id not in self.server_id_2_index:
            return
        index_to_delete = self.server_id_2_index[server_id]
        #print (index_to_delete, self.server_ids, self.server_id_2_index)
        self.server_id_2_index[self.server_ids[-1]] = index_to_delete
        self.server_ids[index_to_delete], self.server_ids[-1] = self.server_ids[-1], self.server_ids[index_to_delete]
        self.server_ids.pop()
        del self.server_id_2_index[server_id]

    """
    @return: pick a server in the cluster randomly with equal probability
    """
    def pick(self):
        # write your code here
        return random.choice(self.server_ids)

s = LoadBalancer()
s.add(406)
s.add(347)
s.remove(406)
s.pick()
s.pick()
s.add(472)
s.pick()
s.pick()
s.remove(347)
s.remove(472)
s.add(595)
s.remove(595)
s.add(200)
s.remove(200)
s.add(38)
s.add(341)
s.remove(341)
s.pick()
s.remove(38)
s.add(689)
