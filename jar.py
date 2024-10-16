class Jar:
    def __init__(self, capacity=12):
        if capacity >= 0:
            self._capacity =capacity
        else:
            raise ValueError("capacity can not me negative")
        self._cookies=0




    def __str__(self):
        str=""
        for i in range(self._cookies):
            str= str + "🍪"
        return str


    def deposit(self, n):
        if n >= 0 and (n + self._cookies) <= self._capacity:
            self._cookies =self._cookies + n
        else:
            raise ValueError("Invalid number of cookies to jar")



    def withdraw(self, n):
        if n <= self._cookies:
            self._cookies = self._cookies-n
        else :
            raise ValueError("less of cookies in jar ")


    @property
    def capacity(self):
        return self._capacity

    @property
    def size(self):
        return self._cookies

