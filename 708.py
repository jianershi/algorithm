"""
708. Elevator system - OO Design
https://www.lintcode.com/problem/elevator-system-oo-design/description?_from=ladder&&fromId=98
"""
class Direction:
    UP = 'UP'
    DOWN = 'DOWN'

class Status:
    UP = 'UP'
    DOWN = 'DOWN'
    IDLE = 'IDLE'

class Request:
    def __init__(self,l = 0):
        self.level = l
        
    def getLevel(self):
        return self.level

class ElevatorButton:
    def __init__(self,level,e):
        self.level = level
        self.elevator = e
        
    def pressButton(self):
        request = InternalRequest(self.level)
        self.elevator.handleInternalRequest(request);

class ExternalRequest(Request):
    def __init__(self,l = 0,d = None):
        Request.__init__(self,l)
        self.direction = d

    def getDirection(self):
        return self.direction

class InternalRequest(Request):
    def __init__(self,l = None):
        Request.__init__(self,l)

class Elevator:
    def __init__(self, n):
        # Keep them, don't modify.
        self.buttons = []
        self.upStops = []
        self.downStops = []
        for i in range(n):
            self.upStops.append(False)
            self.downStops.append(False)
        self.currLevel = 0
        self.status = Status.IDLE

    def insertButton(self,eb):
        self.buttons.append(eb)

    def handleExternalRequest(self,r):
        # Write your code here
            
        if r.direction == Direction.UP:
            self.upStops[r.getLevel() - 1] = True
            if self.status == Status.IDLE:
            # if self.noRequests(self.downStops):
                self.status = Status.UP
        elif r.direction == Direction.DOWN:
            self.downStops[r.getLevel() - 1] = True
            if self.status == Status.IDLE:
            # if self.noRequests(self.upStops):
                self.status = Status.DOWN
        
    def handleInternalRequest(self,r):
        # Write your code here
        if self.status == Status.UP:
            if r.getLevel() <= self.currLevel:
                return
            self.upStops[r.getLevel() - 1] = True
        elif self.status == Status.DOWN:
            if r.getLevel() >= self.currLevel:
                return
            self.downStops[r.getLevel() - 1] = True
        else: #idle
            if r.getLevel() < self.currLevel:
                self.downStops[r.getLevel() - 1] = True
                self.status = Status.DOWN
            elif r.getLevel() > self.currLevel:
                self.upStops[r.getLevel() - 1] = True
                self.status = Status.UP

    def openGate(self):
        # Write your code here
        if self.status == Status.DOWN:
            for i in range(len(self.downStops)):
                next_level = (self.currLevel - i) % len(self.downStops)
                if self.downStops[next_level]:
                    self.currLevel = next_level
                    self.downStops[next_level] = False
                    break
                    
        elif self.status == Status.UP:
            for i in range(len(self.upStops)):
                next_level = (self.currLevel + i) % len(self.downStops)
                if self.upStops[next_level]:
                    self.currLevel = next_level
                    self.upStops[next_level] = False
                    break
        
    def closeGate(self):
        # Write your code here  
        # if self.status == Status.IDLE:
        #     if self.noRequests(self.downStops):
        #         self.status = Status.UP
        #         return
            
        #     if self.noRequests(self.upStops):
        #         self.status = Status.DOWN
        #         return

        if self.noRequests(self.downStops) and self.noRequests(self.upStops):
            self.status = Status.IDLE
            return
        
        if not self.noRequests(self.downStops) and not self.noRequests(self.upStops):
            return
            
        if self.noRequests(self.downStops):
            self.status = Status.UP
        elif self.noRequests(self.upStops):
            self.status = Status.DOWN

    def noRequests(self, stops):
        for stop in stops:
            if stop:
                return False
        return True
    
    def elevatorStatusDescription(self):
        description = "Currently elevator status is : " + self.status + \
                      ".\nCurrent level is at: " + str(self.currLevel + 1) + \
                      ".\nup stop list looks like: " + self.toString(self.upStops) + \
                      ".\ndown stop list looks like:  " + self.toString(self.downStops) + \
                      ".\n*****************************************\n"
        return description
        
    @classmethod
    def toString(cls, stops):
        return str(stops).replace("False", "false").replace("True", "true")


e = Elevator(10)
e.handleExternalRequest(ExternalRequest(1, Direction.UP))
print(e.elevatorStatusDescription())
e.handleExternalRequest(ExternalRequest(5, Direction.UP))
print(e.elevatorStatusDescription())
e.handleExternalRequest(ExternalRequest(4, Direction.DOWN))
print(e.elevatorStatusDescription())
e.handleExternalRequest(ExternalRequest(7, Direction.DOWN))
print(e.elevatorStatusDescription())
e.handleExternalRequest(ExternalRequest(4, Direction.DOWN))
print(e.elevatorStatusDescription())
e.handleExternalRequest(ExternalRequest(7, Direction.DOWN))
print(e.elevatorStatusDescription())
e.handleExternalRequest(ExternalRequest(4, Direction.DOWN))
print(e.elevatorStatusDescription())
e.handleExternalRequest(ExternalRequest(7, Direction.DOWN))
print(e.elevatorStatusDescription())
e.openGate()
print(e.elevatorStatusDescription())
e.closeGate()
print(e.elevatorStatusDescription())
e.openGate()
print(e.elevatorStatusDescription())
e.closeGate()
print(e.elevatorStatusDescription())
e.openGate()
print(e.elevatorStatusDescription())
e.closeGate()
print(e.elevatorStatusDescription())
e.openGate()
print(e.elevatorStatusDescription())
e.closeGate()
print(e.elevatorStatusDescription())
e.openGate()
print(e.elevatorStatusDescription())
e.closeGate()
print(e.elevatorStatusDescription())
e.openGate()
print(e.elevatorStatusDescription())
e.closeGate()
print(e.elevatorStatusDescription())
e.openGate()
print(e.elevatorStatusDescription())
e.closeGate()
print(e.elevatorStatusDescription())
e.openGate()
print(e.elevatorStatusDescription())
e.closeGate()
print(e.elevatorStatusDescription())