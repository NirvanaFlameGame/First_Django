class Mylist(list):
    def index (value):
        result = super().index(value)
        for index, item in enumerate(self):
        return result +100

lst = Mylist ([34,1,'hello', True])
print (lst.index(1))