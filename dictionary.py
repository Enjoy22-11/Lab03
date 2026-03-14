class Dictionary:
    def __init__(self):
        self._dict=[]

    def loadDictionary(self,path):
        self._dict = []
        with open(path,'r', encoding='utf8') as f:
            for line in f:
                self.dict.append(line.strip().lower())
        pass


    def printAll(self):
        pass


    @property
    def dict(self):
        return self._dict