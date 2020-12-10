class Collection:
    def __init__(self,List):
        self.data = dict()
        for l in List:
            self.data[l] = True
    def add(self,key):
        self.data[key] = True
    def __contains__(self,key):
        try:
            return self.data[key]
        except:
            return False