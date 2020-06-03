"""
565. Heart Beat

"""
class HeartBeat:

    def __init__(self):
        # do intialization if necessary
        self.last_heartbeat = {} #slave_ip, timestamp
        self.k = None
    """
    @param: slaves_ip_list: a list of slaves'ip addresses
    @param: k: An integer
    @return: nothing
    """
    def initialize(self, slaves_ip_list, k):
        # write your code here
        for slave_ip in slaves_ip_list:
            self.last_heartbeat[slave_ip] = 0
        self.k = k
    """
    @param: timestamp: current timestamp in seconds
    @param: slave_ip: the ip address of the slave server
    @return: nothing
    """
    def ping(self, timestamp, slave_ip):
        # write your code here
        if slave_ip not in self.last_heartbeat:
            return
        self.last_heartbeat[slave_ip] = timestamp

    """
    @param: timestamp: current timestamp in seconds
    @return: a list of slaves'ip addresses that died
    """
    def getDiedSlaves(self, timestamp):
        # write your code here
        result = []
        for slave_ip, timestamp_slave in self.last_heartbeat.items():
            if timestamp - timestamp_slave >= 2 * self.k:
                result.append(slave_ip)

        return result
