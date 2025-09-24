class Counter:
    def __init__(self):
        self.__value = 0
    
    def getValue(self):
        return self.__value
    
    def click(self):
        self.__value += 1
    
    def reset(self):
        self.__value = 0

class CounterMax:
    def __init__(self, limit):
        self.__value = 0
        self.__limit = limit
    
    def getValue(self):
        return self.__value
    
    def click(self):
        if self.__value >= self.__limit:
            print('Limit exceeded')
            return
        self.__value += 1
    
    def reset(self):
        self.__value = 0

class CounterStr:
    def __init__(self):
        self.__value = ''
    
    def getValue(self):
        return self.__value
    
    def click(self):
        self.__value += '|'
    
    def reset(self):
        self.__value = ''
