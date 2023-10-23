import random

class RandomizedSet:

    def __init__(self):
        self.content = []
    def insert(self, val: int) -> bool:
        if val not in self.content:
            self.content.append(val)
            return True
        else:
            return False
    def remove(self, val: int) -> bool:
        if val in self.content:
            self.content.remove(val)
            return True
        else:
            return False
    def getRandom(self) -> int:
        index = random.randint(1, len(self.content))
        return self.content[index - 1]


class RandomizedSet1:
    def __init__(self):
        self.val_list = []
        self.index_dict = {}
    def insert(self, val: int) -> bool:
        if val not in self.index_dict:
            self.val_list.append(val)
            self.index_dict[val] = len(self.val_list) - 1
            return True
        return False
    def remove(self, val: int) -> bool:
        if val in self.index_dict:
            temp = self.val_list[-1]
            index = self.index_dict[val]
            self.val_list[index] = temp
            self.index_dict[temp] = index
            self.val_list.pop()
            del self.index_dict[val]
            return True
        return False
    def getRandom(self) -> int:
        return random.choice(self.val_list)


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()

obj = RandomizedSet()
param_1 = obj.insert(1)
param_2 = obj.remove(2)
param_3 = obj.getRandom()
pass