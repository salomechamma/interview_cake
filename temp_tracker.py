class Temp_Tracker(object):

    def __init__(self):
        self.min = 111
        self.max = -1
        self.sum = 0
        self.occurence = [0] * 111
        self.total_nb = 0
        self.max_occ = 0
        self.mode = -1

    def insert(self,value):
        self.occurence[value] +=1 
        self.total_nb += 1
        if self.occurence[value] > self.max_occ:
            self.max_occ = self.occurence[value]
            self.mode = value
            print self.mode
        if self.min > value:
            self.min = value
        if self.max < value:
            self.max = value
        self.sum += value

    def get_min(self):
        if self.total_nb != 0:
            return self.min
        else:
            return None
    
    def get_max(self):
        if self.total_nb != 0:
            return self.max
        else:
            return None

    def mean(self):
        return self.sum/self.total_nb

    def model(self):
        print self.mode
        # return self.mode


t = Temp_Tracker()
t.insert(3)
t.insert(9)
t.insert(3)
t.get_max()
t.get_min()
t.model()