"""
1786. Pub Sub Pattern
"""
'''
Definition of PushNotification
class PushNotification:
    @classmethod
    def notify(user_id, message):
'''
class PubSubPattern:
    def __init__(self):
    # do intialization if necessary
        self.channels = {} #channel: set(subscribers)

    """
    @param: channel: a channel name
    @param: user_id: a user id
    @return: nothing
    """
    def subscribe(self, channel, user_id):
        # write your code here
        if channel not in self.channels:
            self.channels[channel] = set()
        self.channels[channel].add(user_id)

    """
    @param: channel: a channel name
    @param: user_id: a user id
    @return: nothing
    """

    def unsubscribe(self, channel, user_id):
    	# write your code here
        if channel not in self.channels:
            return
        if user_id not in self.channels[channel]:
            return
        self.channels[channel].remove(user_id)

    """
    @param: channel: a channel name
    @param: message: need send message
    @return: nothing
    """

    def publish(self, channel, message):
		# write your code here
        if channel not in self.channels:
            return
        for user_id in self.channels[channel]:
            PushNotification.notify(user_id, message)
