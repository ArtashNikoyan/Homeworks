# 1․ Գրել MyList class, որը կունենա գրեթե բոլոր այն մեթոդները և ֆունկցիոնալությունը, որը ունի list class-ը առանց ժառանգելու։
class Mylist:
    def __init__(self, *args):
        self.items = [*args]
    
    def __str__(self):
        return str(self.items)
    
    def __repr__(self):
        return f"{type(Mylist(self.items))} - {self.items}"
    
    def __len__(self):
        return len(self.items)
    
    def __getitem__(self, index):
        if isinstance(index, slice):
            start, stop, step = index.indices(len(self.items))
            return Mylist(*self.items[start:stop:step])
        return self.items[index]
    
    def __setitem__(self, index, value):
        self.items[index] = value
    
    def __delitem__(self, index):
        del self.items[index]
    
    def __iter__(self):
        return iter(self.items)
    
    # Comparison
    def __eq__(self, other):
        return self.items == other.items if isinstance(other, Mylist) else False
    
    def __ne__(self, other):
        return not self.__eq__(other)
    
    def __lt__(self, other):
        return self.items < other.items if isinstance(other, Mylist) else False
    
    def __le__(self, other):
        return self.items <= other.items if isinstance(other, Mylist) else False
    
    def __gt__(self, other):
        return self.items > other.items if isinstance(other, Mylist) else False
    
    def __ge__(self, other):
        return self.items >= other.items if isinstance(other, Mylist) else False
    
    def __bool__(self):
        return bool(self.items)
    
    # Comparison
    def __contains__(self, val):
        return val in self.items
    
    def __add__(self, other):
        if isinstance(other, list | Mylist):
            return Mylist(*self.items + other)
        return NotImplemented
    
    def __radd__(self, other):
        return other + self.items
    
    def __mul__(self, other):
        if isinstance(other, int):
            return Mylist(*self.items * other)
        return NotImplemented
    
    def __rmul__(self, other):
        return other * self.items

    # Methods
    def append(self, val):
        self.items.append(val)
    
    def extend(self, other):
        self.items.extend(other)
        
    def insert(self, index, val):
        self.items.insert(index, val)
        
    def remove(self, val):
        self.items.remove(val)
        
    def pop(self, index=-1):
        self.items.pop(index)
        
    def clear(self):
        self.items.clear()
        
    def index(self, val, start=0, stop=None):
        if stop is None:
            stop = len(self.items)
        return self.items.index(val, start, stop)
    
    def count(self, val):
        return self.items.count(val)
    
    def sort(self, key=None, reverse=False):
        self.items.sort(key=key, reverse=reverse)
    
    def reverse(self):
        self.items.reverse()
    
    def copy(self):
        return Mylist(self.items.copy())